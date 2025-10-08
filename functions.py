# using def keyword to make a function
def my_func() :
    '''
    THis is a docstring
    '''
    print("my first python function !")

my_func()

def addnum(num1,num2):
    return num1+num2

result =addnum(4567,567)
print(result)

result=addnum("Hello",' world')
print(result)

# if you want to use the same data type 
def add_num(num1,num2):
    if type(num1)==type(num2)==type(10):
        return num1+num2
    else:
        return("Sorry oly integer input")


a= 2
b="sum"

result=add_num(a,b)

print(result)

# lambda function

mylist=[1,2,3,4,5,6,7,8,9,2,3,4,5]


evens =filter(lambda num:num%2==0,mylist)

print(list(evens))


# filter

mylist=[1,2,3,4,5,6,7,8,9,2,3,4,5]

def even(num):
    return num%2==0

evens =filter(even,mylist)

print(list(evens))