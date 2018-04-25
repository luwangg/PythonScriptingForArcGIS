import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise07"
infc = "airports.shp"
outfc = "Results/airports_anchorage.shp"
delimitedfield = arcpy.AddFieldDelimiters(infc, "COUNTY")
arcpy.Select_analysis(infc, outfc, delimitedfield + " = 'Anchorage Borough'")