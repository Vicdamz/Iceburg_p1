import string
import random

def generate_password():
    password_length = int(input("Enter the desired password length: "))
    include_numbers = input("Include numbers?  (yes/no): ").lower() == "yes"
    include_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"
    
    # Start with base letters
    password_characters = string.ascii_letters

    # Add characters based on user choices
    if include_numbers:
        password_characters += string.digits
    if include_special_chars:
        password_characters += string.punctuation

    password = ''.join(random.choice(password_characters) for _ in range(password_length))

    ##print("Generated password:", password)
    return password
   