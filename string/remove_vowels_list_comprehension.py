# Remove vowels using list comprehension

s = input()
result = "".join([ch for ch in s if ch.lower() not in "aeiou"])
print(result)
