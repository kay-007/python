# Sets are used to store multiple items in a single variable.
# Set items are unordered, unchangeable, and do not allow duplicate values.
# Set object is not subscriptable.

# Create Set

fruits = {'apple','orange'}
print(fruits)
print(type(fruits))

# Using Constructor

country = set({'us','uk'})
print(country)
print(type(country))

# How many items in set use len() function:

print(len(country))

# Access through loop

for fruit in fruits:
    print(fruit)

# Add an item to a set, using the add() method:

country.add('mm')
print(country)

# Merging two sets using update() method:

another_fruits = {'strawberry','cherry'}

fruits.update(another_fruits)
print(fruits)

# Remove Item from set using remove() method:

fruits.remove('strawberry')
print(fruits)

# Remove Item from set using discard() method:

fruits.discard('strawberry')
print(fruits)

# Clear all item from set.

fruits.clear()
print(fruits)

# Delete Set

del fruits
print(fruits)