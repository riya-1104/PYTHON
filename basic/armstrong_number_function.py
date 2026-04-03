# Check Armstrong number using function (string-based approach)

def is_armstrong(n):
    digits = len(n)
    total = 0

    for ch in n:
        total += int(ch) ** digits

    return total == int(n)

n = input()

if is_armstrong(n):
    print("Armstrong")
else:
    print("Not Armstrong")
