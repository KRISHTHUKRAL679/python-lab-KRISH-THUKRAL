def is_armstrong_number(number):
    str_num = str(number)
    num_digits = len(str_num)
    sum_of_powers = sum(int(digit) ** num_digits for digit in str_num)
   
    return sum_of_powers == number

print("Armstrong Numbers from 1 to 1000:")
for num in range(1, 1001):
    if is_armstrong_number(num):
        print(num)
