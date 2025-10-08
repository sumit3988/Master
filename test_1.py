a="django"

print(a[0])
print(a[-1])
print(a[:4])
print(a[1:4])
print(a[-3:-1])

l=[3,7,[1,4,'hello']]

l[2][2]='goodbye'
print(l)

d1={'simple_key':'hello'}
d2={'k1':{'k2':'hello'}}
d3={'k1':[{'nest-key':['this is deep',['hello']]}]}

print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest-key'][1][0])

mylist=[1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3]

a=set(mylist)
print(a)

age=4
name='Sammy'

print("Hello my dog's name is {x} and he is {y} years old".format(x=name,y=age))