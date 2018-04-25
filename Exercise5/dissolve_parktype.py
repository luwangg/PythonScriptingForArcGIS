# Name: dissolve_parktype.py
# Description: Dissolve features based on common attributes

# Import system modules
import arcpy

arcpy.env.workspace = "C:/EsriPress/Python/Data/Exercise05"
 
# Set local variables
inFeatures = "parks.shp"
tempLayer = "parksLyr"
expression = arcpy.AddFieldDelimiters(inFeatures, "PARK_TYPE") + " <> ''"
outFeatureClass = "C:/EsriPress/Python/Data/Exercise05/Results/parks_dissolve.shp"
dissolveFields = ["PARK_TYPE"]
 
# Execute MakeFeatureLayer and SelectLayerByAttribute.  This is only to exclude 
#  features that are not desired in the output.
arcpy.MakeFeatureLayer_management(inFeatures, tempLayer)
arcpy.SelectLayerByAttribute_management(tempLayer, "NEW_SELECTION", expression)
 
# Execute Dissolve using LANDUSE and TAXCODE as Dissolve Fields
arcpy.Dissolve_management(tempLayer, outFeatureClass, dissolveFields, "", 
                          "SINGLE_PART", "DISSOLVE_LINES")
