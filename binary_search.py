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

