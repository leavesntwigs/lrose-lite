from ctypes import *
import ctypes 
import numpy as np
# TODO use xradar ...

# load the data ..

hpc_url_horizontal_scan = "https://boreas.hpc.ucar.edu:6443/gdex-data/d694517/v2.0_zarr/cfrad.20220525_030910.927_to_20220525_031137.777_SPOL_PrecipSur2_SUR.zarr"
import xarray as xr
dt_horizontal = xr.open_datatree(hpc_url_horizontal_scan, engine="zarr", decode_timedelta=False)

#  dt_horizontal
#  ds_horizontal_sweep0 = dt_horizontal["sweep_0"].to_dataset()

# def filter_radar(ds):
#    ds = ds.assign(
#        VEL=ds.["VEL"]
#    )
#    return ds
#
## Apply the function across all sweeps
#VEL_dtree = dt_horizontal.xradar.map_over_sweeps(filter_radar)
#

# rays = dt_horizontal["/sweep_0"]["VEL"].data
#array([[-0.11261564, -1.7540228 , -1.2277151 , ...,         nan,
#                nan,         nan],
#       [-0.04292193, -2.3776615 , -0.9921984 , ...,         nan,
#                nan,         nan],
#       [ 0.0736348 , -2.0808623 , -1.7480147 , ...,         nan,
#                nan,         nan],
#       ...,
#       [-0.05373647, -1.8862005 , -1.2277151 , ...,         nan,
#                nan,         nan],
#       [ 0.25868365, -2.0688462 , -1.3418686 , ...,         nan,
#                nan,         nan],
#       [-0.13905118, -1.6747161 , -0.9213031 , ...,         nan,
#                nan,         nan]], shape=(480, 1999), dtype=float32)

# set the in and out arrays ...
# Instead of appending rows, allocate a suitably sized array, and then assign to it row-by-row:

nsweeps = dt_horizontal.dims['sweep']

azs = dt_horizontal['/sweep_0'].azimuth.data

nGates = dt_horizontal['/sweep_0'].dims['range']
startRangeKm = dt_horizontal['/sweep_0'].range.data[0]
gateSpacingKm = dt_horizontal['/sweep_0'].range.data[0] - dt_horizontal['/sweep_0'].range.data[0]
radarLatitudeDeg = np.float64(dt_horizontal['/sweep_0'].latitude)
radarLongitudeDeg = np.float64(dt_horizontal['/sweep_0'].longitude)
radarAltitude = np.float64(dt_horizontal['/sweep_0'].altitude)
nyquist = 0.0

nrays = dt_horizontal['/sweep_0'].dims['azimuth'] * nsweeps  #  nrays is total size of all rays
print("nrays = ", nrays)

isweep = 0
sweep_index = np.empty([nsweeps])
# a = np.empty([nsweeps*nrays,nGates])          # velocity data: [all_rays, nGates] =  [nsweeps*nrays, nGates]
a = np.empty([nrays,nGates])          # velocity data: [all_rays, nGates] =  [nsweeps*nrays, nGates]
nAz = azs.size

print("rays shape = ", a.shape)
# elevs = np.empty ?? or c_float ?? (nsweeps * c_float)  HERE!!!! need to define elevs somehow !!!!
elevs = np.ones(4, dtype=np.float32)   # TODO fix this

for group in dt_horizontal.match("/sweep_*"):
    # WORKING HERE ... do I need to_dataset?
    # sweep0ds = dt_horizontal['/sweep_0'].to_dataset()
    print(f"Node Name: {group}")
    # a[isweep*nrays:isweep*nrays+nrays] = dt_horizontal[group]["VEL"].data
    a[isweep*nAz:isweep*nAz+nAz,:] = dt_horizontal[group]["VEL"].data
    # mya[isweep*nrays:isweep*nrays+nrays,:]  HERE!!
    if (isweep > 0):
        sweep_index[isweep] = sweep_index[isweep-1] + dt_horizontal[group].azimuth.size
        # elevs[isweep] = dt_horizontal[group].elevation??  # not currently working
    isweep += 1

# really, rays is better named velocity, because it is the velocity data for all sweeps, for all azimuths/rays, for all gates/ranges
rays = a  # need a flat structure of all the rays for all the sweeps for all the ranges/gates

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
