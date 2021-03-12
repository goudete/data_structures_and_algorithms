"""
Sets
    Unordered collection of elements

Properties
    Each element in a set is UNIQUE
    Each element in a set is IMMUTABLE

Pros
    Checking membership is constant time
    Adding elements is constant time
    Removing elements is constant time

"""

#Create set from list
set_example = set([1,2,3,4])
print('create set:', set_example)


# Adding elements to set (add and update)

#add an element
set_example.add(5)
print('add to set:', set_example)

#add multiple elements
set_example.update([6,7,8])
print('add multiple to set:', set_example)


#Removing elements from set (discard, remove, pop)

# discard element (does nothing if key not present)
set_example.discard(1)
print('discard from set:', set_example)

set_example.discard(10)
print('discard from set:', set_example)

# remove element (raises key error if key not present)
set_example.remove(8)
print('remove from set:', set_example)

# pop removes arbitrary element, bc items are not ordered
print(set_example.pop())
print('pop from set:', set_example)
