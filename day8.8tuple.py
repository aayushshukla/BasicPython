#tuple - immutable - it can not be changed or modified
#fixed size
# heterogenous , ordered , unsorted
# indexed

#create tuple
t=()
print('type of t',type(t))

t=(10,20,30,10,50,10)
#get element from a tuple  tuplename[index] it will return value at given index

index=int(input('enter index to get value'))
v=t[index]
print('value at ',index,'=',v)

# 'tuple' object does not support item assignment
'''nv=int(input('enter new value'))
t[index]=nv
print(t)'''
#count(e) return number of occurance of given element, return 0 if element not found
#index(e) return first occurance of given element  if element exist otherwise raise error
v=int(input('enter new value'))
print('number of occurance of ',v,' =',t.count(v))
print('first occurance of ',v ,' =', t.index(v))

# tuple() to convert a list or string or other sequence object in to tuple
t1=tuple()
print('empty tuple',t1)
l1=['prasad','ankit','amit','arun']
tname=tuple(l1)
print('list converted to tuple',tname)

