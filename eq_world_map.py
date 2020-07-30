import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data_j/eq_data_30_day_m1.json'
with open (filename) as f:
    all_eq_data=json.load(f)
all_eq_dict=all_eq_data['features']
#print(all_eq_dict)
print(len(all_eq_dict))
#print(len(all_eq_data))

mags=[eq_dict['properties']['mag'] for eq_dict in all_eq_dict]
lons=[eq_dict['geometry']['coordinates'][0] for eq_dict in all_eq_dict]
lats=[eq_dict['geometry']['coordinates'][1] for eq_dict in all_eq_dict]
hover_texts=[eq_dict['properties']['title'] for eq_dict in all_eq_dict]
print (f"Magnitude:{mags}")
print (f"longitude:{lons}")
print (f"latitude:{lats}")

#Map
#my_data=[Scattergeo(lon=lons,lat=lats)]
my_data=[{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text':hover_texts,
    'marker':{
        'size':[5*(eq_dict['properties']['mag']) for eq_dict in all_eq_dict],
        'color': mags,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title': 'Magnitude'}
    }
}]
#my_layout=Layout(title='Global Earthquakes')
my_layout=Layout(title= all_eq_data['metadata']['title'])
fig={'data':my_data,'layout':my_layout}
offline.plot(fig,filename='global_earthquakes.html')
