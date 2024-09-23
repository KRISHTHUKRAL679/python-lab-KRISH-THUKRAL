def is_harshad_number(number):
    str_num = str(number)
    
    sum_of_digits = sum(int(digit) for digit in str_num)

    return number % sum_of_digits == 0

number = int(input("Enter a number to check: "))
if is_harshad_number(number):
    print(f"{number} is a Harshad Number.")
else:
    print(f"{number} is not a Harshad Number.")
