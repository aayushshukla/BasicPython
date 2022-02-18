s=input('enter string ')
print('string is',s)
e=input('enter element to search')
#count(element) return number of occurance of given element,if element not exists it will return 0
print('number of occurance of',e,'=',s.count(e))
#find(element) return position of first occurance of element if found , it not found it will  -1
print('first occurance using find method',e ,'=',s.find(e))
#rfind(element) return position of last occurance of element if found , it not found it will return -1
print('last occurance of using find',e ,'=',s.rfind(e))
#index(element) return position of first occurance of element if found , it not found it will raise error
print('first occurance of',e ,'=',s.index(e))
#rindex(element) return position of last occurance of element if found , it not found it will raise error
print('last occurance of',e ,'=',s.rindex(e))


