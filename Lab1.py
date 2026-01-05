# Function 1: Write a simple Hello World program
# This function should print "Hello, World!" to the screen.
def hello_world():
   print('Hello, World! ')

# hello_world()

# Function 2: Get input and output with different variable types
# This function should prompt the user for their name (string), age (int), and height (float),
# and then print them back in a formatted message.
def input_output():   

   name = input('Please enter your first name: ')
   age = int(input('Please enter your age: '))
   height = float(input('Please enter your height in meters: '))

   print('Hello, ' + name + '!')
   print('You are ' + str(age) + ' years old. ')
   print('Your height is ' + str(height) + ' meters. ')

# input_output()
