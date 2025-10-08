#Odd- Even
#  num=int(input("Enter a number: "))

# if num % 2==0:
#     print("Even")
# else:
#     print("Odd")


# Basic Calculator

# a=float(input("Enter a number: "))
# b=float(input("Enter a number: "))
# operations= input("Enter operator (+,-,*,/): ")

# if operations=="+":
#     print("Result: ",a+b)
# elif operations=="-":
#     print("Result: ",a-b)
# elif operations=="*":
#     print("Result: ",a*b)
# elif operations=="/":
#     if b!=0:
#        print("Result: ",a/b)
#     else:
#         print("Error: Division by zero")
# else:
#     print("Invalid Operator")

#Sum of Digits


#  num=int(input("Enter a number: "))
# total=0

# while num>0:
#     total+=num%10
#     num//=10
# print("Sum of Digits: ", total)

# #Factorial Finder 

# num= int(input("Enter a number: "))
# fact =1

# for i in range(1,num+1):
#     fact*=1

# print("Factorial: ",fact)


import random

a=random.randint(0,1)

if a>0.5:
    print("Heads")
else:
    print("tails")