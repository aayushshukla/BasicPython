# wap to calculate total bill
#  take user input noi , poi  ,gst ,
noi=int(input('enter number of items'))
poi=float(input('enter price of item'))
gst=float(input("enter gst % "))
totalbill=(noi*poi) +((noi*poi)*gst/100)
print(f'no of item \t = {noi} \n price \t={poi} ')
print(f'gst \t={gst} \n totalbill = {totalbill} \\')

