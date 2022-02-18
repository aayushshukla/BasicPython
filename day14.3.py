#arbitary keywords arguments  **variablename
# arbitary value argument followed by  arbitary keyword arguments
def printData(*v,**kw):
    print(kw)
    print('--------')
    print(v)
    print('********************')

printData(100,200,400,x=10,y=20)
printData(20,30,40,a=200,b=500,c=600)
printData(l='chitu',m='pintu',n='tinku')
