password = "Secure3p@123"


if len(password) < 6:
    strength = "weak"
elif len(password) <= 10:
    strength = "Medium"
else:
    strength = "Strong"


print("strength of the given password is : ", strength)




