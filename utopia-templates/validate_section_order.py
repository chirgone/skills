#!/usr/bin/env python3
"""
Utopia Vertical Page - Section Order Validator
===============================================
Validates that a generated/edited Utopia vertical page follows the canonical
section order derived from the gold Retail template.

Usage:
    python3 validate_section_order.py <file.html>
    python3 validate_section_order.py /tmp/healthcare_reordered.html

Exit codes:
    0 = All sections in correct order, no contamination
    1 = Section order mismatch or contamination found

This script is the SINGLE SOURCE OF TRUTH for section ordering.
Any future vertical generator or manual edit MUST pass this validator.
"""

import re
import sys
import os

# ============================================================================
# CANONICAL SECTION ORDER (derived from gold-retail.html)
# Each tuple: (section_id, h1_pattern, expand_pattern, required)
#
# h1_pattern:    regex to match the H1 heading text (case-insensitive)
# expand_pattern: regex to match the EXPAND title text (case-insensitive)
# required:      True = must exist, False = optional (e.g., Product Checklist)
# ============================================================================
CANONICAL_ORDER = [
    ("INTRO",
     None,
     None,
     True),

    ("USE_CASES",
     r"Customer Use Cases and Journeys",
     r"Explore sector-specific use cases",
     True),

    ("TOP_10",
     r"Top 10 .+ (?:Sector )?Use Cases",
     None,  # H1 is inside the table, not a standalone expand
     True),

    ("PRODUCT_CHECKLIST",
     r"Product Checklist|Product Deployment",
     r"Product Deployment Status",
     False),  # Optional - not all verticals have it

    ("MEDDPICC",
     r"MEDDPICC",
     r"MEDDPICC for",
     True),

    ("UTOPIA_VISION",
     r"Cloudflare.s Utopia for .+",
     r"Cloudflare.s vision",
     True),

    ("FRAMEWORK",
     r"Cloudflare .+ Framework",
     r"Get Started|Architectural Framework",
     True),

    ("PHASED_DEPLOYMENT",
     r"implementation by phases",
     r"Phased Deployment",
     True),

    ("COMMERCIAL_FOCUS",
     r"Commercial Focus .* Value Proposition",
     r"Products to Lead With",
     True),

    ("SCOPING_QUESTIONS",
     r"Phased Commercial Qualification",
     r"Sequential Opportunity Assessment",
     True),

    ("BUNDLES",
     r"(Cloudflare Service Models|Service Models)",
     r"Cloudflare Bundles",
     True),

    ("CONCLUSION",
     r"Conclusion",
     r"Conclusions",
     True),

    ("RESOURCES",
     r"Featured Videos",
     r"Cloudflare Resources",
     True),

    ("BACK_LINK",
     r"Back to Utopia Framework",
     None,
     True),
]

# ============================================================================
# CONTAMINATION TERMS (forbidden cross-vertical language)
# ============================================================================
CONTAMINATION_TERMS = {
    "retail": [
        "retailer", "shopping cart", "shopper", "Black Friday",
        "e-commerce", "inventory scanner", "POS system",
        "live shopping", "product demos", "boosting conversion",
        "merchandise", "scalper", "Global Shoppers",
    ],
    "hospitality": [
        "check-in", "concierge", "hotel guest", "room service",
        "booking engine", "front desk", "housekeeping",
    ],
    "casino": [
        "gambling", "betting", "casino", "wager", "poker",
        "sportsbook", "Apuesta Total",
    ],
    "government": [
        "citizen portal", "government entities", "public sector",
        "municipal", "civic", "e-government",
    ],
}

# Exceptions: terms that look like contamination but are legitimate
CONTAMINATION_EXCEPTIONS = [
    "Magecart",         # Cybersecurity term, not retail
    "cardholder",       # PCI DSS term
    "card data",        # PCI DSS term
    "credit card",      # General payment term
    "marketplace",      # Can be legitimate in FinServ context
    "Battle Card",      # Internal sales term
    "Waiting Room",     # Cloudflare product name, not hospitality
    "room service",     # Only when preceded by "Waiting Room" (handled by context check below)
    "ticket scalper",   # Valid in airlines (fare scalping), education (event tickets)
    "check-in kiosk",   # Valid in airlines (self-service check-in)
    "check-in",         # Valid in airlines, healthcare (patient check-in)
]


