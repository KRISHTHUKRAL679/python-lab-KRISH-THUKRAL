import math

def calculate_nCr(n, r):
    if r > n:
        return 0  # nCr is 0 if r > n
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

try:
    n = int(input("Enter the value of n: "))
    r = int(input("Enter the value of r: "))
    
    if n < 0 or r < 0:
        print("n and r must be non-negative integers.")
    else:
        result = calculate_nCr(n, r)
        print(f"The value of {n}C{r} is {result}")
except ValueError:
    print("Invalid input. Please enter integer values.")
