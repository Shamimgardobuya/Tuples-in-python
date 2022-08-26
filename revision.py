# Write a Python class to get all possible unique subsets 
# from a set of distinct integers
# Input : [4, 5, 6]
# Output : [[], [6],[5], [5, 6],[4],[4, 6],[4, 5],[4, 5, 6]]
   #create an empty list
   #loop through each element in the first list
   #append the first and the second element
   #create another empty list,check if the items have been repeated in the new list
   #ussing zip function loop through the list.
   #if not append to new list
   #create an empty list and append an element that has not been added in any list
# import itertools-only available in another package.


import numbers
from operator import indexOf


def subbing():
    original_list=[4,5,6]
    new_sub=[]
    sec_sub=[]
    for i  in original_list:
        if i not in new_sub:
            new_sub.append(i)
    print(new_sub)
    sec_sub.append(original_list[0:2])
    print(sec_sub)
    third_sub=[]
    #use zip function to iterate over sec_sub and new_hub
    for (d,c) in zip(sec_sub,new_sub):
        if c!=d :  # will be true 
           
            third_sub.append(c)
            # third_sub.append(c)
    print(third_sub)   
    four=[]
    four.append(third_sub) 
    #how can i get 5 and 6 only?
    new2=[]
    new2.append(original_list[0:])
    five_sub=[5,6]
    six_sub=[6,5]
    seven_sub=[]
    eight_sub=[]
    seven_sub.append(five_sub[-1:])
    eight_sub.append(six_sub[-1:])
    print(four+sec_sub+new2+seven_sub,eight_sub)


    # print(z)

subbing()
  #updating each element in a tuple 
#   Python – Odd Frequency Characters
#   Python – Specific Characters Frequency in String List
       #create a tuple
       #create a counter variable and assign it to 0
       #loop through the length tuple using while loop
       #print the  increament of   each element by 2
       #print using end -''

def increase():
    w=()
    my_tup=(1,2,3,4)
    start=0
    while start<len(my_tup):
          my_tup[start]+2
          start+=1
          print(start)

    # (for x in my_tup x+2)
        #   w+=start
    # my_tup[0],my_tup[1],my_tup[3],my_tup[4]=3,7,8,6
    # for i in my_tup:
    #      i+2
          print(my_tup)
        #   print(tuple(start))
increase()
#   Python – Odd Frequency Characters
    #create a function and pass in parameter
    #loop through the string
    #create condition for printing the characters in the odd position
    #print the output

    # letter=0
    # while letter< len(words):
    #     if letter%2!=0:
    #         print(words[letter])
    #     else:
    #         print("Hello")
    #         words[letter]+=1
def character(words):

    for i in words:   #i for each element
        word2=""
        if words.index(i)%2!=0:  #index to be checked if its divisible
            word2+=i
            print(''.join(str(i) for i in word2))
        #  (words[i])
character("Microsoft")





#create  a list and find the last element 
def list_1(numbers):
    w=len(numbers)-1
    print(numbers[w])
    print(numbers[-1])
    # for i in numbers:
    #     print(i-1)
    last=numbers.pop()
    print(last)

#printing last element of a list 
    
list_1([1,2,3,4,5,6,7])
#accept-a-list-of-5-float-numbers-as-an-input-from-the-user
   #create a function
   #create an empty list
   #using while loop,compare lenghth of list and create condition for length condition

   #using input function ,request for a float type from user
   #append each float input to the empty list
def listing():
    empty_list=[]
    # number1=float(input("Enter a float number "))
    while len(empty_list)!=5:
        number1=float(input("Enter a float number "))
        
        empty_list.append(number1)
        for i in empty_list:
            print(i)
    print(empty_list)
listing()
#h-exercise-3-return-multiple-values-from-a-function
# Write a program to create function calculation() such that it can accept two variables and 
# calculate addition and subtraction. Also,
#  it must return both addition and subtraction
#   in a single return call.
   #create a function with two parameters integer
   #create a variabe for subtraction and addition
   #return a formated string of both its addition and subtraction
def calculating(number_1,number_2):
    subtract=number_1-number_2
    addition=number_1+number_2
    return f"{subtract} is the difference between the two  numbers, and {addition} is the addition between the two"
p=calculating(5,6)
print(p)

# Write a program to remove the item present
#  at index 4 and add it to the 2nd position 
#  and at the end of the list.

#create a function and pass in a list parameters
#find element at index four using assignment,assign it to second and last element
def changing(list_iteming):
    list_iteming=[1,2,3,4,5,6]
    list_iteming[4]=list_iteming[2]
    list_iteming[4]=list_iteming[-1]
    print(list_iteming)
changing([1,2,3,4,5,6])
  # Check if two sets have any elements in common. If yes, display the common elements
     #create function and pass in two arguments
def display_common():


    set1 = {5, 7, 90,}
    set2 = {60, 70, 80, 5,90}

    if set1.isdisjoint(set2):   #inbuilt for quick checker for common value in set
       print("No items in common")
    else:
        print("Common items are present ")
    print(set1.intersection(set2))
display_common()
item_One = lambda x: x*3   #create lambda variable for 
prin(lambda)
print(item_One)
  #Find the day of the week of a given date
#create function 
#request user for  day of week
#using strf time and datetime,print day of week 
