d={'c1':1000,'c2':300,'c3':500}
t=sum(d.values())
print(t)

s=0

for  v in d.values():
    s=s+v
print('sum is',s)
