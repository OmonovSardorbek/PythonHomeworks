def convert_cel_to_far(celsius):
    return celsius * 9 / 5 + 32
def convert_far_to_cel(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

fahrenheit = float(input("Enter a temperature in degrees F: "))
celsius = convert_far_to_cel(fahrenheit)
print(f"{fahrenheit} degrees F = {celsius:.2f} degrees C")

celsius = float(input("\nEnter a temperature in degrees C: "))
fahrenheit = convert_cel_to_far(celsius)
print(f"{celsius} degrees C = {fahrenheit:.2f} degrees F")

