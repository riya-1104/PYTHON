# Replicate elements based on their value

lst = [2, 3, 4]
result = []

for num in lst:
    for _ in range(num):
        result.append(num)

print(result)
