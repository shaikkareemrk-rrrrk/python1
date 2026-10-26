# Student Email and Identifier Validation

# Student details
students = [
    ("arun@gmail.com", "CSE-101"),
    ("banu@gmailcom", "CSE101"),
    ("charan@@gmail.com", "CSE-@03"),
    ("@gmail.com", "ECE-"),
    ("divya123@yahoo.com", "AIML-205")
]

print("STUDENT EMAIL AND ID VALIDATION")
print("-" * 40)

for email, reg_id in students:
    print("\nEmail:", email)
    print("Registration ID:", reg_id)

    # Email validation
    if "@" not in email or "." not in email:
        print("Email Error: Missing @ or domain dot")
    elif email.count("@") != 1:
        print("Email Error: Invalid @ separator")
    elif email.startswith("@") or email.endswith("@"):
        print("Email Error: Missing email name or domain")
    elif " " in email:
        print("Email Error: Contains spaces")
    else:
        print("Email: Valid format")

    # Registration ID validation
    if "-" not in reg_id:
        print("ID Error: Missing hyphen")
    else:
        parts = reg_id.split("-")

        if len(parts) != 2:
            print("ID Error: Invalid separator")
        elif parts[0] == "" or parts[1] == "":
            print("ID Error: Missing ID component")
        elif not parts[0].isalpha() or not parts[1].isdigit():
            print("ID Error: Invalid character groups")
        else:
            print("Registration ID: Valid format")