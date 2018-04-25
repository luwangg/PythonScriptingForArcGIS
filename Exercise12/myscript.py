import arcpy
import list
arcpy.env.workspace = "C:/EsriPress/Python/Data/Exercise12"
fields = list.listfieldnames("streets.shp")
print fields