def extract_section_markers(content):
    """Extract H1 headings and EXPAND titles in document order."""
    markers = []

    # Find all H1 headings with their positions
    # Supports: <h1><strong>Text</strong></h1>, <h1>Text</h1>, <h1><a href="...">Text</a></h1>
    for m in re.finditer(r'<h1[^>]*>(?:<strong>|<a[^>]*>)?\s*([^<]+?)\s*(?:</strong>|</a>)?</h1>', content):
        text = m.group(1).strip()
        # Decode &amp; back to & for matching
        text = text.replace('&amp;', '&')
        markers.append(("H1", text, m.start()))

    # Find all EXPAND titles with their positions
    for m in re.finditer(r'<ac:parameter ac:name="title">([^<]+)</ac:parameter>', content):
        text = m.group(1).strip()
        text = text.replace('&amp;', '&')
        markers.append(("EXPAND", text, m.start()))

    # Sort by position in document
    markers.sort(key=lambda x: x[2])
    return markers


def find_section_positions(markers):
    """Map each canonical section to its position in the document."""
    found = {}
    used_markers = set()

    for section_id, h1_pat, expand_pat, required in CANONICAL_ORDER:
        best_pos = None

        if h1_pat:
            for i, (mtype, text, pos) in enumerate(markers):
                if mtype == "H1" and i not in used_markers:
                    if re.search(h1_pat, text, re.IGNORECASE):
                        best_pos = pos
                        used_markers.add(i)
                        break

        if expand_pat and best_pos is None:
            for i, (mtype, text, pos) in enumerate(markers):
                if mtype == "EXPAND" and i not in used_markers:
                    if re.search(expand_pat, text, re.IGNORECASE):
                        best_pos = pos
                        used_markers.add(i)
                        break

        if best_pos is not None:
            found[section_id] = best_pos
        elif section_id == "INTRO":
            found[section_id] = 0  # Intro is always at position 0

    return found


def validate_order(found):
    """Check that found sections appear in canonical order."""
    errors = []

    # Get sections that were found, sorted by their document position
    found_sorted = sorted(found.items(), key=lambda x: x[1])
    found_order = [s[0] for s in found_sorted]

    # Get expected order (only sections that were found)
    canonical_ids = [s[0] for s in CANONICAL_ORDER]
    expected_order = [s for s in canonical_ids if s in found]

    if found_order != expected_order:
        errors.append("SECTION ORDER MISMATCH")
        errors.append(f"  Expected: {' -> '.join(expected_order)}")
        errors.append(f"  Got:      {' -> '.join(found_order)}")
        errors.append("")

        # Find specific out-of-order sections
        for i, (got, expected) in enumerate(zip(found_order, expected_order)):
            if got != expected:
                errors.append(f"  Position {i+1}: expected [{expected}] but found [{got}]")

    return errors


def validate_required_sections(found):
    """Check that all required sections are present."""
    errors = []
    for section_id, h1_pat, expand_pat, required in CANONICAL_ORDER:
        if required and section_id not in found:
            errors.append(f"MISSING REQUIRED SECTION: [{section_id}]")
            if h1_pat:
                errors.append(f"  Expected H1 matching: {h1_pat}")
            if expand_pat:
                errors.append(f"  Expected EXPAND matching: {expand_pat}")
    return errors


def validate_contamination(content, vertical):
    """Check for cross-vertical contamination."""
    errors = []

    for source, terms in CONTAMINATION_TERMS.items():
        if source == vertical:
            continue  # Don't flag terms from the page's own vertical

        for term in terms:
            # Case-insensitive search
            matches = list(re.finditer(re.escape(term), content, re.IGNORECASE))
            # Filter out exceptions
            real_matches = []
            for m in matches:
                context = content[max(0, m.start()-40):m.end()+40]
                is_exception = any(exc.lower() in context.lower() for exc in CONTAMINATION_EXCEPTIONS)
                # Special case: "Waiting Room services" is Cloudflare product, not hospitality
                if term.lower() == "room service" and "waiting room" in context.lower():
                    is_exception = True
                if not is_exception:
                    real_matches.append(m)

            if real_matches:
                errors.append(f"CONTAMINATION [{source}]: '{term}' found {len(real_matches)}x")
                for m in real_matches[:2]:
                    ctx = content[max(0, m.start()-30):m.end()+30].replace('\n', ' ')
                    errors.append(f"  ...{ctx}...")

    return errors


def validate_ampersands(content):
    """Check for raw ampersands that should be &amp;."""
    errors = []
    raw = re.findall(r'&(?!amp;|lt;|gt;|quot;|#\d)', content)
    if raw:
        errors.append(f"RAW AMPERSANDS: {len(raw)} found (must be &amp; in XHTML)")
    return errors


