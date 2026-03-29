#Write a program that prints the numbers from 1 to N (where N is a positive integer)
#For multiples of 3, print "Fizz" instead of the number.
#For multiples of 5, print "Buzz" instead of the number.
#For multiples of both 3 and 5, print "FizzBuzz".
#Otherwise, print the number itself.
n=int(input("enter the number="))
for i in range(1,n):
    if (i%3==0 and i%5==0): print("FizzBuzz")
    elif i%3==0: print("Fizz")
    elif i%5==0:print("Buzz")
    else:print(i)
        
