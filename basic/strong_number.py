"""Write a Python function check_strong_number(num) that accepts a positive integer
as argument and returns True if the number is strong number else false. Invoke the
function and based on return value print the number is strong number or not.
A number is said to be strong number, if the sum of factorial of each digit
of the number is equal to the given number."""

def check_strong_number(num):
    total=0
    for i in str(num):
        fact=1
        for j in range(1,int(i)+1):
            fact*=j
        total+=fact
    return total==num
n = int(input())
print(check_strong_number(n))
            
