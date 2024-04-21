# An iterator is an object that implements two methods: __iter__() and __next__(). 
# The __iter__() method returns the iterator object itself, and the __next__() method 
# returns the next element from the sequence. When there are no more elements, 
# it raises the StopIteration exception.

my_list = [1, 2, 3, 4, 5]

# Create an iterator object
my_iterator = iter(my_list)

while True:
    try:
        # Get the next element
        element = next(my_iterator)
        print(element)
    except StopIteration:
        # Stop when there are no more elements
        break



# Custom Class Iterator

my_list1 = [1, 2, 3, 4, 5]

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            element = self.data[self.index]
            self.index += 1
            return element
        else:
            raise StopIteration

# Create an iterator object from custom class
my_iterator = MyIterator(my_list1)

# Loop through the iterator
for element in my_iterator:
    print(element)
