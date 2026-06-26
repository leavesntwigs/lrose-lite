
from ctypes import *
cdll.LoadLibrary("TestDataPassing.dylib")
lroselib = CDLL("TestDataPassing.dylib")
lroselib.RadxEvad


ray = c_float * 10
ii = ray(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

div = c_float * 10 

nGates = c_int()
lroselib.RadxEvad(byref(ii), nGates, byref(div))


# passing arrays ...

>>> myarr = c_float * 5
>>> ii = myarr(1,2,3,4,5)
>>> ii
<__main__.c_float_Array_5 object at 0x1059797c0>
>>> jj = myarr(0,0,0,0,0)
>>> jj
<__main__.c_float_Array_5 object at 0x105979e00>
>>> lroselib.RadxEvad(ii, nGates, jj)
45210384
>>> for j in jj: print(j, end=" ")
... 
4.0 4.0 4.0 0.0 0.0 >>> 
>>> 

This worked!!!

import ctypes 
import numpy as np
   
# load the library ...
cdll.LoadLibrary("TestDataPassing.dylib")
lroselib = CDLL("TestDataPassing.dylib")

# set the in and out arrays ...
>>> x
array([12., 13., 11.,  1.])
>>> y = np.array([1.0, 1.0, 1.0, 1.0])
>>> y
array([1., 1., 1., 1.])
>>> x
array([12., 13., 11.,  1.])

# create a pointer type ...
>>> c_float_p = ctypes.POINTER(ctypes.c_float)

# make sure the in and out arrays are of the correct type ...
>>> x
array([12., 13., 11.,  1.])
>>> x = x.astype(np.float32)
>>> y = y.astype(np.float32)
>>> x
array([12., 13., 11.,  1.], dtype=float32)
>>> y
array([1., 1., 1., 1.], dtype=float32)

# call the C++ library ...
>>> lroselib.RadxEvad(x.ctypes.data_as(c_float_p), c_size_t(4), y.ctypes.data_as(c_float_p))
55625936

# notice the changed output array ...
>>> y
array([4., 4., 4., 1.], dtype=float32)
>>> x
array([12., 13., 11.,  1.], dtype=float32)


