# Name: AddXY_Example2.py
# Description: Adding XY points to the hospital dataset

# Import system modules
import arcpy
from arcpy import env

# Set workspace
env.workspace = "C:/EsriPress/Python/Data/Exercise05"

# Set local variables
in_data= "hospitals.shp"
in_features = "hospitalsXPpts2.shp"

# Copying data to preserve original dataset
# Execute Copy
arcpy.Copy_management(in_data, in_features)

# Execute AddXY
arcpy.AddXY_management(in_features)
