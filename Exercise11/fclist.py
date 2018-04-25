import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise11"
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    desc = arcpy.Describe(fc)
    print desc.basename + ": " + desc.shapeType