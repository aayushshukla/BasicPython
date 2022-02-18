n1=int(input('enter number 1'))
n2=int(input('enter number 2'))

print('enter 1 to add numbers')
print('enter 2 to sub numbers')
print('enter 3 to multiple')
print('enter 4 to div')
print('ente 5 to fdiv')
ch=int(input('enter your operation'))

if ch==1:
    print(n1,'+',n2,'=',(n1+n2))
elif ch==2:
    print(n1,'-',n2,'=',(n1-n2))
elif ch==3:
    print(n1,'*',n2,'=',(n1*n2))
elif ch==4:
    if n2!=0:
        print(n1,'/',n2,'=',(n1/n2))
    else:
        print('cant divide by zero')
elif ch==5:
    if n2!=0:
        print(n1,'//',n2,'=',(n1//n2))
    else:
        print('cant divide by zero')
else:
    print('Invalid operation selected')
    
