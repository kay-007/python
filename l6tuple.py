# A tuple is used to store collectons of data.

# Tuple items are ordered, unchangeable and allow duplicate values.

# Create tuple
laptop = ('apple','dell','msi')
print(laptop)
print(type(laptop))

# Using a constractor
juice = tuple(('apple','orange'))
print(juice)

# To know many items a tuple has use len() function.
print(len(juice))

# If you wnat to create a tuple with only one item, you need to add , in the end.
# Otherwise, python will not recognize as tuple
fruit = ('apple' ,)
print(type(fruit))


# Get value
print(fruit[0])


# Can't change value
# fruit[0] = 'orange'

# Delete tuple
del fruit
print(fruit)