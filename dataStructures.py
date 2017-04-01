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

# remove() function is used to remove an element from a list based on value
>>> a
[10, 'vivek', 20, 'abc', 1, 2, 1, 2, 4]
>>> a.remove('vivek')
>>> a
[10, 20, 'abc', 1, 2, 1, 2, 4]
>>>
>>> a.remove('vivek')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>>

#pop is used to extract last element from the list 
>>> a
[10, 20, 'abc', 1, 2, 1, 2, 4]
>>>
>>>
>>>
>>> a.pop()
4
>>> a
[10, 20, 'abc', 1, 2, 1, 2]

# pop() can also pop an element from location 'i', for example,
# in the following code, we pop an element from index - 2 
>>> a
[10, 20, 'abc', 1, 2, 1, 2]
>>> a.pop(2)
'abc'
>>> a
[10, 20, 1, 2, 1, 2]
>>>

# remove all element from the list using clear() function
>>> a
[10, 20, 1, 2, 1, 2]
>>> a.clear()
>>> a
[]

#use index() function to find location of a element in a list
>>> a.extend([1,2,4,5])
>>> a
[1, 2, 4, 5]
>>> a.index(2)
1
>>> a.index(4)
2
>>>

# in case of multiple elements, index() provides the location of the first element
>>> a.append(4)
>>> a
[1, 2, 4, 5, 4]
>>> a.index(4)
2
>>>


