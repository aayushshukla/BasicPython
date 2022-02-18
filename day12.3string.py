s1="good evening class \n how are you ? \t hmmm"
print(s1)
np=0
for  ch in s1:
    if ch.isprintable()==True:
        pass
    else:
        np+=1
print('number of non printable character',np)
    
