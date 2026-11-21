
import re

def validate_password(password):
    checks = [
        (
            len(password) >= 12,
            "Use at least 12 characters."
        ),
        (
            re.search(r"[a-z]", password) is not None,
            "Add a lowercase letter."
        ),
        (
            re.search(r"[A-Z]", password) is not None,
            "Add an uppercase letter."
        ),
        (
            re.search(r"\d", password) is not None,
            "Add a number."
        ),
        (
            re.search(r"[^A-Za-z0-9]", password) is not None,
            "Add a symbol."
        )
    ]

    issues = [
        message for passed, message in checks
        if not passed
    ]

    return not issues, issues


if __name__ == "__main__":
    candidate = input("Enter a password to check: ")
    valid, issues = validate_password(candidate)

    if valid:
        print("Password meets all example rules.")
    else:
        print("Suggestions:")
        for issue in issues:
            print("-", issue)
