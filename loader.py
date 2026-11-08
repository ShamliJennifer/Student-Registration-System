"""CSV import and export helpers."""

import csv
from pathlib import Path

from validator import validate_contact

FIELDS = ["name", "phone", "email"]


def load_contacts(file_path: str = "contacts.csv") -> tuple[list[dict], dict]:
    """Load valid unique records and return them with an import summary."""
    records = []
    seen_phones = set()
    seen_emails = set()
    summary = {"total": 0, "accepted": 0, "invalid": 0, "duplicates": 0}

    path = Path(file_path)
    if not path.exists():
        return records, summary

    with path.open("r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
            summary["total"] += 1
            name = (row.get("name") or "").strip()
            phone = (row.get("phone") or "").strip()
            email = (row.get("email") or "").strip()

            valid, _ = validate_contact(name, phone, email)
            if not valid:
                summary["invalid"] += 1
                continue

            email_key = email.casefold()
            if phone in seen_phones or email_key in seen_emails:
                summary["duplicates"] += 1
                continue

            seen_phones.add(phone)
            seen_emails.add(email_key)
            records.append({"name": name, "phone": phone, "email": email})
            summary["accepted"] += 1

    return records, summary


def save_contacts(records: list[dict], file_path: str = "students_clean.csv") -> None:
    """Write student records to a CSV file."""
    with Path(file_path).open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(records)
