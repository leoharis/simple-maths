"""
Simple Maths v3
Author: Leo Haris
"""
import random

x = 5
y = 2
z = 7

# Ask user for a number
print("Enter a number: ")
user_input = int(input())

# calculate total using a random integer
total = (random.randint(1, 10) + y) * z

# Is total greater than user input?
if user_input > total:
    print("Yes user input is greater than total")
else:
    print("No user input is less than total")

print("Total is " + str(total) + ", and user input was " + str(user_input))
