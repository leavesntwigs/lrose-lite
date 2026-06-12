
//using namespace std;

extern "C" 
{
   void RadxEvad (
//     const float *sweep_index, 
     const float *rays, 
    // sweeps, and rays:  pass by reference, i.e. pointer (ctypes::byref() which is faster than pointer()) pass as an xarray.DataArray 
     int  nGates,
   
   // --- output arguments, values returned ---
//     float *ht, 
//     float *uu, 
//     float *vv, 
//     float *ww, 
     float *div
    );
}

void RadxEvad (
// const float *sweep_index,
 const float *rays,
// sweeps, and rays:  pass by reference, i.e. pointer (ctypes::byref() which is faster than pointer()) pass as an xarray.DataArray
 int  nGates,

   // --- output arguments, values returned ---
// float *ht,
// float *uu,
// float *vv,
// float *ww,
 float *div
) 
{
   // *nGates = 47;    
  div[0] = div[1] = div[2] = nGates;
}
