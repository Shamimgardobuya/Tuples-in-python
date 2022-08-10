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