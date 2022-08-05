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
# numb(7)