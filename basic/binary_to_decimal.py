# Write a function to convert a number from binary to decimal
def conversion(n):
    add=0
    rev=n[::-1]
    for i in range(len(rev)):
        add+=(2**i)*int(rev[i])
    return add
n=input()
print(conversion(n))
