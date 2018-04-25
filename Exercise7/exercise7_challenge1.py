import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise07"
env.overwriteOutput = True

infc = "airports.shp"
airportoutfc = "Results/airports_select.shp"
seaplaneoutfc = "Results/seaplane_select.shp"

delimitedfield = arcpy.AddFieldDelimiters(infc, "FEATURE")
arcpy.Select_analysis(infc, airportoutfc, delimitedfield + " = 'Airport'")
arcpy.Select_analysis(infc, seaplaneoutfc, delimitedfield + " = 'Seaplane Base'")

airportbuffer = "Results/airports_buffer.shp"
seaplanebuffer = "Results/seaplane_buffer.shp"

arcpy.Buffer_analysis(airportoutfc, airportbuffer, "15000 METERS")
arcpy.Buffer_analysis(seaplaneoutfc, seaplanebuffer, "7500 METERS")