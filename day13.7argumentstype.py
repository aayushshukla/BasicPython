#  positional arguments
#  named / keyword arguments
#  default arguments
#  arbitary value arguments    #  arbitary keyword arguments

#positional arguments
def  fn(x,y):
    print(x, '  ',y)

fn(10,20)


#keyword arguments or named arguments - it works with function calling
# position arguments followed by keyword arguments
def  fn (l,m,n):
    print('value of l',l )
    print('value of m',m)
    print('value of n',n)

fn(30, n=50,m=100)

#default arguments we can give a default value to a arguments , it is mention during declaration of function
# that default value is used when no value is given to that argument
# default arguments will be last arguments of function
# non default arguments will be written first ,
# nondefault arguments follows by default argument
def fn(name='john doe' ,age=18):
    print('user name is',name)
    print('user age is',age)

fn('pintu')
fn('chintu',20)
fn(age=30)

print('>>>>>>>>>second variation<<<<<<<<')
def fn(age,name='john doe' ):
    print('user name is',name)
    print('user age is',age)


fn(name='chintu',age=20)
fn(age=30)

