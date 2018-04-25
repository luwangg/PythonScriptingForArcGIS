import arcpy
arcpy.env.workspace = "C:/EsriPress/Python/Data/Exercise02"
arcpy.Clip_analysis("lakes.shp", "basin.shp", "results/lakes_myClip.shp")
