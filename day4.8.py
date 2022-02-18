uname=input('enter user name')
password=int(input('enter password'))
cpassword=int(input('confirm password'))
if password==cpassword:
    print(f' welcome {uname} valid password')
else:
    print('password not match')
    cpassword=int(input('confirm password'))
    if password==cpassword:
        print(f' welcome {uname} valid password')
    else:
        print('password not match')
    
