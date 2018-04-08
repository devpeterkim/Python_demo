#Lists (Arrays - Java, C)

#LISTS + LEN + LOOP + APPEND  
#List are mutable, they can change

movies = ["intersteller", "Dark Night", "Xmen"]
print (movies)

#Len ex. You can see how many movies are in Netflix
#How many authors are on the website

for movie in movies:
  print(len(movie))
  
print("break")  

#add items to list  
movies.append("ToyStory")
movies.append("Cars")

print (movies)
print (len(movies))

#More examples 
fruits = ["apple","orange","pear","watermelon","oranges"]

count = 0
for prntln in fruits:
  print(prntln)
  
#Passing in collection to the loop.   
bank_numbers = [1, 2, 3, 4, 5, 100, 101, 102]

def count_numbers(numbers):
  count = 0
  for number in numbers:
      #count = number
     #print(number)
   count = count + number

  return count

print(count_numbers(bank_numbers))

#Setting List 

invoices = [1, 2, 3, 4, 5, 100, 101, 102]

def biggest(numbers):
  biggest_number = numbers[0]
  for number in numbers:
    if number > biggest_number:
      biggest_number = number
  return biggest_number

print(biggest(invoices))







