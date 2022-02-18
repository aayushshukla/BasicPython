n=int(input('enter number'))
flag=0
if n>=2:
    for i in range(2,n):
        if n%i ==0:
            flag=1
            break
    if flag!=1:
        print('number is prime')
    else:
        print('number is not prime')
else:
    print('number should be greater or equal to 2')

# run a program  to take user input until user is going to press x 
     
