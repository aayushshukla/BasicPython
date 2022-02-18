# decimal  0-9
# octal  0-7 - 0o
# hexadecimal 0-15  , 10 - a , 11 -b , 12 -c ,13-d ,14-e, 15-f - 0x
# binary 0,1 - 0b
# int() ,float(),oct(),bin(),hex() string must be numeric
n=int(input('enter number'))
octal=oct(n)
hexadecimal=hex(n)
binary=bin(n)
print(f' octal representation of {n} = {octal}')
print(f' hexadecimal representation of {n} = {hexadecimal}')
print(f' binary representation of {n} = {binary}')
