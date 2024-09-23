def is_disarium_number(number):
    # Convert the number to a string to easily iterate over its digits
    str_num = str(number)
    
    # Initialize the sum to 0
    sum_of_powers = 0
    
    # Iterate over the digits and their positions
    for index, digit in enumerate(str_num):
        # Convert the digit back to an integer
        digit = int(digit)
        # Compute the power of the digit (position + 1)
        power = index + 1
        # Add the result to the sum_of_powers
        sum_of_powers += digit ** power
    
    # Check if the computed sum of powers equals the original number
    return sum_of_powers == number

# Example usage:
number = int(input("Enter a number to check: "))
if is_disarium_number(number):
    print(f"{number} is a Disarium Number.")
else:
    print(f"{number} is not a Disarium Number.")
