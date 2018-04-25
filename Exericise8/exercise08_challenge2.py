import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise08"
fc = "Hawaii.shp"
newfc = "Results/Hawaii_single.shp"
arcpy.MultipartToSinglepart_management(fc, newfc)
spatialref = arcpy.Describe(newfc).spatialReference
unit = spatialref.linearUnitName
cursor = arcpy.da.SearchCursor(newfc, ["SHAPE@"])
for row in cursor:
    print ("Perimeter: {0} square {1}".format(row[0].length, unit))
    print ("Area: {0} square {1}".format(row[0].area, unit))