password=input("Enter your password:\n")
upper=True
for i in password:
    if i.isupper():
        upper=False
        break
if len(password)<8:
    print("Password is too short.")
elif upper:
    print("Password must contain an uppercase letter.")
else:
    print('Password is strong.')