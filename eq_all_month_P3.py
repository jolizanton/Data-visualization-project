import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data_j/1.0_week.json'
with open (filename) as f:
    all_eq_data=json.load(f)

all_eq_dict=all_eq_data['features']
print(len(all_eq_dict))

mags=[(eq_dict['properties']['mag']) for eq_dict in all_eq_dict]
lons=[eq_dict['geometry']['coordinates'][0] for eq_dict in all_eq_dict]
lats=[eq_dict['geometry']['coordinates'][1] for eq_dict in all_eq_dict]
hover_texts=[eq_dict['properties']['title'] for eq_dict in all_eq_dict]
print (f"Magnitude:{mags}")
print (f"longitude:{lons}")
print (f"latitude:{lats}")

#Map
my_data=[{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text':hover_texts,
    'marker':{
        'size':[5*(abs(eq_dict['properties']['mag'])) for eq_dict in all_eq_dict],
        'color': mags,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title': 'Magnitude'}
    }
}]
my_layout=Layout(title= all_eq_data['metadata']['title'])
fig={'data':my_data,'layout':my_layout}
offline.plot(fig,filename='1.0_week.html')
