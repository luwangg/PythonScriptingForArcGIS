import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise09"
arcpy.CreateFileGDB_management("C:/EsriPress/Python/Data/Exercise09/Results", "challenge2.gdb")
rasterlist = arcpy.ListRasters()
for raster in rasterlist:
    desc = arcpy.Describe(raster)
    arcpy.Copy_management(raster, "/results/challenge2.gdb/" + raster)