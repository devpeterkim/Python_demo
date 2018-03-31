# single line comment
""" Multi line comment
Line 1
Line 2
line 3
"""


haiku = """ 
The old pond,
A frog jumps in:
Plop!
"""
print haiku

float_1 = 0.25
float_2 = 40.0

product = float_1 * float_2
print float(product) 

age = 13
print "I am " + str(age) + " years old!"

number1 = "100"
number2 = "10"

string_addition = number1 + number2 
#string_addition now has a value of "10010"
print string_addition

print "hello Gavin"
int_addition = int(number1) + int(number2)
#int_addition has a value of 110
print int_addition

float_1 = 0.25
float_2 = 40.0

product = float_1 * float_2
print float(product) 

#Changing float to int
int_product = int(product)
print int_product

big_string = "The product was " + str(int_product)
print big_string

"""
Python Syntax Review

- Print statements
- How to create, modify, and use variables
- Arithmetic operations like addition, subtraction, division, and multiplication
- How to use comments to make your code easy to understand
- Different data types, including strings, ints, floats, and booleans
- Converting between data types

"""
skill_completed = "Python Syntax"
print skill_completed

exercises_completed = 13
print exercises_completed

#The amount of points for each exercise may change, because points don't exist yet
points_per_exercise = 5 
print points_per_exercise

"""
point_total = int(exercises_completed) * int(points_per_exercise)
print point_total

"""

point_total = 100
point_total = point_total + int(exercises_completed) * int(points_per_exercise)
print point_total

print "I got " + str(point_total) + " points!"
