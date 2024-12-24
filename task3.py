import re

def assess_password_strength(password):
    strength = 0
    feedback = []
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")


    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")

    if strength == 5:
        feedback.append("Your password is very strong!")
    elif strength == 4:
        feedback.append("Your password is strong.")
    elif strength == 3:
        feedback.append("Your password is moderate. Consider adding more complexity.")
    elif strength == 2:
        feedback.append("Your password is weak. Consider adding more complexity.")
    else:
        feedback.append("Your password is very weak. Please make it more complex.")

    return strength, feedback

password = input("Enter your password: ")
strength, feedback = assess_password_strength(password)

print(f"\nPassword Strength Score: {strength}/5")
print("suggessions:")
for item in feedback:
    print(f"- {item}")
