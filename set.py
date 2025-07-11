# set - collection of the unordered items
# each element in the set must be unique & immutable

collection = {1,2,3,3,4,"hello", "world"}

print(collection)
print(len(collection))
print(type(collection))

# empty set
coll = set()
print(type(coll)) 

# set Methods

collection.add(8)
print(collection)
collection.remove(8)
print(collection)

# remove random  value
print(collection.pop())
print(collection)
print(collection.pop())
print(collection)

print(collection.clear())

print(len(collection))

# union intersection method

set1 = {1,2,3}
set2 = {2,3,4}
print(set1)
print(set2)
print(set1.union(set2))
print(set1.intersection(set2))

values = {9,9.0,8,8.0}
print(values)

values1 = {"9",9.0,8,"8.0"}
print(values1)

values2 = {
    ("float",9.0),
    ("int", 9)
}

print(values2)
