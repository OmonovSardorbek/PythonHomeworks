def is_prime(x):
	if x==1: 
		return False
	for i in range(2, int(x**0.5+1)):
		if x%i==0:
			return False
	return True

while True:
	n=input("Enter a number:\n")
	if not n.isdecimal():
		print("Invalid input, enter integer number!")
		continue
	if is_prime(int(n)):
		print(n,"is prime number")
		break
	else:
		print(n, "is not prime number")
		break
	
