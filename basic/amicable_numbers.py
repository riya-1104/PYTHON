# Check Amicable Numbers

def divisor_sum(n):
    total = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            total += i
    return total

def check_amicable_numbers(num1, num2):
    return divisor_sum(num1) == num2 and divisor_sum(num2) == num1

num1 = int(input())
num2 = int(input())

if check_amicable_numbers(num1, num2):
    print("Amicable Numbers")
else:
    print("Not Amicable Numbers")

def divisor_sum(n):
    total = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            total += i
    return total

def check_amicable_numbers(num1, num2):
    return divisor_sum(num1) == num2 and divisor_sum(num2) == num1

num1 = int(input())
num2 = int(input())

if check_amicable_numbers(num1, num2):
    print("Amicable Numbers")
else:
    print("Not Amicable Numbers")
