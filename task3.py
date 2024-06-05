# Checking the password length is Strong, Good or Bad check it - the checker basically.

import re

def check_password_strength(password):
    # Criteria checks
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'\d', password) is not None
    special_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    
    # Strength assessment
    strength = 0
    if length_criteria:
        strength += 1
    if uppercase_criteria:
        strength += 1
    if lowercase_criteria:
        strength += 1
    if number_criteria:
        strength += 1
    if special_criteria:
        strength += 1

    # Feedback based on strength
    feedback = ""
    if strength == 5:
        feedback = "Your password is very strong."
    elif strength == 4:
        feedback = "Your password is strong."
    elif strength == 3:
        feedback = "Your password is good."
    elif strength == 2:
        feedback = "Your password is weak."
    else:
        feedback = "Your password is very weak."

    # Detailed feedback for missing criteria
    if not length_criteria:
        feedback += " It should be at least 8 characters long."
    if not uppercase_criteria:
        feedback += " It should include at least one uppercase letter."
    if not lowercase_criteria:
        feedback += " It should include at least one lowercase letter."
    if not number_criteria:
        feedback += " It should include at least one number."
    if not special_criteria:
        feedback += " It should include at least one special character (e.g., !@#$%^&*)."
    
    return feedback

def main():
    print("Password Strength Checker")
    while True:
        password = input("Enter a password to check its strength: ")
        feedback = check_password_strength(password)
        print(feedback)
        continue_choice = input("Do you want to check another password? (Y/N): ").upper()
        if continue_choice != 'Y':
            break

if __name__ == "__main__":
    main()