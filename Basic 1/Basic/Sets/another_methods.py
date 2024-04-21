set1 = {1, 2, 3, 4, 5}
set2 = {3, 4}
set3 = set1.copy()
# Check if set2 is a subset of set1
print(set2.issubset(set1))

# Check if set1 is a superset of set2
print(set1.issuperset(set2))  

# printing copy set
print(set3)

# Modifying set2 doesn't affect set1
set3.add(6)
print(set1) 

# Length of set
print(len(set1))

# maximum and minimum values
print(max(set1))  
print(min(set1))  


# Disjoint: isdisjoint() :

# The isdisjoint() method checks whether two sets have any elements in common.
# Returns True if the sets have no elements in common, otherwise returns False.

set4 = {1, 2, 3}
set5 = {4, 5, 6}

# Check if set1 and set2 are disjoint (no common elements)
print(set4.isdisjoint(set5))  
