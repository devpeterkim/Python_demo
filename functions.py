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
  
  
 #While Loop Countdown loop
  i = 100
while i >= 0:
 if i > 0:
  print (i)
 if i == 0:
   print("Boom")
  i = i - 1
  
 #While loop + Else Countdown loop  
  i = 100
while i >= 0:
  if i > 0:
   print (i)
  else:
   print("Boom")
  i = i - 1
  
  
  
  #Created Loop Function
def loop():
  i = 100
  while i >= 0:
    if i > 0:
      print (i)
    else:
     print("Boom")
    i = i - 1

def Print_Out_Hello():
  print ("Hello Wednesday")
  
  
#Calling Hello Function 
Print_Out_Hello()

#Calling Loop Function
loop()



#For Loop Example 
for number in range(101):
  if number == 100:
    print("Boom!")
  else:
    print(number)

#For Loop Function	
def string_length(word)
	count = 0
	for letter in "Orange":
		count = count + 1
	return count

#indexing - help you do search through a blog post 
#-1 for last word 
#[2:4] for between word
print("Orange"[5])


#Say good morning
def Speak(name, name2):
  Talk = "Good Morning" + " " + name + " & " + name2 + "!!!!"
  return Talk

print Speak("Peter","Gavin")


#How many letters are in each name2
def Speak(name):
  count = 0
  for letter in (name):
      count = count + 1
  return count

print Speak("Peter")  

#Adding string numbers converting to integers
'1 2 5 '

numbers = [1,2,5]

count = 0

for number in numbers:
  count = count + int(number)
  
print(count)
  
