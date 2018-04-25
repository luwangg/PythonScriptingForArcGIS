import arcpy
import string
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise08"
env.overwriteOutput = True
outpath = "C:/EsriPress/Python/Data/Exercise08"
newfc = "Results/newpolygon.shp"
arcpy.CreateFeatureclass_management(outpath, newfc, "Polygon")
coords = [(0, 0), (0, 1000), (1000,1000), (1000, 0)]
cursor = arcpy.da.InsertCursor(newfc, ["SHAPE@"])
array = arcpy.Array()
for x, y in coords:
    array.add(arcpy.Point(x, y)
cursor.insertRow([arcpy.Polygon(array)])
del cursor