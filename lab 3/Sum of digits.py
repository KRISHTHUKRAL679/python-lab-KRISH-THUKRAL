def sum_of_digits(number):
    # Ensure the number is positive for digit extraction
    number = abs(number)
    
    # Convert the number to a string to easily iterate over its digits
    str_num = str(number)
    
    # Compute the sum of the digits
    total_sum = sum(int(digit) for digit in str_num)
    
    return total_sum

# Get user input
try:
    number = int(input("Enter a number: "))
    
    # Calculate the sum of digits
    result = sum_of_digits(number)
    
    # Print the result
    print(f"The sum of the digits of {number} is {result}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
