#  Using recursion find sum of digits of a given number.
def digitsSum(n):
    if n==0:return 0
    return n%10+digitsSum(n//10)
    
n=int(input("input a num:"))
print(digitsSum(n))
