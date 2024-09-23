def factorial(n):
    fact = 1
    if n==0 or n==1: return 1
    for i in range (2,n+1):
        fact = fact * i
    return fact

def nCr(n,r):
    num = factorial(n)
    den = factorial(n-r)*factorial(r)
    return num/den

n = int(input("enter a number : "))
r = int(input("enter a number : "))

ans = int(nCr(n,r))
print(ans)
