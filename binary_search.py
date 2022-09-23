#create a function and inside the body
#create a list of numbers
#find number 4
#find the midpoint of the list 

def binaring():
    x=100
    list_test=[20,500,10,5,100,1,50]
    mid=len(list_test)//2
    if x>list_test[mid]:
        return 'hello'
    elif(x<list_test[mid]):
        return 'not yet'
    # start=77
    # for i in list_test:
    #     if list_test[i]==start:
    #         print("Found")
    #     else:
    #         print("Not executed")
a=binaring()
print(a)
def linear_search():
    list_test=[20,500,10,5,100,1,50]


    start=20
    p=list_test[0]
    for i in list_test:
        if i==start:
           print("Found")
           return 0
        else:
          print("Not executed")
          return 1
linear_search()

# Given two lists, l1 and l2, 
# write a program to create a third list l3 
# by picking an odd-index element from the list l1 
# and even index elements from the list l2.

  #cretae a function 
  #inside the block of function creae listone and two
  #loop through and find odd indexes from list one
  #loop through and find even indices in list two
  #append the items to list 3


def three():
    list_one=[1,2,3,4,5,6]
    list_two=[3,4,5,6]
    list_three=[]
    for i in range(0,len(list_one)):    #looping through a list using a range function
        if list_one[i]%2!=0:            #able to find index
            print(list_one[i])
            list_three.append(i)        #adds element at end of the list 
    print(list_three)
            # return 0
        # else:
        #     print("hi")
    y=0
    while y < len(list_two):
        # print("Hello Liz")
        if list_two[y]%2==0:
            print(y)
            list_three.append(y)
            print(list_three)
            y+=1
        # else:
        #     # return 1
        #     print("Hello")
        #     return 0
three()




