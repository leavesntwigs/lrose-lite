lroselite.RadxEvad(cre.sweep_index.ctypes.data_as(cre.c_size_t_p),  
    c_size_t(cre.nsweeps),
    cre.rays.ctypes.data_as(cre.c_float_p), 
    c_size_t(cre.nrays),
    cre.elevs.ctypes.data_as(cre.c_float_p), 
    cre.azs.ctypes.data_as(cre.c_float_p), 
    c_size_t(cre.nGates),
    c_float(cre.startRangeKm),
    c_float(cre.gateSpacingKm),
    c_float(cre.radarLatitudeDeg),
    c_float(cre.radarLongitudeDeg),
    c_float(cre.radarAltitude),
    c_float(cre.nyquist),
    cre.ht.ctypes.data_as(cre.c_float_p),
    cre.uu.ctypes.data_as(cre.c_float_p),
    cre.vv.ctypes.data_as(cre.c_float_p),
    cre.ww.ctypes.data_as(cre.c_float_p),
    cre.div.ctypes.data_as(cre.c_float_p)
    )


