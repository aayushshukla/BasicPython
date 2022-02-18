# arbitary value argument / variable arguments  , *variablename
def  printData(k,*v):
    print('value of k =',k)
    print(v)
    for  values in  v:
        print(values)
    print('--------------------------')

printData(10,20)
printData(100,200,300,400)
printData('chintu')
printData(1,2,3,4,5,6,7,'pintu','rahul')
