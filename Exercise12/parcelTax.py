import parcelclass
fc = "C:/EsriPress/Python/Data/Exercise12/parcels.shp"
cursor = arcpy.SearchCursor(fc)
for row in cursor:
    fid = row.getValue("FID")
    landuse = row.getValue("Landuse")
    value = row.getValue("Value")
    parcel = parcelclass.Parcel(landuse, value)
    print str(fid)+ ": " + str(parcel.assessment())
del row
del cursor