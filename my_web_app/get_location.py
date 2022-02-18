def get_loc(finding_location):
    from geopy.geocoders import ArcGIS, Nominatim

    arcgis = ArcGIS(timeout=100)
    nominatim = Nominatim(timeout=100, user_agent='http')
    geocoders = [arcgis, nominatim]

    def geocode(adress):
        try:
            i = 0
            while i < len(geocoders):
                location = geocoders[i].geocode(adress)
                if location is not None:
                    return location.latitude, location.longitude
                else:
                    i += 1
        except:
            return [None, None]
    finaly_location = []
    for loc in finding_location:
        try:
            coord = geocode(loc[0])
            if coord[0] is not None:
                finaly_location.append(((coord[0], coord[1]), loc[1]))
        except:
            1
    return finaly_location
