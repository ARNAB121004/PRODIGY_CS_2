import string

def check_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    score = 0
    feedback = []

    if length >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters.")

    if has_upper:
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if has_lower:
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if has_digit:
        score += 1
    else:
        feedback.append("Add numbers.")

    if has_special:
        score += 1
    else:
        feedback.append("Add special characters (!@#$, etc.).")

    strength = {
        0: "Very Weak",
        1: "Weak",
        2: "Moderate",
        3: "Strong",
        4: "Very Strong",
        5: "Excellent"
    }[score]

    return strength, feedback

def main():
    print("=== Password Strength Checker ===")
    password = input("Enter your password: ")

    strength, feedback = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Suggestions:")
        for tip in feedback:
            print(f" - {tip}")

if __name__ == "__main__":
    main()
