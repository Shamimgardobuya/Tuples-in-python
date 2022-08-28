#create a class called reversing
#will take arguments as the string itself
#create a function  inside the class of reversing 

class Reversing:
    def __init__(self,word):
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
    start=p[0]
    st=0
    while(start<end):
        p[start],p[end]=p[end],p[start]
        start-=1
        end+=1
    print("Hello World")

#validating anarams using python.



    
    