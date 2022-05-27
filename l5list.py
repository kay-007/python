# A List is a cellection which is ordered and changeable . Allows duplicate members.

# Create List

fruits = ['apple', 'orange']

print(fruits)
print(type(fruits))

#  Use a constructor

cars = list(['ford', 'toyota'])

print(cars)
print(type(cars))

#  In List, the index start with [0], [1], ect.

# Access Items
print(cars[0])

# Get Length
print(len(cars))

# Append to list (add)
cars.append('tesla')
print(cars)

# Remove from list
cars.remove('toyota')
print(cars)

# insert() method inserts an item at the specified index
cars.insert(0, 'bmw')
print(cars)

# Change value
cars[0] = 'BMW'
print(cars)

# Remove the specified index with pop
cars.pop(0)
print(cars)

# Reverse List
cars.reverse()
print(cars)

# Sort List
cars.sort()
print(cars)

# Reverse sort
cars.sort(reverse=True)
print(cars)