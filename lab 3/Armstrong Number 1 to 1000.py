def is_armstrong_number(number):
    # Convert the number to a string to easily iterate over its digits
    str_num = str(number)
    # Determine the number of digits
    num_digits = len(str_num)
    # Compute the sum of each digit raised to the power of num_digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in str_num)
    # Check if the computed sum equals the original number
    return sum_of_powers == number

# Iterate over the range from 1 to 1000
print("Armstrong Numbers from 1 to 1000:")
for num in range(1, 1001):
    if is_armstrong_number(num):
        print(num)
