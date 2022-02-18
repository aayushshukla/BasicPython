x=65
for  i in range(4):
    for j in range(4):
        if i>=j:
            print(chr(x),end=' ')
    x=x+1
    print()
