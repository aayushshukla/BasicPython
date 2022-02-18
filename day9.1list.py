l1=[1,2,3,4]
l2=[10,20,30,40]
l3=[]
for i in range(0,len(l1)):
    for j in range(0,l1[i]):
        l3.append(l2[i])

print(l3)
    
