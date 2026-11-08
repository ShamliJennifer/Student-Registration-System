"""Validation helpers for student contact records."""

import re


def validate_contact(name: str, phone: str, email: str) -> tuple[bool, str]:
    """Return (is_valid, message) for a student's contact information."""
    if not name or not name.strip():
        return False, "Name cannot be empty."

    cleaned_phone = (phone or "").strip()
    if not re.fullmatch(r"[6-9]\d{9}", cleaned_phone):
        return False, "Phone must be 10 digits and start with 6, 7, 8, or 9."

    cleaned_email = (email or "").strip()
    if " " in cleaned_email or cleaned_email.count("@") != 1:
        return False, "Enter an email address with one @ symbol and no spaces."

    local, domain = cleaned_email.split("@")
    if not local or not domain or "." not in domain:
        return False, "Enter a valid email domain, such as name@example.com."
    if domain.startswith(".") or domain.endswith(".") or ".." in domain:
        return False, "Email domain is not valid."

    return True, "Contact details are valid."
