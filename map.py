import folium
import pandas

data = pandas.read_csv("location1.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
det = list(data["details"])

def color_producer(details): #image will be here too
	if details ==1 :
		return 'lightblue'
	elif details ==2:
		return 'blue'
	else:
		return 'darkblue'

html = """<h4> City Information </h4>
Height: %s m
"""

map = folium.Map(location=[38.58, -99.09], zoom_start=4, tiles="Stamen Terrain")

fgc = folium.FeatureGroup(name="Cities")


for lt, ln, de in zip(lat, lon, det): 

#Cities I have been too function
	iframe = folium.IFrame(html=html % str(de), width=1000, height=1000)   #image will be here // Now a circle but expect to have png images//
	fgc.add_child(folium.CircleMarker(
	location=[lt,ln],
	popup=str(de)+" time(s) in that city?",
	color=color_producer(de),
	radius= 20,
	fill = True)) 

#Population of every country in the world
fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig').read(), #adds segmentation lines
style_function=lambda x: {'fillColor':'red'
if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] <50000000
else 'pink' if 50000000 <= x['properties']['POP2005'] <100000000
else 'green' if 100000000 <= x['properties']['POP2005'] <200000000
else 'blue'})) #color



map.add_child(fgc)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")

