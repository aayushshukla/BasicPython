# dynamic size
#  heterogenous
#  index , duplicacy
# mutable - list object can changed or modified
# ordered ,unsorted
# creation of list
l1=[ ]
print('type of l1',type(l1))
l2=list()
print('type of l2',type(l2))

namelist=["amit",'leena','ankit','prasad','rahul','akash']

#get value from list   listname[index]
index=int(input('enter index'))
name=namelist[index]
print('name for given ',index, '=',name)

#update  value to a list  -- listname[index] = value  it will update value of given index if index found
# otherwise it will raise IndexError - index out of range
index=int(input('enter index to update'))
newname=input('enter new name to  replace')
print('Names before update : ',namelist)
namelist[index]=newname
print('Names after update : ',namelist)

for name in namelist:
    print('Name is ',name)

for index in range(0,len(namelist)):
    print('name on basis on =', index, '\t',namelist[index] )


