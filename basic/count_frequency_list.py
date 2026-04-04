#wap to count the occurrence of each element in a list
list1=[4,2,3,1,2,3,4,5,1,1,2,3,6,7,2,3]
freq={}
for num in list1:
    freq[num]=freq.get(num,0)+1
print(freq)
