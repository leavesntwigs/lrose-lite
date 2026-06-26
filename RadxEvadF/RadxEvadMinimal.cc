#include <stddef.h>

// slice and dice the data in python
// only send what is needed
// deal with missing data in python

extern "C" 
{
   void RadxEvad (
     const size_t *sweep_index, 
     const size_t nsweeps,
     const float *rays, 
     const size_t nrays,
     const float *elevs, // elevation for each sweep
     const float *azs,   // azimuth for each ray
     size_t  nGates,
     float startRangeKm,
     float gateSpacingKm,
     float radarLatitudeDeg,
     float radarLongitudeDeg,
     float _radarAltitude, 
     float nyquist,
     float *ht, 
     float *uu, 
     float *vv, 
     float *ww, 
     float *div
    );
}

#include <vector>
#include <string>
#include <iostream>
#include <toolsa/mem.h>
#include <toolsa/toolsa_macros.h>
#include <toolsa/sincos.h>
#include <toolsa/TaArray.hh>
#include <rapmath/RapComplex.hh>
#include <physics/IcaoStdAtmos.hh>
#include <physics/thermo.h>

/////////////////////////////////////////////////////
// define functions to be used for sorting

int _doubleCompare(const void *i, const void *j)
{
  double *f1 = (double *) i;
  double *f2 = (double *) j;
  if (*f1 < *f2) {
    return -1;
  } else if (*f1 > *f2) {
    return 1;
  } else {
    return 0;
  }
};

void RadxEvad (
 const size_t *sweep_index,
 const size_t nsweeps,
 const float *rays,
 const size_t nrays,
 const float *elevs,
 const float *azs, 
 size_t nGates,
 float startRangeKm,
 float gateSpacingKm,
 float radarLatitudeDeg,
 float radarLongitudeDeg,
 float radarAltitude,
 float nyquist,
 float *ht,
 float *uu,
 float *vv,
 float *ww,
 float *div
) 
{

    div[0] = 47;


};

