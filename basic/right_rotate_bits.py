"""Write a Python function right_shift(num, n) that takes two numbers num and n as  arguments and returns value of the integer num rotated to the right by n positions. Assume both the numbers are unsigned.
Invoke the function and print the return value."""

def right_shift(num,n):
    bits=len(bin(num))-2 #to calculate the number of bits in binary of num
    
    for i in range(n):
        last_bit=num&1 #this will calculate the last bit of bin(num)
        num=num>>1
        num=num| (last_bit<<(bits-1))
    return num
num = int(input())
n = int(input())

print(right_shift(num, n))
