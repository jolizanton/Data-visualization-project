import json
filename = 'data_j/eq_data_1_day_m1.json'
with open (filename) as f:
    all_eq_data=json.load(f)
all_eq_dict=all_eq_data['features']
#print(all_eq_dict)
print(len(all_eq_dict))
#print(len(all_eq_data))

mags=[eq_dict['properties']['mag'] for eq_dict in all_eq_dict]
lons=[eq_dict['geometry']['coordinates'][0] for eq_dict in all_eq_dict]
lats=[eq_dict['geometry']['coordinates'][1] for eq_dict in all_eq_dict]
print (f"Magnitude:{mags}")
print (f"longitude:{lons}")
print (f"latitude:{lats}")

readable_file = 'data_j/readable_eq_data.json'
with open(readable_file,'w') as f:
    json.dump(all_eq_data,f,indent=4)