# create a class vehicle 
#provide function for speeding and braking
#create a child class of the Vehicle 
#make it ingherit the two funtions
class Vehicle:
    def __init__(self,distance,duration):
        self.distance=distance
        self.duration=duration
    def __str__(self):
        return f"{self.distance} for {self}"
    def speeding(self):
        #create variable  for multiplyng distance and duration.
        speed=self.distance//self.duration
        return f"this is the speed,{speed}km/h of a car travelling at {self.distance} for {self.duration}min"
# class Bus():
import math

start=int(input("Enter the starting range"))
end=int(input("Enter the ending range"))

while start<=end:    
    new_numb=math.ceil(math.sqrt(start))   #create an integer of the square root of the starting number
    count=0                             #create a default variable
    for i in range(2,new_numb+1):    #loop through the range from 2 to the interger you created 
        if start%i==0:                         
            count=1
            # print("Hello")
    if count==0:                           
            print(start)

    start=start+1                             #for the increament
   
#  Write a Python program to get the length 
#  in bytes of one array item in the internal representation. 
    # create an array of numberss
    #loop through each element and convert the items to string
    #find the byte of the element in array.
def byte(x):
    for i in x:
       print( bytes(i))
    # for i in x:
       print( bytes(x))
       
byte([3,4,5,6,7])

    