"""Simple analytics for student contact records."""

from collections import Counter


def generate_report(students: list[dict], import_summary: dict | None = None) -> str:
    """Build and return a readable summary of the current records."""
    total = len(students)
    prefixes = Counter(item["phone"][0] for item in students if item.get("phone"))
    domains = Counter(
        item["email"].rsplit("@", 1)[-1].casefold()
        for item in students if "@" in item.get("email", "")
    )

    lines = [
        "\n========== STUDENT ANALYTICS ==========",
        f"Current student records: {total}",
    ]
    if import_summary is not None:
        lines.extend([
            f"Imported rows: {import_summary.get('total', 0)}",
            f"Accepted rows: {import_summary.get('accepted', 0)}",
            f"Invalid rows: {import_summary.get('invalid', 0)}",
            f"Duplicate rows: {import_summary.get('duplicates', 0)}",
        ])

    lines.append("\nPHONE PREFIX DISTRIBUTION")
    for prefix in "6789":
        lines.append(f"{prefix}: {prefixes.get(prefix, 0)}")

    lines.append("\nEMAIL DOMAIN BREAKDOWN")
    if domains:
        for domain, count in sorted(domains.items()):
            lines.append(f"{domain}: {count}")
    else:
        lines.append("No email records available.")

    lines.append("=======================================")
    return "\n".join(lines)
