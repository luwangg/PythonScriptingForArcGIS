import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise08"
fc = "Hawaii.shp"
newfc = "Results/Hawaii_bounded.shp"
arcpy.MinimumBoundingGeometry_management(fc, newfc, "CONVEX_HULL", "NONE")