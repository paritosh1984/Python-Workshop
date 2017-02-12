>>> b=numpy.array([[1,2,3],[2,3,4]])
>>> b
array([[1, 2, 3],
       [2, 3, 4]])
>>> b[0]
array([1, 2, 3])
>>> b[1]
array([2, 3, 4])
>>> b[1][1]
3
>>> b[1,1]
3

#shape provides the matrix dimensions
>>> b.shape
(2, 3)
>>>

# get number of rows
>>> b.ndim
2

#get total number of elements in the matrix

>>> b.size
6
>>>

