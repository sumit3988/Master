#HOW TO PRINT NORMAL STRING
a= "My Name is Sumit"
print(a)
#FOR UPPER CASE
x= a.upper()
print(x)
# FOR LOWER CASE
y=a.lower()
print(y)
# FOR SWAP CASE
z=a.swapcase()
print(z)
# FOR SPLITING
p=a.split("e")
print(p)

#INDEXING
print(a[1])
print(a[0])
print(a[11])
print(a[::1])
print(a[::2])


# PRINT FORMATIING
s="Insert another thing here: {}".format("INSERT ME!!")
print(s)
# ADDING MULTIPLE VALUES AT ONCE 
t="1st value: {x} 2nd value: {y}".format(x="Hello",y="World")
print(t)
