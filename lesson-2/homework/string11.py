s="0123456789"
user_input = input("Enter a string: ")
for i in user_input:
    if i in s:
        print("This string contains a digit")
        exit()
print("This string does not contain any digit")