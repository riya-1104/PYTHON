# Count occurrences of 2 until a tuple is encountered

lst = [1,2,2,3,2,1,2,3,(1,2),2,3]
count = 0

for item in lst:
    if isinstance(item, tuple):
        break
    if item == 2:
        count += 1

print(count)
