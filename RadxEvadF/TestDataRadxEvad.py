from ctypes import *
import ctypes 
import numpy as np
# TODO use xradar ...

# load the data ..


# set the in and out arrays ...
# Instead of appending rows, allocate a suitably sized array, and then assign to it row-by-row:

nsweeps = 2
nAz = 4

azs = np.empty(nAz)
azs[0]=0
azs[1]=90
azs[2]=180
azs[3]=270

nGates =  3
startRangeKm = 100
gateSpacingKm = 10
radarLatitudeDeg = 30 
radarLongitudeDeg = 30
radarAltitude = 100
nyquist = 0.0

# velocity data ...
# sweep1
sweep0_vel = np.zeros((nAz,nGates), dtype=np.float32) 
sweep1_vel = np.ones((nAz,nGates), dtype=np.float32) 


nrays = nAz
print("nrays = ", nrays)

asweep = 0
sweep_index = np.empty([nsweeps])
sweep_index[0] = 0
sweep_index[1] = nrays * nGates

# a = np.empty([nsweeps*nrays,nGates])          # velocity data: [all_rays, nGates] =  [nsweeps*nrays, nGates]
# a = np.empty([nrays,nGates])          # velocity data: [all_rays, nGates] =  [nsweeps*nrays, nGates]
nAz = azs.size

# print("rays shape = ", a.shape)
# elevs = np.empty ?? or c_float ?? (nsweeps * c_float)  HERE!!!! need to define elevs somehow !!!!
elevs = np.ones(nsweeps, dtype=np.float32)   
elevs[0] = 10
elevs[1] = 20

#for group in dt_horizontal.match("/sweep_*"):
#    # WORKING HERE ... do I need to_dataset?
#    # sweep0ds = dt_horizontal['/sweep_0'].to_dataset()
#    print(f"Node Name: {group}")
#    # a[isweep*nrays:isweep*nrays+nrays] = dt_horizontal[group]["VEL"].data
#    a[isweep*nAz:isweep*nAz+nAz,:] = dt_horizontal[group]["VEL"].data
#    # mya[isweep*nrays:isweep*nrays+nrays,:]  HERE!!
#    if (isweep > 0):
#        sweep_index[isweep] = sweep_index[isweep-1] + dt_horizontal[group].azimuth.size
#        # elevs[isweep] = dt_horizontal[group].elevation??  # not currently working
#    isweep += 1
#
## really, rays is better named velocity, because it is the velocity data for all sweeps, for all azimuths/rays, for all gates/ranges
#rays = a  # need a flat structure of all the rays for all the sweeps for all the ranges/gates

rays = np.zeros((nsweeps * nAz, nGates), dtype=np.float32)
rays[0,:] = [ 0, 1, 2]
rays[1,:] = [10,11,12]
rays[2,:] = [20,21,22]
rays[3,:] = [30,31,32]
rays[4,:] = [40,41,42]
rays[5,:] = [50,51,52]
rays[6,:] = [60,61,62]
rays[7,:] = [70,71,72]

print("rays = \n", rays)

#  uu,vv are calculated for each elevation and one elevation per sweep
ht = np.zeros(nsweeps, dtype=np.float32) # initialize to all zeros
uu = np.zeros(nsweeps, dtype=np.float32) # initialize to all zeros
vv = np.zeros(nsweeps, dtype=np.float32) # initialize to all zeros
ww = np.zeros(nsweeps, dtype=np.float32) # initialize to all zeros
div = np.zeros(nsweeps, dtype=np.float32) # initialize to all zeros

# create a pointer type ...
c_float_p = ctypes.POINTER(ctypes.c_float)
c_size_t_p = ctypes.POINTER(ctypes.c_size_t)

# make sure the in and out arrays are of the correct type ...
# x = x.astype(np.float32)
# y = y.astype(np.float32)
sweep_index = sweep_index.astype(np.uintp)

# x=numpy.ascontiguousarray(x) # may not be necessary ???
 
#  
## load the library ...
#cdll.LoadLibrary("lroselite.dylib")
## <CDLL 'lroselite.dylib', handle 760e4eb0 at 0x1058fefd0>
#lroselite = CDLL("lroselite.dylib")
## lroselite.RadxEvad
## <_FuncPtr object at 0x105998790>
#
#
## set the in and out arrays ...
#
## call the C++ library ...
#lroselite.RadxEvad(sweep_index.ctypes.data_as(c_size_t_p),  
#    c_size_t(nsweeps),
#    rays.ctypes.data_as(c_float_p), 
#    c_size_t(nrays),
#    elevs.ctypes.data_as(c_float_p), 
#    azs.ctypes.data_as(c_float_p), 
#    c_size_t(nGates),
#    c_float(startRangeKm),
#    c_float(gateSpacingKm),
#    c_float(radarLatitudeDeg),
#    c_float(radarLongitudeDeg),
#    c_float(radarAltitude),
#    c_float(nyquist),
#    ht.ctypes.data_as(c_float_p),
#    uu.ctypes.data_as(c_float_p),
#    vv.ctypes.data_as(c_float_p),
#    ww.ctypes.data_as(c_float_p),
#    div.ctypes.data_as(c_float_p),
#    )
### 55625936
##
### notice the changed output array ...
##ht
### array([4., 4., 4., 1.], dtype=float32)
##uu
### array([12., 13., 11.,  1.], dtype=float32)
##
##
