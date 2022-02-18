def build(locations):
    import folium
    map = folium.Map()
    # map = folium.Map(tiles="Stamen Terrain")
    users_location_fg = folium.FeatureGroup(name="Location map")
    for i in locations:
        users_location_fg.add_child(folium.Marker(location=[i[0][0], i[0][1]],
                                                  popup=i[1],
                                                  icon=folium.Icon(color='blue')))

    map.add_child(users_location_fg)
    map.add_child(folium.LayerControl())
    return map
