# Password Generator — CodSoft Internship Project

import random
import string

def generate_password(length):
    if length < 4:
        print("Length too short. Use at least 4 characters.")
        return

    # Character pool
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    print(f"\nGenerated Password: {password}")

# Main execution
try:
    user_input = int(input("Enter desired password length: "))
    generate_password(user_input)
except ValueError:
    print("Invalid input. Please enter a valid number.")