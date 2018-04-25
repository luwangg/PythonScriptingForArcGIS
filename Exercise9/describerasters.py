import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise09"
raster = "landcover.tif"
desc = arcpy.Describe(raster)
x = desc.meanCellHeight
y = desc.meanCellWidth
spatialref = desc.spatialReference
units = spatialref.linearUnitName
print "The raster resolution is " + str(x) + " by " + str(y) + " " + units + "."
