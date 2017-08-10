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

# to find index of an element within a subsection of list
>>> a.extend([5,4,6])
>>> a
[1, 2, 4, 5, 4, 5, 4, 6]
>>>
>>>

# a.index(4,5,7) looks for element 4 in the subsection a[5:8]
>>> a.index(4,5,7)
6
>>>

#accessing element using : operator
# a[m,n] gives all elements starting with m index and upto (n-1) index.
>>> a
[1, 2, 4, 5, 4, 5, 4, 6]
>>> a[0:4]
[1, 2, 4, 5]
>>>
#test

#sort() function is used to sort the list in ascending or descending order
>>> a
[1, 2, 4, 5, 4, 5, 4, 6]
>>> a.sort()
>>> a
[1, 2, 4, 4, 4, 5, 5, 6]
>>>
#to sort a list in reverse or descending order
>>> a.sort(reverse=True)
>>> a
[6, 5, 5, 4, 4, 4, 2, 1]
>>>

# reversre() function changes the order of the list, 
>>> a
[6, 5, 5, 4, 4, 4, 2, 1]
>>>
>>>
>>> a.reverse()
>>> a
[1, 2, 4, 4, 4, 5, 5, 6]
>>>

>>> a=[2,6,4]
>>>
>>> a.reverse()
>>> a
[4, 6, 2]
>>>

# make copy of a list - you can use copy() function or assignment function
>>> a
[4, 6, 2]
>>> b=a.copy()
>>> b
[4, 6, 2]
>>> c=b
>>> c
[4, 6, 2]
>>>


# difference between using copy() function and assignment
>>> a
[4, 6, 2]
>>>
>>> b
[4, 6, 2]
>>> c
[4, 6, 2]
>>> c[2]=1
>>> a
[4, 6, 2]
>>> b
[4, 6, 1]
>>> c
[4, 6, 1]
>>>

# 'b' is created from 'a' using copy() function and 'c' is created from 'b' using assignment operator. 'b' and 'c' point to same memory,
# so, when we change c[2]=1, the value of b is also changes, however, the value of a not changed.
