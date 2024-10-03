#sudo apt install python3-gpxpy python3-shapely
#pip install shapely
import os
import json
from shapely.geometry import shape, Point, LineString, Polygon

# Paths to the input files
regions_file_path = 'assets/georef-france-region-custom.geojson'
folder = '2024-10-03'
bookcases_file_path = f'{folder}/bookcases.geojson'

# Load the regions data
with open(regions_file_path, 'r', encoding='utf-8') as f:
    regions_data = json.load(f)

# Load the bookcases data
with open(bookcases_file_path, 'r', encoding='utf-8') as f:
    bookcases_data = json.load(f)

# Create the output directory inside folder
output_dir = f'{folder}/Régions Françaises'
os.makedirs(output_dir, exist_ok=True)

# Function to convert LineString to Polygon
def linestring_to_polygon(linestring):
    coords = linestring['coordinates']
    if coords[0] != coords[-1]:
        coords.append(coords[0])  # Close the loop if not already closed
    return Polygon(coords)

# Function to check if a point is inside a region
def is_point_in_region(point, region):
    if region['geometry']['type'] == 'LineString':
        region_shape = linestring_to_polygon(region['geometry'])
    else:
        region_shape = shape(region['geometry'])
    return region_shape.contains(point)

# List to hold bookcases not in any region
out_of_region_bookcases = {
    "type": "FeatureCollection",
    "features": []
}

total_bookcases = len(bookcases_data['features'])

# Process each region
for region in regions_data['features']:
    region_name = region['properties']['reg_name']

    # Filter bookcases inside the region
    filtered_bookcases = {
        "type": "FeatureCollection",
        "features": []
    }
    for bookcase in bookcases_data['features']:
        point = Point(bookcase['geometry']['coordinates'])
        if is_point_in_region(point, region):
            filtered_bookcases['features'].append(bookcase)

    # Print the number of bookcases in the region
    print(f"Region: {region_name}, Bookcases: {len(filtered_bookcases['features'])}")

    # Export to .geojson
    geojson_output_path = os.path.join(output_dir, f'{region_name}.geojson')
    with open(geojson_output_path, 'w', encoding='utf-8') as f:
        json.dump(filtered_bookcases, f, ensure_ascii=False, indent=4)

# Check each bookcase to see if it is in any region
for bookcase in bookcases_data['features']:
    point = Point(bookcase['geometry']['coordinates'])
    in_any_region = False
    for region in regions_data['features']:
        if is_point_in_region(point, region):
            in_any_region = True
            break
    if not in_any_region:
        out_of_region_bookcases['features'].append(bookcase)

# Export out-of-region bookcases to .geojson
out_geojson_output_path = f'{folder}/out-france-metro.geojson'
with open(out_geojson_output_path, 'w', encoding='utf-8') as f:
    json.dump(out_of_region_bookcases, f, ensure_ascii=False, indent=4)

# Print the bookcases that are out of any region
print(f"Out of region bookcases: {len(out_of_region_bookcases['features'])}")

# Print the bookcase that are in any region
print(f"In region bookcases: {total_bookcases - len(out_of_region_bookcases['features'])}")

# Print the total number of bookcases
print(f"Total bookcases: {total_bookcases}")

print("Processing complete!")
