print('enter PAN for pan card')
print('enter ADHAAR for adhaar card')
idtype=input('enter your id type')
if idtype=='PAN' or idtype=='pan' or idtype=='ADHAAR' or idtype=='adhaar':
    idno=input('enter id no')
    print(f'{idtype} no = {idno}')
else:
    print('Invalid id type ')
