d_stock={'mindtree':4000,'pnb':40,'hcl':1011}
d_stock2={'wipro':561,'ioc':121}
# merge  two dictionary  we use update()
print('Stock list before update',d_stock)
d_stock.update(d_stock2)
print('Stock list after update',d_stock)

#pop(key) it will remove given key and return its value , if key not exists it will raise error
stockname = input('enter stock to sale')
price =d_stock.pop(stockname)
print(stockname , ' saled for rs =',price)
print('New stock list after sale',d_stock)

#popitem() it will remove last element of dictionary .It will return key  value pair  in tuple
item =d_stock.popitem()
print('stock removed',item)
print('new list after reoved',d_stock)

# copy() to copy a dictionary
dcopy=d_stock.copy()
print('copied dictionary',dcopy)
print('original dictionary',d_stock)
#clear() it will remove all elements of given dictionary
dcopy.clear()
print('copied dictionary after clear',dcopy)

#wap to find sum of values of dictionary
