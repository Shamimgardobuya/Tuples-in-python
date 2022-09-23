# The Python abs() function 
# return the absolute value and
#  remove the negative sign of a number in 
def loop():                 #create a function 
    list_one=[[1,2,3,4],[3,4,5,6]]   #create a main list with sub list inside
    z=0                             #create a initial variable
    while z< len(list_one):         #loop through the length of the list     
        print(list_one[z])          
        z+=1
loop()                #call function

#create a function and pass in parameter
#create a binary number 
#using the abs function,
#print the number
def abs_function(numb):
    abss=abs(numb)
    print(abss)
abs_function(-5)
#using lambda function,
    # Write a Python program to create 
    # a lambda function that adds 15 to a
    # given number passed in as an argument,
    # also create a lambda function that multiplies
    # argument x with argument y and print the result.
#create  a lambda function
#create a return type of addying 15 to a number
#create an iterable and render the output
x=lambda a,b,c:a+b+c
print(x(1,2,3))
x=lambda a,b:a*b
print(x(2,3))






