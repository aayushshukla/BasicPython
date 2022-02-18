#split(element) return a list
# it brake string on basis of given element if  element not exists it will return  original string
#by default it splits on basis of space
email='aayush@gmail.com'
data=email.split('@')
print(data)
print('usename is',data[0])
print('domain name is',data[1])
