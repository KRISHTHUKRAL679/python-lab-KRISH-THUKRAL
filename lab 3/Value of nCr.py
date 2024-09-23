import math

def calculate_nCr(n, r):
    # Calculate nCr using the formula nCr = n! / (r! * (n-r)!)
    if r > n:
        return 0  # nCr is 0 if r > n
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

# Get user input for n and r
try:
    n = int(input("Enter the value of n: "))
    r = int(input("Enter the value of r: "))
    
    if n < 0 or r < 0:
        print("n and r must be non-negative integers.")
    else:
        # Calculate nCr
        result = calculate_nCr(n, r)
        
        # Print the result
        print(f"The value of {n}C{r} is {result}")
except ValueError:
    print("Invalid input. Please enter integer values.")
