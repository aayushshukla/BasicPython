#paired   - key : value , key is  unique , keys and values can have one to one  , one to many mapping
# keys are immutable
# non indexed
# ordered  - before python  3.6  dictionary are unordered  , order dictionary were used to make it ordered
# after 3.6 they are ordered

# creation of dictionary
d={ }  # empty dictionary
d1=dict()
print(f'type of d {type(d)} \n  type of d1 {type(d1)}')

dmenu={'dosa':100,'mishal pav':50,'achari momo':80,'vada pav':20}
print('menu is ',dmenu)

#  get value from dictionary
# i) dictionaryname[keyname] it will return value for given key , if key not exist it will raise key error

dname=input('enter dish name')
price=dmenu[dname]
print('Price of ',dname,' =',price)

# ii) get(keyname)  it will return value for given key, if key not found it will return None
dname=input('enter dish name')
if (dmenu.get(dname)!=None):
    price=dmenu.get(dname)
    print('Price of ',dname,' =',price)
else:
    print('Dish requested is not available')

#update dictionary dictionary[key]=value
# if key already exist it will update new value for given key
# if key not exists it will add new key value pair at the end of dictionary
dname=input('enter dish name')
price=int(input('enter price of dish'))
dmenu[dname]=price
print('menu after update',dmenu)

    




