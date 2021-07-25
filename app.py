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
    zoom_start=3, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="Volcanoes map")

for lt, ln, nm, cn, d in zip(lat, long, name, country, deaths):
    fg.add_child(
        folium.Marker(
            location=[lt, ln],
            popup=nm + ' ' + cn, icon=folium.Icon(color=color_marker(d))))

json_file = open("world.json", 'r', encoding="utf-8-sig").read()


def style_lambda(x): return{
    "fillColor": "green"
    if x["properties"]["POP2005"] < 10000000 else "orange"
    if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"}


fg.add_child(
    folium.GeoJson(
        data=json_file, style_function=style_lambda))

map.add_child(fg)
map.save("Volcanoes_and_Population.html")
