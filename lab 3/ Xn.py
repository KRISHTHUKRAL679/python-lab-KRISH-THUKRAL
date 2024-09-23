def compute_power(base, exponent):
    return base ** exponent
try:
    base = float(input("Enter the base (X): "))
    exponent = int(input("Enter the exponent (n): "))
    
    result = compute_power(base, exponent)
    
    print(f"{base} raised to the power of {exponent} is {result}")
except ValueError:
    print("Invalid input. Please enter numeric values.")
