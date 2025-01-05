import re

def is_valid_email(email):
   
    email_regex = r"^(?!.*[!#$%&'*+/=?^_`{|}]{2,})[a-zA-Z0-9!#$%&'*+/=?^_`{|}]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}]+)*" \
                  r"@[a-zA-Z0-9-]+(?:\.[a-zA-Z]{2,})$"
    return re.match(email_regex, email) is not None


emails = [
    "valid.email@example.com",
    "invalid..email@example.com",
    "valid-email@example.co",
    "invalid-email@.example.com",
    "invalid@domain",
    "invalid@domain..com",
]

for email in emails:
    print(f"{email}: {'Valid' if is_valid_email(email) else 'Invalid'}")
