# check_extensions.py checks if ArcGIS 3D Analyst, ArcGIS Network Analyst, and ArcGIS Spatial Analyst are available.

import arcpy

extensions = ["3D", "Network", "Spatial"]

print "The following extensions are available: ..."

for extension in extensions:
    if arcpy.CheckExtension(extension):
        print(extension)