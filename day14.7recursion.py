fact=1
def factorial(n):
    global fact
    #fact=1
    if n>=1:
        fact=fact * n
        n=n-1
        factorial(n)
factorial(5)
print(fact)
        
