from sklearn.datasets import load_iris
d=load_iris()
#print(d)
#print(d.keys())
flowerdata=d['data']
print(flowerdata)
print(sum(flowerdata))

