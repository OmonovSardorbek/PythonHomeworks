string = input("Enter a string: ")
symbol = "*"
vowels = "aeiouAEIOU"
result = ""
for i in string:
    if i in vowels: i=symbol
    result += i
print("Result:", result)
