# Assign String to a Variable 
x = 'hello world!'
print(x)

# How to assign multiline string?
p = '''How to assign multiline string?
How to assign multiline string'''

print(p)

# How to get the length of the string?
print(len(p))

# In python, string are array.
print(p[0])
print(p[-1])

# Check if 'your word' in string
print('string' in p)   #True
print('strings' in p)  #False

# Check if not 'your word' in string
print('are' not in p)  #True
print('string' not in p)

# String formatting!
name = 'Kyaw Htet'
age = 20

# concatenate
print('My name is '+ name + ' and I am '+ str(age) + ' years old.')
# assign by arguments
print('My name is {name} and I am {age} years old.'.format(name=name, age=age))
# f string
print(f'My name is {name} and I am {age} years old.')