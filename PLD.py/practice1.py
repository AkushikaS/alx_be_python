password = input("Enter the password: ")
length = len(password)
score = 0
#has_digit = False

if length >= 8:
    score += 1
    print(score)
for char in password:
    if char.isupper():
        score += 1
        print(score)
        break
for c in password:
    if c.isdigit():
        score += 1
        #has_digit = True
        print(score)
        break
print("Password strength score:", score)
print(password)
print(length)
if score == 3:  #and has_digit
    print("Strong password")
elif score == 2:
    print("Moderate password")
else :
    print("Weak password")