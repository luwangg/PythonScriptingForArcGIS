import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise07/Results"
env.overwriteOutput = True
fc = "roads.shp"
fieldname = "FERRY"
fieldtype = "TEXT"
arcpy.AddField_management(fc, fieldname, fieldtype, "", "", 20)
delimfield = arcpy.AddFieldDelimiters(fc, "FEATURE")
cursor = arcpy.da.UpdateCursor(fc, ["FEATURE", "FERRY"])
for row in cursor:
    if row[0] == "Ferry Crossing":
        row[1] = "YES"
    else:
        row[1] = "NO"
    cursor.updateRow(row)
del cursor, row