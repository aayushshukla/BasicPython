#function with argument
# in python there is no function without return type. if a function have no return type it will return None 
def  add(n1,n2):
    print(n1,'+',n2,'=',n1+n2)
    #n1=n1+10
    #print(n1)
    return None 

x=int(input('enter number 1'))
y=int(input('enter number 2'))
z=add(x,y)  # call by value
print(z)


