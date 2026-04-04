#wap to find tuple with maximum product
l=[(1,2),(3,4),(5,6)]
nl=max(l,key=lambda x:x[0]*x[1])
print(nl)
