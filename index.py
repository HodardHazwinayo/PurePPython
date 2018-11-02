# the first option to format strings.
age = 20

name = 'Hodard'

print('{0} was {1} was testing the python app'.format(name, age))

print('why is {0} playing with that python!'.format(name))

# Python 3.6 introduced a shorter way to do named parameters, called "f-strings"
age = 20

name = "Hodard"

print(f'{name} was {age} years old when he wrote this book')

print(f'why is {name} is playing with python!')

# decimal (.) with precision of 3 float '0.333'
print('{0: .3f}'.format(10 / 3))

# fill with underscores (_) with the text centered
#  (^)  to 11 width ' _hello_ '
print('{0:_^11}'.format('hello'))

# keyword-based 'Hodard wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Hodard', book='A Byte of Python'))

# simple mathematical operations

a = 2   # variable
a = a * 3   # mathematical operation
print(a)    # Return or Result

# Operators and Expressions

length = 20
breadth = 10

area = length * breadth

print('Area is', area)

print('Perimeter is', 2* (length + breadth))



