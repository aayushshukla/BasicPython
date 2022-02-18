#insert(position,value) it add new object at given index
l=[10,20,30,40]
index=int(input('enter index to add new value'))
value=int(input('enter value at given index'))
print('list before insertion',l)
l.insert(index,value)
print('list after insertion',l)
