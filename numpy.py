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

#get data type of the matrix elements
>>> b.dtype
dtype('int32')

#size of each element
>>> b.itemsize
4
#getting shape values in variables
>>> m,n=b.shape
>>>
>>>
>>> m
2
>>> n

