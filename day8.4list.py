l=[10,20,30,10,40,50,20,10]
e=int(input('enter element to search'))
#index(element) it will return first occurance index of given element
# if element not found it will raise error
print('list is \t',l)
#count(e) it will return number of occurance of given element .
# if element not found it will return 0
occurance=l.count(e)
print(f'number of occurance of {e} ={occurance}')
pos=l.index(e)
print('first occurance of ',e ,' =',pos)

