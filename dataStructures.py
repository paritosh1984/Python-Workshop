# https://docs.python.org/3/tutorial/datastructures.html

# A list is a vector which contains different data types. In the following example,
# we create a list containing three values - 10, 20, 'abc'.
>>> a=list()
>>> a
[]

# append() function is used to add an element to the end of the list
>>> a.append(10)
>>> a
[10]
>>> a.append(20)
>>> a
[10, 20]
>>> a.append('abc')
>>> a
[10, 20, 'abc']
>>>

>>> a.insert(1,'vivek')
>>> a
[10, 'vivek', 20, 'abc']
>>>

>>> a.extend([1,2])
>>> a
[10, 'vivek', 20, 'abc', 1, 2]
>>>

# merge two list
>>> b=[1,2,4]
>>> b
[1, 2, 4]
>>>
>>>
>>> a.extend(b)
>>> a
[10, 'vivek', 20, 'abc', 1, 2, 1, 2, 4]
>>>

