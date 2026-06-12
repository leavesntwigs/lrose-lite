// *=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=* 
// ** Copyright UCAR (c) 1990 - 2026                                         
// ** University Corporation for Atmospheric Research (UCAR)                 
// ** National Center for Atmospheric Research (NCAR)                        
// ** Boulder, Colorado, USA                                                 
// ** BSD licence applies - redistribution and use in source and binary      
// ** forms, with or without modification, are permitted provided that       
// ** the following conditions are met:                                      
// ** 1) If the software is modified to produce derivative works,            
// ** such modified software should be clearly marked, so as not             
// ** to confuse it with the version available from UCAR.                    
// ** 2) Redistributions of source code must retain the above conypyright      
// ** notice, this list of conditions and the following disclaimer.          
// ** 3) Redistributions in binary form must reproduce the above copyright   
// ** notice, this list of conditions and the following disclaimer in the    
// ** documentation and/or other materials provided with the distribution.   
// ** 4) Neither the name of UCAR nor the names of its contributors,         
// ** if any, may be used to endorse or promote products derived from        
// ** this software without specific prior written permission.               
// ** DISCLAIMER: THIS SOFTWARE IS PROVIDED "AS IS" AND WITHOUT ANY EXPRESS  
// ** OR IMPLIED WARRANTIES, INCLUDING, WITHOUT LIMITATION, THE IMPLIED      
// ** WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.    
// *=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=* 
///////////////////////////////////////////////////////////////
// RadxEvad.cc
//
// Mike Dixon, RAP, NCAR, P.O.Box 3000, Boulder, CO, 80307-3000, USA
//
// Feb 2013
//
// Functional adaptation by Brenda Javornik NCAR
// June 2026
//
///////////////////////////////////////////////////////////////

#include <toolsa/mem.h>

// #include "RadxEvad.hh"
/*
#include <Radx/RadxSweep.hh>
#include <Radx/RadxRay.hh>
#include <Radx/RadxField.hh>
#include <Radx/RadxTime.hh>
#include <Radx/RadxTimeList.hh>
#include <Radx/RadxPath.hh>
//#include <Ncxx/Nc3xFile.hh>
//#include <Mdv/GenericRadxFile.hh>
#include <dsserver/DsLdataInfo.hh>
#include <toolsa/pmu.h>
#include <toolsa/toolsa_macros.h>
#include <toolsa/sincos.h>
#include <toolsa/TaArray.hh>
#include <toolsa/Path.hh>
#include <toolsa/file_io.h>
#include <rapmath/RapComplex.hh>
#include <physics/IcaoStdAtmos.hh>
#include <physics/thermo.h>
//#include <Spdb/SoundingPut.hh>
#include <algorithm>

using namespace std;
*/

extern "C" 
{
   void RadxEvad (
     const float *sweep_index, 
     const float *rays, 
    // sweeps, and rays:  pass by reference, i.e. pointer (ctypes::byref() which is faster than pointer()) pass as an xarray.DataArray 
     int  nGates,
   
   // --- output arguments, values returned ---
     float *ht, 
     float *uu, 
     float *vv, 
     float *ww, 
     float *div
    );
}

