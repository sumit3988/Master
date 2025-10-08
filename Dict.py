# DICTIONARY IN PYTHON
my_stuff={"key1":"value","key2":"Value2" }

print(my_stuff["key2"])

# INDEXING IN DICTIONARY

my_stuff_2={"key1":"value","key2":"Value2","key3":{'123':[1,2,3,'pickme']}}
print(my_stuff_2['key3']['123'][3])

# TO MAKE THE INDEXED ONE UPPER OR LOWER
my_stuff_2={"key1":"value","key2":"Value2","key3":{'123':[1,2,3,'pickme']}}
print(my_stuff_2['key3']['123'][3].upper())

print(my_stuff_2['key3']['123'][3].lower())