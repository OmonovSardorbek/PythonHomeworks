def invest(amount, rate, years):
    for i in range(years):
        amount=amount*(100+rate)/100
        print(f"year {i+1}: {amount:.2f}")
try:
    amount, rate, years = map(int, input("Enter an initial amount, an annual percentage rate and a number of years: ").split())
    invest(amount, rate, years)
except:
    print("Invalid input, enter integer numbers separated by a space!")
