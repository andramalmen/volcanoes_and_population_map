import folium
import pandas
import numpy as np


data = pandas.read_csv("volcano_data_2010.csv")
lat = list(data["Latitude"])
long = list(data["Longitude"])
name = list(data["Name"])
country = list(data["Country"])
deaths = list(data["TOTAL_DEATHS"])


def color_marker(d):
    if np.isnan(d):
        return "green"
    elif d <= 10:
        return "red"
    return "darkred"


map = folium.Map(
    location=[60.135115711989656, 24.431788098341286],
    zoom_start=2, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="Volcanoes map")

for lt, ln, nm, cn, d in zip(lat, long, name, country, deaths):
    fg.add_child(
        folium.Marker(
            location=[lt, ln],
            popup=nm + ' ' + cn, icon=folium.Icon(color=color_marker(d))))

map.add_child(fg)
map.save("Volcanoes.html")
