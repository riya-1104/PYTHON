'''Write a program that accepts a string from user and returns it after removing vowels from
it.'''
str=input("enter a string:")
v="aeiouAEIOU"
s=""
for i in str:
    if i in v:
        continue
    s=s+i
print(s)
