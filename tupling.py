# #Create a list of tuples from given list having number and its cube in each tuple
# def tuplist():
#     p=[1,2,3,4]
#     z=tuple(p)
# #     n=0
#     while(n<len(z)):     #index to be less
#         z[n]*3
#         print(z[n]**3)
#         # ', '.join('{}={}'.format(*z) for n in z)

#         print(z,end='')  #use .end to make output in one line
#         n+=1
# tuplist()
  #Python – Maximum and Minimum K elements in Tuple
     #create a default varable representing the first element
     #loop through the tuple 
     #condition if it is greater
     #then assign i to maximum number
     # print the maximum number
     #di the vice sersa for minimum
def max_min(tup2):
   word2=tup2[0]
   for i in tup2:
    if i>word2:
      word2=i
   print(word2)
max_min((2,3,4,5,6))
def min_mum(tup3):
   word3=tup3[0]
   for i in tup3:
      if i<word3:
         word3=i
   print(word3)
min_mum((2,4,5,6))
              #Row-wise element Addition in Tuple Matrix
#create a list inside a list
#inside list create elements of tuples
#create a list having elements to be added in row wise manner
#xreate a variable and assign each variable

#loop through the original list using lists with zip function
def matrix():
   list3=[[(123,3,4,5),(4,7),(8,69)]]
   listm=[8,2]
   looping=[[(numb,listm2)for numb in key]for key,  listm2 in zip(list3,listm)]
   print(looping)
matrix()

         
   #loop through the original list using lists with zip function
def counting (p):
   z=""
   x=0
   while x<len(p):
      z+=p[x]
      x+=1
   print(f"{z} is the new word")
counting(["c","a","t"])

