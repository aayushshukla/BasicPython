def table(m,i=1):
    if i<=10:
        print(f'{m} * {i} ={m*i}')
        #i=i+1
        table(m,i+1)
n=int(input('enter number'))
table(n)
        
