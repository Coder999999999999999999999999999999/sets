#How to create a set
#Converting the lists into sets

sample_list=[1,2,3,4,5]

sample_set = set(sample_list)

print(sample_set)
setA=set([1,2,3,4,5])
print(setA)

setB=set([3,9,5,1,0])
print(setB)

#Adding items to empty set
setC=set([])
setC.add(4)
setC.add(10)
setC.add(12)
print(setC)

#Remove an item from a set
setC.remove(10)
print(setC)

#Checking if any item is in set
if 10 in setC:
    print("10 is in set")
else:
    print("10 is not in set")

#Sets dont have index numbers
#print(setC[0]) this will give an error sets dont have potition numbers

#Set operations

#1.Union
#2.Intersection
#3.Difference
#4.Symetric diffrence

print(setA.union(setB))

print(setA|setB)

print(setA.intersection(setB))
print(setA&setB)