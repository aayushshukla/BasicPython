#remove(element) it will remove first  occurance of given element from the list
# element not found it will raise error.It returns None
# clear() will remove all element of list 
l=[10,20,30,10,20,10,10,20,40,50]
e=int(input('enter element to remove'))
print('list before removal \t',l)
l.remove(e)
print('list after removal \t',l)

# reverse() reverse list
l.reverse()
print('list after reversal \t',l)

#copy() copy one list into another new list
clist= l.copy()
print('original list \t',l)
print('copied list \t',clist)
print('address of copied list ',id(clist))
print('address of original list',id(l))

