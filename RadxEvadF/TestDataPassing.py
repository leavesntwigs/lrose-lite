
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
>>> nGates
4

