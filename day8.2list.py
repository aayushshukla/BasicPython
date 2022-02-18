#pop() it will remove last element of list .it return that element also.
# if list is empty it will raise error
l=['hulk','thor','ironman','flash']
print('original list is',l)
v=l.pop()
print(f' element removed {v} and list after pop is {l}')

for  i in range(0,len(l)):
    print(l.pop())

print(l)
