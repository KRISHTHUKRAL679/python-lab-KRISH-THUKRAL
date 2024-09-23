n = int(input("enter a number : "))

sum = 0
temp = n
while(temp!=0):
    sum = sum + temp%10
    temp //= 10

if(n%sum==0): print(n,"is a harshad number")
else: print(n,"is not a harshad number")
