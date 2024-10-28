#maths functionality
import math
from pdb import post_mortem

x= 99

square_root = math.sqrt(x)
print('Root is',square_root)

rounded = round(square_root,2)
print('Rounded to two decimal places',rounded)

#functions (arguments)
print(rounded)

#call a function
y = round(8.343636,3)
print(y)

x = 2
y = 3
print(math.pow(x, y))

print('--------------------------')
name = 'Francis'
print(len(name))
print(name.lower())
print(name.upper())
print(name.title())
print(name.capitalize())

post = 'This thing is so easy and fluent'
new_post = post.replace('fluent', 'flowing')
print(new_post)

#if statements
#lists
#loops
