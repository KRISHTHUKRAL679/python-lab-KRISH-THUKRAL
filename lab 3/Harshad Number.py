def is_harshad_number(number):
    # Convert the number to a string to easily iterate over its digits
    str_num = str(number)
    
    # Calculate the sum of the digits
    sum_of_digits = sum(int(digit) for digit in str_num)
    
    # Check if the number is divisible by the sum of its digits
    return number % sum_of_digits == 0

# Example usage:
number = int(input("Enter a number to check: "))
if is_harshad_number(number):
    print(f"{number} is a Harshad Number.")
else:
    print(f"{number} is not a Harshad Number.")
