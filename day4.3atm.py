pin=1234
amt=10000
upin=int(input('enter pin'))
if pin==upin:
    print('enter 1 to withdraw')
    print('enter 2 to deposite')
    print('enter 3 to check balance')
    ch=int(input('enter your operation'))
    if ch==1:
        wamt = int(input('enter amount to withdraw'))
        if wamt<=amt:
            if wamt%100==0:
                if wamt>=100:
                    amt=amt-wamt   # amt -=wamt
                    print('withdraw amount =',wamt)
                    print('balance amount =',amt)
                else:
                    print('Amount should be greater or equal to 100 rs')
            else:
                print('Amount should be multiple of 100 , 200 or 500')
        else:
            print('Insufficient funds')
    elif ch==2:
      pass  
    elif ch==3:
        print('Balance amount =',amt)
    else:
        print('Invalid option selected')
else:
    print('Invalid pin')
