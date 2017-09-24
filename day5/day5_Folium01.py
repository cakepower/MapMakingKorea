#!__*__coding:utf-8__*__

import folium

my_map = folium.Map(location=[45.0000, -122.0000])
print(dir(my_map))

x = folium.Marker([45.1000, -122.2000], popup="한글")
x.add_to(my_map)

my_map.save("map_output.html")
