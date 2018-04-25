import arcpy
from arcpy import env
env.overwriteOutput = True
env.workspace = "C:/EsriPress/Python/Data/Exercise06"
arcpy.CreateFileGDB_management("C:/EsriPress/Python/Data/Exercise06/Results", "NM.gdb")
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    fcdesc = arcpy.Describe(fc)
    arcpy.CopyFeatures_management(fc, "C:/EsriPress/Python/Data/Exercise06/Results/NM.gdb/" + fcdesc.basename)