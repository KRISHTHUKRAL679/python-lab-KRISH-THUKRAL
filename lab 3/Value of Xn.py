def compute_power(base, exponent):
    # Calculate base raised to the power of exponent
    return base ** exponent

# Get user input for base and exponent
try:
    base = float(input("Enter the base (X): "))
    exponent = int(input("Enter the exponent (n): "))
    
    # Compute the power
    result = compute_power(base, exponent)
    
    # Print the result
    print(f"{base} raised to the power of {exponent} is {result}")
except ValueError:
    print("Invalid input. Please enter numeric values.")
