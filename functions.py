#https://repl.it/@devpeterkim/ReasonableChocolateVendors
import turtle

turtle = turtle.Turtle()
  
#Functions
def square(Length,Length2):
  turtle.forward(Length)
  turtle.left(Length2)
  turtle.forward(Length)
  turtle.left(Length2)
  turtle.forward(Length)
  turtle.left(Length2)
  turtle.forward(Length)
  turtle.left(Length2)

#declare arguments
square(300,90)

"""
turtle.forward(90)
square()


turtle.forward(90)
square()


turtle.forward(90)
square()
"""
#if statement
is_john_killer = True
is_bob_killer = False

if is_john_killer == True:
  print("john is the killer")
  square(300,90)
 
#while loop
i = 0
while i < 50:
  print(i)
  i = i + 1
  
  
 #Countdown loop
  i = 100
while i >= 0:
 if i > 0:
  print (i)
 if i == 0:
   print("Boom")
  i = i - 1
