def sum_of_digits(number):
    number = abs(number)
    str_num = str(number)
    total_sum = sum(int(digit) for digit in str_num)
    return total_sum

try:
    number = int(input("Enter a number: "))
    result = sum_of_digits(number)
    print(f"The sum of the digits of {number} is {result}")
