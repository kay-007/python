# A function is a block of code which only runs when it is called.
# You can pass data, known as paremeters, into a function.
# A function can return data as a result.

# Create function

def sayHi():
    print('hi')


# Call function

sayHi()

# Passing Arguments

def greeting(msg):
    print(msg)

greeting('Hello Everyone')

# Default Parameter
# More than one argument

def adding(num1 = 0, num2 = 0):
    print(num1 + num2)

adding(4)



# Arbitrary Arguments, *args

def getNames(*name):
    print(name[0], name[1])

getNames('Jhon', 'Leo')

# Send arguments with the key

def i_am(name, age):
    print(f'My name is {name} and I am {age} years old.')

i_am(age=20, name='Kyaw Htet')

# The pass Statement

def no_content():
    pass