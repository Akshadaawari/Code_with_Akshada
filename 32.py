#.Write a program that keeps taking user input for password until ‘Enter’ key is pressed and then checks password with following validation:
import re

def validate_password(password):
   
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter."
    if not re.search(r"\d", password):
        return "Password must contain at least one digit."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password must contain at least one special character."
    return "Valid password!"

def main():
    passwords = []
    print("Enter passwords one by one. Press 'Enter' without typing anything to stop.")
    
    while True:
        pwd = input("Enter a password: ").strip()
        if pwd == "":
            break
        passwords.append(pwd)
    
    print("\nPassword Validation Results:")
    for idx, pwd in enumerate(passwords, 1):
        result = validate_password(pwd)
        print(f"{idx}. Password: {pwd} -> {result}")

if __name__ == "__main__":
    main()
