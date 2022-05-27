# A dictionary is a collection which is ordered*, changleable. 
# No duplicate members.

# Create dictionary

car = {
    'name' : 'bmw',
    'price' : '$30000',
    'model' : 2020
}

print(car)
print(type(car))

# Use constructor

fruits = dict(name = 'apple', price = '$3')
print(fruits)
print(type(fruits))

# How many item in dictionary using len() function:

print(len(car))

# Get item with key

print(fruits['name'])
print(fruits.get('price'))

# Add key/value

fruits['name_2'] = 'orange'
fruits['price_2'] = '$2'

print(fruits)

# Get keys

print(fruits.keys())

# Get values

print(fruits.values())

# Copy dict

another_car = car.copy()
print(another_car)

# Remove the item with the specified key name suing del keyword

del another_car['name']
print(another_car)

# Clear

another_car.clear()
print(another_car)
print(type(another_car))

# Delete the dict

del another_car
print(another_car)


