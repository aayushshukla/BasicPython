#String - immutable it can not be changed or modified and whenever perform any operation it
# will create new object
#indexed
s="Hello"
print('address of s',id(s))
sl=s.lower()
print('address of lower s',id(sl))
print("string in lower case",sl)
# convert string into upper case
su=s.upper()
print('string in upper case',su)
s1='Good eveNing'
sw=s1.swapcase() # it will swap case convert upper into lower case and lower into uppercase
print('String after swap case',sw)
fullname=input('enter full name')
standard=fullname.title() # return a string into standard case
print('Standard case',standard)
cap =fullname.capitalize() # return a string in which one character will be in upper case
print('Captialized string is',cap)

