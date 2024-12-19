import json
import os
from datetime import datetime

# Get the current date
current_date = datetime.now().strftime("%Y-%m-%d")
folder = current_date
file = 'bookcases.geojson'
color = '#ff5020'

# Constants
regions = 'Régions Françaises/'
livres = 'BoiteLire'
horsFrance = 'BoiteLire hors France métro'

# Globals
t = ''

def save_file(file, content):
    try:
        with open(file, 'w+', encoding='utf-8') as f:
            f.write(content)
        print('OK ' + file)
    except Exception as err:
        print('KO ' + file + ' ' + str(err))

def w(line):
    global t
    t += line + '\n'

# Write GPX headers
def w_header():
    w("<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>")
    w('<gpx version="1.1" creator="Binnette" xmlns="http://www.topografix.com/GPX/1/1" xmlns:osmand="https://osmand.net" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd">')

# Write GPX footer
def w_footer(title):
    w(f'  <extensions>')
    w(f'    <osmand:points_groups>')
    w(f'      <group name="{title}" color="{color}" icon="public_bookcase" background="square" />')
    w(f'    </osmand:points_groups>')
    w(f'  </extensions>')
    w(f'</gpx>')

def clean(text):
    text = text or ''
    text = text.replace('&', ' et ')
    text = ' '.join(text.split())
    return text.strip()

def get_addr(p):
    tab = []
    street = p.get("adresse")
    zip_code = p.get("code_postal")
    city = p.get("ville")
    country = p.get("pays")
    if street:
        tab.append(street)
    if zip_code or city:
        tab.append(f'{zip_code} {city}')
    if country:
        tab.append(country)
    addr = ', '.join(tab)
    return clean(addr)

def w_bookcase(b, i, title):
    try:
        lat = b['geometry']['coordinates'][1]
        lon = b['geometry']['coordinates'][0]
        p = b['properties']
        # convert string time like "2024-08-20 09:54:49" to string time like "2024-08-20T09:54:49Z"
        date = p.get('date_updated')
        if date is None:
            date = p.get('date_created')
        if date is None:
            time = ''
        else:
            dt = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            time = dt.strftime("%Y-%m-%dT%H:%M:%SZ")

        name = clean(f"{p['nom']} b{p['id']}")
        desc = clean(f"{p['remarque']}")
        addr = get_addr(p)

        w(f'  <wpt lat="{lat}" lon="{lon}">')
        w(f'    <time>{time}</time>')
        w(f'    <name>{name}</name>')
        w(f'    <desc>{desc}</desc>')
        w(f'    <type>{title}</type>')
        w(f'    <extensions>')
        w(f'      <osmand:address>{addr}</osmand:address>')
        w(f'      <osmand:color>{color}</osmand:color>')
        w(f'      <osmand:background>square</osmand:background>')
        w(f'      <osmand:icon>public_bookcase</osmand:icon>')
        w(f'    </extensions>')
        w(f'  </wpt>')
    except Exception as err:
        print(err)

def convert(geo, title):
    global t
    count = len(geo['features'])
    print(f'Converting {count} features...')

    # reset content
    t = ''
    w_header()

    for i, boite in enumerate(geo['features']):
        w_bookcase(boite, i, title)

    w_footer(title)

    return t

def read_file(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
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
    converted = convert(data, title)
    gpx_path = os.path.join(folder, f'{name}.gpx')
    save_file(gpx_path, converted)

for file in region_files:
    name = os.path.splitext(file)[0]
    title = f"{livres} {name}"
    data = read_file(os.path.join(folder, regions, file))
    converted = convert(data, title)
    gpx_path = os.path.join(folder, regions, f'{name}.gpx')
    save_file(gpx_path, converted)

print("Done.")
