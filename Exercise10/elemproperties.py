import arcpy
mxd = "C:/EsriPress/Python/Data/Exercise10/Georgia.mxd"
mapdoc = arcpy.mapping.MapDocument(mxd)
elemlist = arcpy.mapping.ListLayoutElements(mapdoc)
title = elemlist[0]
title.text = "Housing Vacancy for Georgia Countries (2000)"
mapdoc.save()
del mapdoc