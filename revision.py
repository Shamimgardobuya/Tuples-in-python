# Write a Python class to get all possible unique subsets 
# from a set of distinct integers
# Input : [4, 5, 6]
# Output : [[], [6],[5], [5, 6],[4],[4, 6],[4, 5],[4, 5, 6]]
   #create an empty list
   #loop through each element in the first list
   #append the first and the second element
   #create another empty list,check if the items have been repeated in the new list
   #if not append to new list
   #create an empty list and append an element that has not been added in any list
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
        # if d in new_sub !=c in sec_sub:
            print(d,c)
            print('hello')
            third_sub.append(d)
    # print(third_sub)

subbing()