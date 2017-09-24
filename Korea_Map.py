#!__*__coding:utf-8__*__
import folium
import csv
import pandas as pd

state_geo = r'.\data\seoul_municipalities_geo_simple.json'
state_umemployment = r'.\data\US_Unemployment_Oct2012.csv'

state_data = pd.read_csv(state_umemployment)

map = folium.Map(location=[37.5666, 126.97], zoom_start=12, tiles="Stamen Toner")
#folium.Marker([37.5666, 126.97],popup='Test',icon=folium.Icon(color='blue',icon='info-sign')).add_to(map)


map.choropleth(geo_data=state_geo, data=state_data,
               columns=['State','Unemployment'],
               key_on = 'feature.properties.SIG_CD',
               fill_color = 'YlGn', fill_opacity=0.7, line_opacity=0.2,
               legend_name='Unemployment Rate (%)')

file = open(".\\data_shop\\상가업소_201706_01.csv")
csv_reader = csv.reader(file)

for i in csv_reader:
    longitude = i[-2]
    latitude = i[-1]
    name = i[1]
    if name.find("스타벅스") >=0 :
        x = folium.Marker([float(latitude), float(longitude)], popup=name, icon=folium.Icon(color='blue',icon='coffee', prefix='fa'))
        x.add_to(map)

map.save(".\\data\\Korea_Seoul_03.html")

