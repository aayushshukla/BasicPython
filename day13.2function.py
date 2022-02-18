def withdraw(amt,wamt):
    if wamt<=amt and wamt%100==0 and wamt>=100:
        amt=amt-wamt
        print('withdraw amount is',wamt)
        print('balance amount is',amt)
    else:
        print('invalid amount or insufficient funds')

def options():
    print('enter 1 to withdraw')
    print('enter 2 to deposite')
    print('enter 3 to balance')
    print('enter 4 to exit')

def operations(ch):
    if ch==1:
         amt=int(input('enter amount'))
         wamt=int(input('enter withdraw amount'))
         withdraw(amt,wamt)
    elif ch==2:
        pass
    elif ch==3:
        pass
    elif ch==4:
        exit(0)
    else:
        print('invalid choice')
    
def validate(pin,upin):
    if pin==upin:
        options()
        choice=int(input('enter your choice'))
        operations(choice)
    else:
        print('invalid pin')
       
pin=1234
upin=int(input('enter pin'))
validate(pin,upin)

