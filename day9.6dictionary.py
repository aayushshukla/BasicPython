d={2012:100,2017:390,2020:500,2022:700}
#key() returns all keys of dictionary
#values() returns all value of dictionary
#items() returns key , value pair dictionary in tuple
print('key of dictionary',d.keys())
for  key in d.keys():
    print('key =',key)
print('value of dictionary',d.values())
for  v in d.values():
    print('Value =',v)
print('items of dictionary',d.items())

for item in d.items():
    print('key =',item[0])
    print('value =',item[1])
