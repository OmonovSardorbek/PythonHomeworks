def print_factors(n):
    for i in range(1, n+1):
        if n%i==0:
            print(f"{i} is a factor of {n}")
n=input("Enter a positive integer: ")
if not n.isdecimal():
    print("Invalid input, enter a positive integer!")
else:
    print_factors(int(n))
