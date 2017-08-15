import scipy
import numpy
from scipy import misc
import glob
image=misc.imread('C:/Users/vivek4/Desktop/top.png')

# change image dimension
image.shape

import matplotlib.pyplot as plt
plt.imshow(image)
plt.show()

b=b=image[0:200,:,:]
plt.imshow(image)
plt.show()
