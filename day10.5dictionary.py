l=['c1','c2','c3','c4']
d={ }
#fromkeys(iterator, value) it will create a dictionary havings keys as iterator value and default value
#if no default value is given it will assign None
# it always create a new dictionary object
print(id(d))
d=d.fromkeys(l,30)
print(id(d))

print(d)
