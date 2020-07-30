import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data_j/world_fires_7_day.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    first_row=next(reader)

    print (header_row)
    print (first_row)
    for index, column_header in enumerate(header_row):
       print (index, column_header)

    #Get
    brightness,lats,lons=[],[],[]
    for row in reader:
        bright=float(row[header_row.index('bright_ti4')])
        brightness.append(bright)
        lat=float(row[header_row.index('latitude')])
        lats.append(lat)
        lon = float(row[header_row.index('longitude')])
        lons.append(lon)
    print (brightness)
    print (lats)
    print (lons)



# Map
my_data= [{
    'type': 'scattergeo',
    'lon':lons,
    'lat':lats,
    'marker': { 'size': [0.07*bright for bright in brightness],
                'color': brightness,
                'colorscale': 'Viridis',
                'reversescale': True,
                'colorbar': {'title': 'Magnitude'}
                }

}]
my_layout = Layout(title="World fires")
fig = {'data': my_data, 'layout': my_layout}
offline.plot(fig, filename='world fires.html')











