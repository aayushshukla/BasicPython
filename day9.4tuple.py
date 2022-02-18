t=([10,20,30],50,60) # tuple is immutable but its elements may be mutable 
tl=t[0]
print(tl)
tl[1]=100
print(t)
