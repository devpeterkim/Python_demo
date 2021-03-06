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

#Let's filter movies with 7+

our_movies = [("Interstellar",10),("StarWars",6),("Apollo",8.5)]

def rating_filter(movies, max_rating):
  final_movies = []
  
  for movie in movies:
    if movie[1] >= max_rating:
        final_movies.append(movie[0])
        #print(final_movies)
  return final_movies

print(rating_filter(our_movies,5))


people_age = [("George",50),("Bob",6),("Lucy",8),("Mark",25),("John",18),("Tom",87)]

def age_filter(name, max_age):
  final_age = []
  
  for age in name:
    if age[1] >= max_age:
      final_age.append(age[0])
  return final_age
  
print(age_filter(people_age,20))

print(people_age)


#intro to dictionaries
#Dictionaries are also known as Maps or Hash

phone_book = {"John": "555-556-6988", "Billy": "115-556-1118"}

print(phone_book)
print(phone_book["John"])


movies = {"Cars3": 9.3, "Starwars": 8.5}
print(movies)



authors = {"Rafeh Qazi": ['b1','cleverprogrammer.com/blog/2','Programming'],"John Sonmez": ['b1','SimpleProgrammer.com','Programming']}
print authors
print(authors['John Sonmez'][1])


#Dictionary + Create Keys + Change Values + Word Frequency Counter
sentence = "Hey how are you doing? hey hey hey are you doing alright?"

final_dictionary = {}

for word in sentence.split():
  
  if word not in final_dictionary:
    final_dictionary[word] = 1
  else:
    final_dictionary[word] = final_dictionary[word] + 1
    
print(final_dictionary)

test_sentence = "Hey how are you doing? hey hey hey are you doing alright?"

#Writing in funcction 
def word_frequencey(sentence):
  final_dictionary = {}
  
  for word in sentence.split():
    if word not in final_dictionary:
      final_dictionary[word] = 1
    else:
      final_dictionary[word] += 1
  
  return final_dictionary
    
print(word_frequencey(test_sentence))
    







