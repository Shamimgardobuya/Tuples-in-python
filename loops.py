# Write a program to display all prime numbers within a range
   # this a program for printing prime numbers within a range.
# one divisible,one and itself
# create function and pass in a paramater 
   #using a while loop loop ,loop through the range of the number
   #using a for loop the number is prime only if it is divisible by itself and one
   #else not a primenumber 

def priming(z):
    # x=0
    # while x<z:
    #     if ((x%1==0) and (x%z==0)):
    #         print(f"{x} is a prime number")
    #         x
    #     else:
    #         print("Not a prime number")
    #         break
      for i in range(1,z):
        if i%2==1  or i%5==3 :
          print(f"{i} is a prime number")
        elif z==2:
           print("Is a prime number")
        else:
         print(f"{i} not a prime number")

priming(10)
# print(a)
  #create a function with paramter 
  #create a variable and assign it a number 1
  #create another variabl for the loop and assign it a 0
  #loop through up to the number
  #multiply each number and assign it to the factorial variable
  #call the function

def numb(y):
   factorial=1
   counter=1
   while (counter<y):
      factorial*=counter
      counter+=1

   print(f"the factorial of {y} is {factorial}")
numb(6)
# numb(7)




#  print(a)
  #create a function with paramter 
  #create a variable and assign it a number 1
  #create another variabl for the loop and assign it a 0
  #loop through up to the number
  #multiply each number and assign it to the factorial variable
  #call the function

#   OOP Exercise 3: Create a child class 
#   Bus that will inherit all of the variables 
#   and methods of the Vehicle class
  #create a class with parameters of color and speed
  #create a child class Bus that will inherit from Car
class Car:
   def __init__(self,color,number_plate):
     self.color=color
     self.number_plate=number_plate
   def numbering(self):
         return f"Hello{self.color}"

class Bus(Car):
   def __init__(self, color,number_plate):
    super().__init__(number_plate,color)
         #   self.color=color
    self.number_plate=number_plate
   def numbering(self):
      return f"Hi {self.color}"
    #multiple inheritance,an object inheriting from two classes

#current occurences in python
  #create a string and the number of their occurrences to be as keys and the value the letter
  #create a function and pass in paramters
  #create an empty dictionary 
  #loop through the string 
  #create a condition if character in string 
  #if in sstring,pass in the dictionary
def counting(word):
  dict_words={}     #create an empty dictionary
  for z in word:      #loop through the word
    if z in dict_words:       #check if character in the word
      dict_words[z]+=1         #append the number as the value
    else:
      dict_words[z]=1              #else should print one
  print(dict_words)               #return the whole string
wording2=input("Enter a word ") 
# wording2=word
counting(wording2)

   #Age calculator in python
   #create a fnuction and pass in 3 parameters of day of birth
   #import datetime
   #Create toda's date in a variable
   #create variable for holding dateteime
   #create variable age and assign it to today from date of birth
def ageCalculator(y,m,d):
  import datetime
  today=datetime.datetime.now.date()
  dob=datetime.date(y,m,d)
  your_age=int(today-dob)


    