void RadxEvad (
 const float *sweep_index,
 const float *rays,
// sweeps, and rays:  pass by reference, i.e. pointer (ctypes::byref() which is faster than pointer()) pass as an xarray.DataArray
 int  nGates,

   // --- output arguments, values returned ---
 float *ht,
 float *uu,
 float *vv,
 float *ww,
 float *div
) 
{


const double missingVal = -9999.0;
const double pseudoEarthDiamKm = 17066.0;

/// return height, speed, direction, u_wind, v_wind


// This is going to be a function in a shared library call liblroselite
// pyart.retrieve.vad_michelson(radar, vel_field=None, z_want=None, gatefilter=None)[source]
// wradlib ?? ask Kai

/*
return flat-structure-of-information RadxEvad(radarVolumeDataModel??, or flat-structure-information??, params)
What information is needed from the radar volumne?
If this approach, then I need to change more code, ???
 sweeps ???  pass by reference, i.e. pointer (ctypes::byref() which is faster than pointer()) pass as an xarray.DataArray
Send data for VEL variable for radar volume; send all sweeps, all rays, all ranges; ordered by...
sweep[0]
VEL.ray[0][gate0 ... gateN]
VEL.ray[n][gate0 ... gateN]
sweep[1]
VEL.ray[0][gate0 ... gateN]
VEL.ray[n][gate0 ... gateN]
sweep[n]
VEL.ray[0][gate0 ... gateN]
VEL.ray[n][gate0 ... gateN]

How to distinguish which rays are in which sweep?  
   How are the data stored in the xradar.DataTree?  Use this layout to pass the data.
   pass array of indexes into the rays, for the first ray and last ray of a sweep; pass as a list of tuples?  or just a list, where i mod 1 == 0 ==> first ray, 
                           i mod 1 == 1 ==> last ray

rays:  pointer to list of VEL data continuous like this ...
ray[0][gate0 ... gateN]
ray[n][gate0 ... gateN]

Data Access:
   Access the raw data using da.data or da.values (which returns a numpy.ndarray).

Memory Continuity:
   ctypes requires contiguous memory. If the xarray data is not contiguous (e.g., after certain slicing operations), you must use .copy() or np.ascontiguousarray() before passing it to C.

Data Type Matching:
   Ensure the xarray dtype matches the ctypes type (e.g., float64 to ctypes.c_double)

If radar-volume-data-model, then I need to convert xradar to RadxVol structure, using ctypes.

*/

/*
void RadxEvad (
  const float *sweep_index, 
  const float *rays, 
 // sweeps, and rays:  pass by reference, i.e. pointer (ctypes::byref() which is faster than pointer()) pass as an xarray.DataArray 
  size_t _nGates,
  float _radxStartRange,
  float _radxGateSpacing,
  // _radarName,
  float _radarLatitude,
  float _radarLongitude,
  float _radarAltitude,

// --- output arguments, values returned ---
  float *ht, 
  float *uu, 
  float *vv, 
  float *ww, 
  float *div,

// ----  tunable parameters ----
  float min_range,
  float max_range,
  float delta_range,
  bool range_gate_geom_equal,
  float _radxStartRange,
  float _radxGateSpacing,
  float min_elev,
  float max_elev,
  size_t _nRanges,
  // _ring,
  bool compute_profile_spacing_from_data,
  bool debug)

// RadxEvad(int argc, char **argv)
  
{
*/

  //int OK = TRUE;

//  if (_params_override_radar_location) {
//    if (_params_radar_latitude_deg < -900 ||
//        _params_radar_longitude_deg < -900 ||
//        _params_radar_altitude_meters < -900) {
//      cerr << "ERROR: " << _progName << endl;
//      cerr << "  Problem with command line or TDRP parameters." << endl;
//      cerr << "  You have chosen to override radar location" << endl;
//      cerr << "  You must override latitude, longitude and altitude" << endl;
//      cerr << "  You must override all 3 values." << endl;
//      OK = FALSE;
//    }
//  }

  // matrix allocation

  double **_AA;
  double **_AAinverse;
  const static int nFourierCoeff = 7;
  const static int nDivCoeff = 2;

  _AA = (double **) umalloc2(nFourierCoeff, nFourierCoeff, sizeof(double));
  _AAinverse = (double **) umalloc2(nFourierCoeff, nFourierCoeff, sizeof(double));

  double **_PP;
  double **_PPinverse;
  _PP = (double **) umalloc2(nDivCoeff, nDivCoeff, sizeof(double));
  _PPinverse = (double **) umalloc2(nDivCoeff, nDivCoeff, sizeof(double));

  // initialize the azimuth slice geometry, making sure we have
  // an integral number of slices

}
