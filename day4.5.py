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
        if wamt<=amt and wamt%100==0 and wamt>=100:
            amt=amt-wamt   # amt -=wamt
            print('withdraw amount =',wamt)
            print('balance amount =',amt)
        else:
            print('Amount should be greater or equal to or multiple of 100 rs or insufficient fund')
    elif ch==2:
      pass  
    elif ch==3:
        print('Balance amount =',amt)
    else:
        print('Invalid option selected')
else:
    print('Invalid pin')
