import json
import os
from datetime import datetime

# Constants
folder = 'bookcases'
file = 'bookcases.geojson'
color = '#ff5020'
regions = 'Régions Françaises/'
livres = 'BoiteLire'
horsFrance = 'BoiteLire hors France métro'

def save_file(filepath, content):
    try:
        with open(filepath, 'w+', encoding='utf-8') as f:
            f.write(content)
        print('OK ' + filepath)
    except Exception as err:
        print('KO ' + filepath + ' ' + str(err))

def generate_gpx(features, title):
    header = """<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>
<gpx version="1.1" creator="Binnette" xmlns="http://www.topografix.com/GPX/1/1" xmlns:osmand="https://osmand.net" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd">"""
    footer = f"""  <extensions>
    <osmand:points_groups>
      <group name="{title}" color="{color}" icon="public_bookcase" background="square" />
    </osmand:points_groups>
  </extensions>
</gpx>"""
    content = [header]
    
    for feature in features:
        lat = feature['geometry']['coordinates'][1]
        lon = feature['geometry']['coordinates'][0]
        props = feature['properties']
        date = props.get('date_updated', props.get('date_created', ''))
        time = ''
        if date:
            dt = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            time = dt.strftime("%Y-%m-%dT%H:%M:%SZ")
        name = props.get('nom', '').replace('&', ' et ')
        desc = ' '.join(props.get('remarque', '').replace('&', ' et ').replace('\n', ' ').replace('\r', ' ').split())
        addr = ', '.join(filter(None, [props.get("adresse"), f"{props.get('code_postal')} {props.get('ville')}", props.get("pays")])).replace('&', ' et ')
        name = f"{name.strip()} b{props['id']}".strip()
        
        wpt = f"""  <wpt lat="{lat}" lon="{lon}">
    <time>{time}</time>
    <name>{name}</name>
    <desc>{desc}</desc>
    <type>{title}</type>
    <extensions>
      <osmand:address>{addr}</osmand:address>
      <osmand:color>{color}</osmand:color>
      <osmand:background>square</osmand:background>
      <osmand:icon>public_bookcase</osmand:icon>
    </extensions>
  </wpt>"""
        content.append(wpt)
    
    content.append(footer)
    return '\n'.join(content)

def read_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as err:
        print(err)

main_files = [f for f in os.listdir(folder) if f.endswith('.geojson')]
region_files = [f for f in os.listdir(os.path.join(folder, regions)) if f.endswith('.geojson')]

for file in main_files:
    name = os.path.splitext(file)[0]
    title = livres if name.startswith('bookcases') else horsFrance
    path = os.path.join(folder, file)
    data = read_file(path)
    converted = generate_gpx(data['features'], title)
    gpx_path = os.path.join(folder, f'{name}.gpx')
    save_file(gpx_path, converted)

for file in region_files:
    name = os.path.splitext(file)[0]
    title = f"{livres} {name}"
    data = read_file(os.path.join(folder, regions, file))
    converted = generate_gpx(data['features'], title)
    gpx_path = os.path.join(folder, regions, f'{name}.gpx')
    save_file(gpx_path, converted)

print("Done.")
