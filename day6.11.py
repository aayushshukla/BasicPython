n=int(input('enter number of rows'))
m=int(input('enter number of columns'))
for  i  in range(n):
    for j in range(m):
        if i>=j:
            print('*',end='  ')
    print()
