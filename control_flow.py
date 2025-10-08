# If-Else statement
if 1<2:
 print('yes')
 if 2<3:
  print("true")
if 1>2:
 print("WTF")
elif 3==2:
 print("Right")
else:
 print("MKB fat ja ga")

# printing the element of a list
 seq=[1,2,3,4,5,6,7]

 for item in seq:
  print(item)

# Printing the element of a dictionary
d={"sam":1,"frank":2,"dan":3}

for k in d:
   print(k)
   print(d[k])

# printing the tuples in a list
mypairs=[(1,2),(3,4),(5,6)]

for item in mypairs:
 print(item)

# printing the elements of a tuple
for tup1,tup2 in mypairs:
    print(tup1)
    print(tup2)

# while loop 
i =0

while i<=5:
  print("The value of i is {}".format(i))
  i=i+1

# Range 
for item in range(1,10,2):
  print(item)

# list comprehension
x=[1,2,3,4,5]

out=[]
for num in x:
  out.append(num**2)

print(out)

# Another method for list comprehension
x=[1,2,3,4,5,6,7,8,9]

out = [num**2 for num in x]

print(out)