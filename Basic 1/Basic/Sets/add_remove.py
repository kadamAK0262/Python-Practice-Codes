# Sets
fruits = {'apple', 'banana', 'orange'}

# Another process of Creating a set using the set() constructor
colors = set(['red', 'green', 'blue'])

print(fruits) 
print(colors) 

# Adding elements to a set
fruits.add('grape')
fruits.update(['kiwi', 'pineapple'])
print(fruits) 

# Removing elements from a set
fruits.remove('banana')
fruits.discard('kiwi')

print(fruits) 
