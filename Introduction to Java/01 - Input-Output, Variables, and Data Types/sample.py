'''
    File name: sample.py
    Author: Jason Guo
    Date created: 5/1/2018
    Date last modified: 5/1/2018
    Python Version: 3.x

    This file gives Python code example for input and output,
    variables, and data types
'''

# Asks the user for their name, and prints it
print("Hello " + input("What is your name? "))

# Stores the user's age as a variable
age = input("What is your age? ")

# Prints the user's age in 5 years
print("Your age in 5 years will be " + str(int(age) + 5))

# This variable stores 6 digits of pi as a float
pi = 3.14159

# Prints pi as a float
print("The float version of pi is: " + str(pi))

# Prints pi as an int
print("The integer version of pi is: " + str(int(pi)))

# Creates and prints a boolean with a "True" value
condition = bool(1) # '1' and '0' can also be used to represent True and False, respectively
print(condition)

