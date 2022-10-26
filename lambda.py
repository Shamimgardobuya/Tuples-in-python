# item_One = lambda x: x*3   #create lambda variable for 
# prin(lambda)
# print(item_One)
# 1) Make a decorator which calls a given function twice. 
# You can assume the functions don't return anything important, 
# but they may take arguments.





# # def twice(function):
# #      def wrapper ():
# #         func=function()
# #         addition=func.upper()
# #         return addition
# #      return wrapper 
# # @twice
# # def double():
# #     print("Hello World")
# # decorator=twice(double)
# # decorator()
# import functools


# def uppercase_decorator(function):
#     @functools.wraps(function)
#     def wrapper(numb1,numb2):
#         # func = function()
#         print("My favorite number is {numb1}{numb2}".format(numb1,numb2))
#         function(numb1,numb2)
#     return wrapper
# @uppercase_decorator()
# def say_hi(city1,city2):
#     print("Cities i love are {0} and{1}".format(city1,city2))

# say_hi("Nairobi","Bungoma")

# decorate = uppercase_decorator(say_hi)
# decorate()

# def inner(double):
#     def inner(*args):
#         print("Hello")
#         double(*args)
#         print(2,3)
#     print(inner)
   #practicing floyd's triangle
    #create a function and
from operator import indexOf


def floyd_triangle():
    start=int("Enter a number ")
    number_first=1

#   Return a new set of identical items from two sets

  #create two sets with some identical items
  #find 
  #return the new set made 
def sets_mine():
    set_end={}
    
    set_one={"food",1,2,3}
    set_two={"pip",2,3,5}
    for i,b in zip(set_one,set_two):
        if i==b:
            # set_end.add(i)
            # set_end.add(b)
             print(set_end)

    set_three=set_one.intersection(set_two)
    print(set_three)
sets_mine()
    #   Write a Python program to triple 
# print(set_three)
sets_mine()
    #   Write a Python program to triple 
    #   all numbers of a given list of integers. U
    #   se Python map.
#create a function and pass in a parameters
#return the function preferred like returning each item and multiply by 3
#create variable for holding  map function and link function with list 
#print the list of variable
def tripple(number):
    return number*3
# result=[1,2,3,4,56]
ans_for_map=map(tripple,[1,2,3,4,5,56])
print(ans_for_map)
print(list(ans_for_map))
# Write a Python program to add three 
# given lists using Python map and lambda
 #create 3 lists of integers 
 #create a variable holding map function inside it the lambda syntax
 #use each argument with a different variable 
 #using map,map the addition function to all the original list 

 #pass in  the 3 list as values
list_one=[1,2,3,5]
list_two=[3,4,5]
list_three=[4,5,6]
# function=lambda list_one,list_two,list_three:list_one+list_two+list_three
# function=lambda list_one,list_two,list_three:list_one+list_two+list_three

mapping=map(lambda x,y,z:x+y+z,list_one,list_two,list_three)
print(f"The addition of the elements in the three lists  is {list(mapping)}")

#    Update the first set with items 
#    that don’t exist in the second set
# Write a Python program to create a list containing the power of said number in 
# bases raised to the corresponding number in the 
# index using Python map
#base number is the number  to be powered 
#any number powered to zero is 1

  #mean 1 power 0
  #create function and pass in a parameter
  #using index of function together with the ^ find its power
list_example=[1,2,3,4]

map_me=map(lambda x:x^x.index(x),list_example )
# print(list(map_me))