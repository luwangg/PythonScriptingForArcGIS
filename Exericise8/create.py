import arcpy
import string
import os
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise08"
env.overwriteOutput = True
outpath = "C:/EsriPress/Python/Data/Exercise08"
newfc = "Results/newpolyline.shp"
arcpy.CreateFeatureclass_management(outpath, newfc, "Polyline")
infile = "C:/EsriPress/Python/Data/Exercise08/coordinates.txt"
cursor = arcpy.da.InsertCursor(newfc, ["SHAPE@"])
array = arcpy.Array()
f = open(infile, 'r')
for line in f:
    ID, X, Y = string.split(line, " ")
    array.add(arcpy.Point(X, Y))
cursor.insertRow([arcpy.Polyline(array)])
f.close()
del cursor
