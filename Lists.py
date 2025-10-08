a=[1,2,3,4,5,6,78,]
b=["hello",1,23,455,22,1,1,True,[1,2,3,42,1]]
# PRINTING A LIST
print(a)
print(b)
# PRINTING THE LENGTH OF A LIST 
print(len(a))
print(len(b))
# INDEXING IN A LIST 
print(a[0])
print(a[2])
print(a[1:])
print(a[:4])
# ADDING NEW ITEM TO A LIST
a[1]="Sumit"
print(a)
# APPEND COMMAND
a.append("Hello World")
print(a)
# EXTEND COMMAND
a.extend("Hello World")
print(a)
a.extend(b)
print(a)
# POP COMMAND
item=a.pop()
print(a)
item = a.pop(1)
print(a)
# SORT COMMAND 
a.sort()
print(a)
# LIST COMPREHENSION
matrix=[[1,2,3],[4,5,6],[7,8,9]]

first_col= [row[0] for row in matrix]

print(first_col)