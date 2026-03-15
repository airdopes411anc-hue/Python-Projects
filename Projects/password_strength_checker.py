print("======================================")
print("      PASSWORD STRENGTH CHECKER      ")
print("======================================\n")


password = input("Enter your Password: ")

length=len(password)
Upper = password == password.lower()
Lower = password == password.upper()
digit = not password.isalpha()
special_characters = not password.isalnum()

strength = 0

if Upper is False:
    strength += 1 
if Lower is False:
    strength += 1 
if digit is True:
    strength += 1
if special_characters is True:
    strength += 1
if length >= 10:
    strength += 1
    

print("\n--------------------------------------")
print("🔎 Password Analysis Results:")
print("--------------------------------------")
print("Length of Password:", length)
print("Contains Uppercase Letter:", "Yes" if not Upper else "No")
print("Contains Lowercase Letter:", "Yes" if not Lower else "No")
print("Contains Digit:", "Yes" if digit else "No")
print("Contains Special Character:", "Yes" if special_characters else "No")
print("--------------------------------------")

if length < 8:
    print("Password is too short")
elif strength <= 2:
    print("\nPassword Strength: WEAK")
elif strength == 3 or strength == 4:
    print("\nPassword Strength: MODERATE")
else:
    print("\nPassword Strength: STRONG \n")

