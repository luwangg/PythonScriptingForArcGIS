'''Write a script that reads all the feature classes in a workspace and prints
the name of each feature class and the geometry type of that feature
class in the following format:
streams is a point feature class'''

import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise06"
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    fcdescribe = arcpy.Describe(fc)
    print "Name: " + fcdescribe.name
    print "Geometry type: " + fcdescribe.shapeType