def validate_phase6(content):
    """Check that Phase 6 (AI) exists in key sections."""
    errors = []
    phase6_markers = ["Phase 6", "AI Security", "AI Governance", "AI Gateway", "Firewall for AI"]
    found_any = any(m in content for m in phase6_markers)
    if not found_any:
        errors.append("MISSING PHASE 6: No AI Security/Governance section found")
    return errors


def detect_vertical(content):
    """Auto-detect which vertical this page is for.
    
    Uses the page title (H1 or first line) as primary signal.
    Falls back to body content patterns.
    """
    # Priority 1: Match from the page title (first 2000 chars)
    title_zone = content[:2000]
    title_patterns = [
        ("government", r"Government|Public Sector"),
        ("retail", r"Retail"),
        ("hospitality", r"Hospitality"),
        ("healthcare", r"Healthcare|Pharma"),
        ("finserv", r"Financial Services|FinServ"),
        ("telco", r"Telco|Telecom"),
        ("media", r"Media.*Entertainment"),
        ("universities", r"Education|University"),
        ("utilities", r"Utilities|Critical Infra"),
        ("airlines", r"Airlines|Aviation"),
        ("automotive", r"Automotive"),
    ]
    for vertical, pattern in title_patterns:
        if re.search(pattern, title_zone, re.IGNORECASE):
            return vertical

    # Priority 2: Full body scan
    vertical_patterns = {
        "retail": r"Retail Sector|retail sector",
        "hospitality": r"Hospitality|Hotels? &",
        "healthcare": r"Healthcare|Pharma|HIPAA|PHI",
        "finserv": r"Financial Services|FinServ|PCI DSS|DORA",
        "government": r"Government|Public Sector|Citizen",
        "telco": r"Telco|Telecom|MNO|MVNO",
        "media": r"Media.*Entertainment|Streaming|OTT",
        "universities": r"Education|Universit",
        "utilities": r"Utilities|Critical Infra|SCADA",
        "airlines": r"Airlines|Aviation|Airline",
        "automotive": r"Automotive|Connected Vehicle",
    }
    for vertical, pattern in vertical_patterns.items():
        if re.search(pattern, content, re.IGNORECASE):
            return vertical
    return "unknown"


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file.html> [--vertical NAME]")
        print(f"       {sys.argv[0]} /tmp/healthcare_reordered.html")
        sys.exit(1)

    filepath = sys.argv[1]
    if not os.path.exists(filepath):
        print(f"ERROR: File not found: {filepath}")
        sys.exit(1)

    # Optional vertical override
    vertical_override = None
    if "--vertical" in sys.argv:
        idx = sys.argv.index("--vertical")
        if idx + 1 < len(sys.argv):
            vertical_override = sys.argv[idx + 1]

    content = open(filepath).read()
    vertical = vertical_override or detect_vertical(content)

    print(f"=" * 60)
    print(f"UTOPIA SECTION ORDER VALIDATOR")
    print(f"=" * 60)
    print(f"File:     {filepath}")
    print(f"Chars:    {len(content):,}")
    print(f"Vertical: {vertical}")
    print(f"-" * 60)

    # Run all validations
    markers = extract_section_markers(content)
    found = find_section_positions(markers)

    print(f"\nSections found: {len(found)}/{len(CANONICAL_ORDER)}")
    for section_id, pos in sorted(found.items(), key=lambda x: x[1]):
        print(f"  [{section_id}] at position {pos:,}")

    all_errors = []

    # 1. Required sections
    errors = validate_required_sections(found)
    all_errors.extend(errors)

    # 2. Section order
    errors = validate_order(found)
    all_errors.extend(errors)

    # 3. Contamination
    errors = validate_contamination(content, vertical)
    all_errors.extend(errors)

    # 4. Ampersands
    errors = validate_ampersands(content)
    all_errors.extend(errors)

    # 5. Phase 6
    errors = validate_phase6(content)
    all_errors.extend(errors)

    print(f"\n{'=' * 60}")
    if all_errors:
        print(f"FAILED: {len(all_errors)} issue(s) found\n")
        for err in all_errors:
            print(f"  {err}")
        print(f"\n{'=' * 60}")
        sys.exit(1)
    else:
        print(f"PASSED: All validations OK")
        print(f"  - Section order: correct")
        print(f"  - Required sections: all present")
        print(f"  - Contamination: none detected")
        print(f"  - Ampersands: clean")
        print(f"  - Phase 6: present")
        print(f"{'=' * 60}")
        sys.exit(0)


if __name__ == "__main__":
    main()
