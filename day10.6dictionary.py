# dictionary having multi value
d={'c1':[100,200,300],'c2':[400,500,600],'c3':[400,500,600]}
# dictionary as value , nested dictionary
d1={'c1':{2019:200,2020:400,2021:500}, 'c2': {2019:400,2020:500,2021:600} }
print(d1['c1'])
print(d1['c1'][2020]) # accessing dictionary['key']['innerkey']
print(d['c1'][2])
