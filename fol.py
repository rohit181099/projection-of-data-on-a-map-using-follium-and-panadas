import folium
import pandas as pd
from folium.features import DivIcon

new = pd.read_csv("cities.csv.csv",sep="\t")
m = folium.Map(location=[12.9716, 77.5946],zoom_start=4)

for val in new.iloc[:,1:].values:
    folium.Marker(
    location=val[:-1],
    icon=folium.Icon(color="red",icon_color='white', icon='car', prefix='fa')
    ).add_to(m)
    
    folium.CircleMarker(
    location=val[:-1],
    radius=20,
    color='#3186cc',
    fill=True,
    fill_color='#3186cc'
    ).add_to(m)
    
    folium.Marker(val[:-1], icon=DivIcon(
            icon_size=(150,36),
            icon_anchor=(7,20),
            html=f'<div style="font-size: 9pt; color : black">{val[-1]}</div>',
            )).add_to(m)




m.save("data.html")
