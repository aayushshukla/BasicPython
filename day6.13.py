n=int(input('enter number of rows'))
m=int(input('enter number of columns'))
for  i  in range(1,n):
    for j in range(1,m):
        if i>=j:
            print(i,end='  ')
    print()
