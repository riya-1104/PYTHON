#Write a function that takes two strings and return a string containing only the common
#characters in both strings.
def remove(s1,s2):
    print(set(s1)&set(s2))
s1="riya"
s2="tiya"
remove(s1,s2)
