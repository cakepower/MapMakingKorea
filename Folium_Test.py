#!__*__coding:utf-8__*__
import folium
import csv
import pandas as pd

state_geo = r'.\data\us-states.json'
state_umemployment = r'.\data\US_Unemployment_Oct2012.csv'

state_data = pd.read_csv(state_umemployment)

map = folium.Map(location=[48, -102], zoom_start=3, tiles="Stamen Toner")
folium.Marker([48, -102],popup='Test',icon=folium.Icon(color='blue',icon='info-sign')).add_to(map)
map.choropleth(geo_data=state_geo, data=state_data,
               columns=['State','Unemployment'],
               key_on = 'feature.id',
               fill_color = 'BuPu', fill_opacity=0.7, line_opacity=0.2,
               legend_name='Unemployment Rate (%)')

map.save(".\\data\\unemployment.html")


"""
my_map = folium.Map(location=[37.5666, 126.97], zoom_start=12, tiles="Stamen Toner")
print(dir(my_map))

x = folium.Marker([37.5666, 126.95000], popup="한글", icon=folium.Icon(color='red', icon='info-sign'))
x.add_to(my_map)

y = folium.Marker([38.5666, 127.85000], icon=folium.Icon(color='blue', icon='bath'))
y.add_to(my_map)

my_map.save(".\\data\\map_output01.html")


file = open(".\\data\\aaa.csv")
file = open("C:\\Users\\cakepower\\Downloads\\data_shop\\상가업소_201706_01.csv")
csv_reader = csv.reader(file)

for i in csv_reader:
    longitude = i[-2]
    latitude = i[-1]
    name = i[1]
    #print(longitude)
    if name.find("스타벅스") >=0 :
        x = folium.Marker([float(latitude), float(longitude)], popup=name)
        x.add_to(my_map)

my_map.save("map_output_스타벅스.html")
"""