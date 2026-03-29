#Write a program to count total number of upper case and lower case letters in it.
s="My nAme iS RIYA"
lower=upper=0
for ch in s:
    if ch.islower():
        lower+=1
    elif ch.isupper():
        upper+=1
print(f"{lower=}")
print(f"{upper=}")
