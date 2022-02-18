l1=[10,20,30,40,10,10,20,10]
count=0
position=[ ]
e=int(input('enter element to search'))
for index in range(0,len(l1)):
    if l1[index]==e:
        count=count+1
        position.append(index)

if count!=0:
    print('element found')
    print('Number of occurance of element',count)
    print('Position of element',position)
else:
    print('element not found')
