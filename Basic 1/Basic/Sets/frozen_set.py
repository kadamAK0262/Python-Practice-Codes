frozen_set = frozenset([1, 2, 3, 4, 5])

# Accessing elements in a frozen set (iteration)
for num in frozen_set:
    print(num)

# Frozen sets are immutable, so you can't add or remove elements



# The main reason to use a frozen set in Python is immutability. 
# While regular sets (set objects) are mutable, meaning you can add or remove elements from 
# them after they are created, frozen sets (frozenset objects) are immutable, meaning once they are created, 
# their contents cannot be changed.

# Here are some reasons to use frozen sets:

# Hashability: Frozen sets are hashable, meaning they can be used as keys in dictionaries and 
# elements in other sets. This is because their contents cannot be modified after creation, 
# ensuring that their hash value remains constant.

# Security: Since frozen sets cannot be modified, they are often used to store constant sets of data 
# that should not be altered during program execution. This helps prevent accidental changes to 
# important data.

# Thread Safety: Immutable data structures like frozen sets are inherently thread-safe, 
# meaning they can be safely shared among multiple threads without the risk of data corruption due to 
# concurrent modification.

# Performance: Frozen sets can offer performance benefits in certain scenarios, 
# such as when storing small, constant sets of data. They are implemented using hash tables, 
# which provide fast access and membership testing operations.

# Now, let's discuss the differences between sets and frozen sets:

# Mutability: Sets (set objects) are mutable, meaning you can add or remove elements from them 
# after creation. Frozen sets (frozenset objects), on the other hand, are immutable and cannot be 
# modified after creation.

# Hashability: Sets are not hashable, while frozen sets are hashable. This means that sets cannot 
# be used as keys in dictionaries or elements in other sets, while frozen sets can.

# Usage: Sets are typically used when you need a mutable collection of unique elements that may 
# change over time. Frozen sets are used when you need an immutable collection of unique elements 
# that should not change after creation.

# In summary, while sets are more flexible and allow for dynamic changes to their contents, 
# frozen sets provide immutability and hashability, making them suitable for scenarios where constant, 
# unchanging sets of data are needed. Both sets and frozen sets have their own use cases and advantages, 
# and the choice between them depends on the specific requirements of your program.