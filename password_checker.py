def password_check(password):
    special = "!@#$%"
    if len(password) < 8:
        return "Weak"
    digit = False
    special_char = False
    for ch in password:
        if ch.isdigit():
            digit = True
        if ch in special:
            special_char = True
    if digit and special_char:
        return "Strong"
    else:
        return "Weak"
password = input("Enter password: ")
print("Password Strength =", password_check(password))

