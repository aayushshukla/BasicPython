s1=input('enter string').strip()
if s1.isalpha()==True:
    print('string is alphabetic')
elif s1.isnumeric()==True:
    print('string is numeric')
elif s1.isalnum()==True:
    print('string is alpha numeric')

else:
    print('string',s1)
    
