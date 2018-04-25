import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/EsriPress/Python/Data/Exercise09"
elev = arcpy.Raster("elevation")
lc = arcpy.Raster("landcover.tif")
if arcpy.CheckExtension("spatial") == "Available":
    arcpy.CheckOutExtension("spatial")
    slope = Slope(elev)
    aspect = Aspect(elev)
    goodslope = ((slope > 5) & (slope < 20))
    goodaspect = ((aspect > 150) & (aspect < 270))
    goodlandcover = ((lc== 41) | (lc ==42 ) | (lc == 43))
    goodfinal = (goodslope & goodaspect & goodlandcover)
    goodfinal.save("challenge1")
    arcpy.CheckInExtension("spatial")
else:
    print "Spatial Analyst license is not available."
