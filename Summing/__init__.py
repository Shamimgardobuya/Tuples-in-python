# create a new function called sum(), 
# which takes an iterable (a list, tuple, or set) and
#  adds the values together:

#create a function and pass a params
#create a sum variable and assign it a zero
#using recursion,assign each number to the value


def findsum(list_one):
    sum=0
    for i in list_one:
        sum+=i
    return sum
# findsum([2,35,7])   #output is 44
    # if list_one==0:
    #     return 0

    # else:
    #     (findsum(list_one-1))

