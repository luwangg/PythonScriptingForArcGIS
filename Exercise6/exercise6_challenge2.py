'''Write a script that reads all the feature classes in a personal or file
geodatabase and copies only the polygon feature classes to a new file
geodatabase. You can assume there are no feature datasets in the existing
data, and the feature classes can keep the same name.'''

import arcpy
from arcpy import env
env.overwriteOutput = True
env.workspace = "C:/EsriPress/Python/Data/Exercise06/NM.gdb"
fclist = arcpy.ListFeatureClasses() 
arcpy.CreateFileGDB_management("C:/EsriPress/Python/Data/Exercise06/Results", "NM2.gdb")
for fc in fclist:
    fcdesc = arcpy.Describe(fc)
    if fcdesc.shapeType == "Polygon":
        arcpy.CopyFeatures_management(fc, "C:/EsriPress/Python/Data/Exercise06/Results/NM2.gdb/" + fcdesc.basename)