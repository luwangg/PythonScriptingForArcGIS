import arcpy
mxd = "C:/EsriPress/Python/Data/Exercise10/Austin_TX.mxd"
mapdoc = arcpy.mapping.MapDocument(mxd)
df_1 = arcpy.mapping.ListDataFrames(mapdoc)[0]
df_2 = arcpy.mapping.ListDataFrames(mapdoc)[1]
park_df = arcpy.mapping.ListDataFrames(mapdoc)[2]
park_layer = arcpy.mapping.ListLayers(mapdoc)[-2]
arcpy.mapping.AddLayer(df_1, park_layer, "AUTO_ARRANGE")
arcpy.mapping.AddLayer(df_2, park_layer, "AUTO_ARRANGE")
mapdoc.saveACopy(r"C:/EsriPress/Python/Data/Exercise10/challenge1.mxd")
del mapdoc