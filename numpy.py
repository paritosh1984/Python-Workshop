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

#getting data columnwise
>>> b[:,0]
array([1, 2])
>>> b[:,2]
array([3, 4])
>>> b[:,3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: index 3 is out of bounds for axis 1 with size 3
>>> b[:,2]
array([3, 4])
>>>

#alternate ways to create numpy arrarys
>>> kk=numpy.zeros(6,dtype=numpy.int)
>>> kk
array([0, 0, 0, 0, 0, 0])
>>>
>>> kk=numpy.zeros(6)
>>> kk
array([ 0.,  0.,  0.,  0.,  0.,  0.])
>>>
>>> numpy.arange(6)
array([0, 1, 2, 3, 4, 5])

>>> xx
array([0, 1, 2, 3, 4, 5])
>>> id(xx)
52309192
>>>
>>>
>>>
>>> yy=numpy.arange(6)
>>> id(yy)
2481472
>>>
>>>
>>> xx is yy
False
>>>
>>> zz=xx
>>>
>>> zz is xx
True
>>>
>>> id(xx.base)
1365666200
>>>
>>>
>>> id(zz.base)
1365666200
>>>
>>>
>>> id(yy.base)
1365666200
>>>

>>> xx.astype(str)
array(['1', '2', '3'],
      dtype='<U11')
>>>

>>> xx
array([1, 2, 3])
>>> xx.mean()
2.0
>>>
>>>


>>> yy=np.array([[1,2,3],[4,5,6]])
>>>
>>>
>>> yy
array([[1, 2, 3],
       [4, 5, 6]])
>>>
>>>
>>>
>>> yy.shape
(2, 3)


>>>
>>> yy.size
6
>>>


#calcualting mean columnwise
>>> np.mean(yy,axis=0)
array([ 2.5,  3.5,  4.5])
>>>

>>> np.savetxt('file.csv',yy)





