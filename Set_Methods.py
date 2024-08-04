"""

collection = set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(10)
collection.add("Tohid")
collection.add((1,2,3,4,5,6))

collection.remove(10)


print(collection)

"""
"""
collection = set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(10)
collection.add("Tohid")
collection.add((1,2,3,4,5,6))

collection.clear()

print(len(collection))
"""
"""
collection = {"hello", "college","world","code","java","C++"}

print(collection.pop())
print(collection.pop())
print(collection.pop())
"""
 
"""
set1 = {1,2,3}
set2 = {2,3,4}

print(set1.union(set2)) #[1,2,3,4]
print(set1)
print(set2)
"""

set1 = {1,2,3,4,5,6}
set2 = {2,4,5,8,9,7}

print(set1.intersection(set2))