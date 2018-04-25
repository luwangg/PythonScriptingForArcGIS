import arcpy
import os
def countstringfields(fc):
    fields = arcpy.ListFields(fc)
    counter = 0
    for field in fields:
        if field.type == "String":
            counter += 1
    return counter