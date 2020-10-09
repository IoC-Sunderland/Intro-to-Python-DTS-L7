"""
REPL:

Read
Evaluate
Print
Loop

"""

'''
CTRL-L to clear REPL
'''

# Variable decleration
num = 1

print(num)

# Get input from user
# name = input("Please enter your name: ")

# Type function to check var type
# print(type(name))
print(type(num))

# Functions
def name_of_function():
    return "Hi from name_of_function!"

print(name_of_function())

# Function arguments
def function_params(num1, num2):
    return num1 + num2 # Concatenation

print(function_params("He", "llo"))

# Arbitary number of positional args
def number_of_args(num1, *args):
    return num1, args

# Conditional statements
if 10 == 9:
    print('!')
elif 10 == 10:
    print('True')
else:
    print('False')

print('Hi!')

# While Loops

import time

'''
while True:
    print('Continous loop..')
    time.sleep(3)
'''

# For loops

toys = ['Lego', 'Scooter', 'Bouncy Ball']

for toy in toys:
    print(toy)
