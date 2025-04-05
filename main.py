# Take input from the user
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Function to calculate HCF
def calculate_hcf(a, b):
    while b:
        a, b = b, a % b
    return a

# Calculate LCM using the formula: LCM = (number1 * number2) // HCF
hcf = calculate_hcf(number1, number2)
lcm = (number1 * number2) // hcf

print("LCM is: ", lcm)