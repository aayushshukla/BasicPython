d={}
for i in range(2) :
    keys=input("Enter Keys")
    values=int(input("Enter Values"))
    d[keys]=values
print(d)
v=list(d.values())
print(type(v))
print(sum(v))
d={1:11,2:22,3:33,4:44,5:55}
print("Sum of all values is ",sum(d.values()))
