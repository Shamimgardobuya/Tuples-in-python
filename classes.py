#create a class called reversing
#will take arguments as the string itself
#create a function  inside the class of reversing 

class Reversing:
    def __init__(self,word): #initializing object
        self.word=word
    def reversing(self):      
        # p=self.word[::-1]
        z=list(self.word)
        start=0
        end=len(z)-1
        while start<end:
            z[start],z[end]=z[end],z[start]
            start+=1
            end-=1
        print(f"The reversed string is {''.join(z)}")
class Me(Reversing):
    def __init__(self,word2):
        super().__init__("Me")   #creating a super object
        self.word2=word2
    def reversing(self):
        # self.word=word
        return f"Hello {self.word2}"
        # print( f"Hello {self.word}")
word=Me("Afia")
print(word.reversing())

        

#create a class Roman,
#pass in attribute of number

#create a function to convert the number to roman
#create a dictionary  of alg l the roman numbers from 1 to 10 as values and keys for 1 to 10 numbers
#loop through the dictionary to get keys
#if object corressponds to the key name,use square bracket to obtain its value in roman form.
#print the number

class Romaning:
    def __init__(self,number):
        self.number=number
    def romaning(self):
        roman={1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",10:"X"}
        for i in roman:
         if self.number==i:
                print(roman[self.number])
class A:
    def __init__(self):
        self.multiply(15)
    def multiply(self, i):
        self.i = 6 * i
class B(A):     #child class B takes A as argument
    def __init__(self):
        super().__init__()   #super key word
        print(self.i)
 
    # def multiply(self, i):
    #     self.i = 2 * i      
obj = B()                   #creating object from B,in polymorphism we do
                           #python will override parent class method just give it under child class
#PALINDROME WORDS USING PYTHON
#using 2 pointer fnuction 
  #create a function and pass in a word as a paramater
  #split the string
  #create a starting point and ending point of the string
  #check condition for the lenghts to be equal
  #using while loop,contiinue to loop through tthe string
  #if more characters are similar,word is paramter
def palindrome(wordx):
    p=wordx.split()
    end=len(p)-1
    end2=p[end]
    start=p[0]
    while(start<end2):
        p[start],p[end]=p[end],p[start]
        start-=1
        end+=1
        print(start)
        print(f"The reversed string is {''.join(p)}")
palindrome("Shamim")

#validating anagrams using python.
#create a function with a word as parameter
#request input from user and compare the length of the two strings and 
#loop through the string and compare
#if characters are equal to the other
def anagram(my_word):
    enter_word=str(input(f"Enter the anagram of {my_word} "))
    split_enter=enter_word.split()
    wording2=my_word.split()
    for p in wording2:
     for i in split_enter:
      if len(split_enter) == len(wording2) and ( i==p):
        print("Yay! this is an anagram")
      else:
        # print("Try again")
        #  return anagram(my_word)
        print('hello') 

# anagram("secure")
   #write program for summing up list items

   #create an initial variable as sum and assign it to 0
   #loop through using while loop
   #add each varable to the sum 
   #print the sum
def summ_list(my_list):
    sum=0
    initial=0
    while(initial<len(my_list)):
        sum+=initial
    print(sum)
summ_list([5,7,8,9])
# Write a Python program to get a list,
#  sorted in increasing order by the last element in each tuple
#   from a given list of non-empty tuples.

  #create a function and pass in a list of tuples as parameters
  #create starting variable of the list
  #loop through whole list
  #
list_tuple=[(1,2,3),(5,6,7),(8,9,10)]
my_start=list_tuple[0][2]
# for i in list_tuple:
    # if i 

  


    
    