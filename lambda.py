# item_One = lambda x: x*3   #create lambda variable for 
# prin(lambda)
# print(item_One)
# 1) Make a decorator which calls a given function twice. 
# You can assume the functions don't return anything important, 
# but they may take arguments.
@twice
@people
def double():
    print("Hello World")

def inner(double):
    def inner(*args):
        print("Hello")
        double(*args)
        print(2,3)
    print(inner)

