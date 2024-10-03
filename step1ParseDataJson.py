import json
import os

# Define the folder and file path
folder_path = "2024-10-03"
file_path = os.path.join(folder_path, "data.json")

# Read the JSON file
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Sort data by id in descending order
data.sort(key=lambda x: x["id"], reverse=True)

# Log the number of objects in the JSON array
num_objects = len(data)
print(f"Starting conversion.")
print(f"Number of objects in JSON array: {num_objects}")

# Initialize GeoJSON structures
geojson = {
    "type": "FeatureCollection",
    "features": []
}
duplicates_geojson = {
    "type": "FeatureCollection",
    "features": []
}

# Check for duplicates and convert to GeoJSON
seen_coordinates = set()

def create_feature(item):
    coordinates = tuple(map(float, item["coord_gps"].split(',')))
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [coordinates[1], coordinates[0]]
        },
        "properties": {
            "id": item["id"],
            "nom": item["nom"],
            "adresse": item["adresse"],
            "code_postal": item["code_postal"],
            "ville": item["ville"],
            "pays": item["pays"],
            "creditimage": item["creditimage"],
            "email": item["email"],
            "image": item["image"],
            "image_admin": item["image_admin"],
            "remarque": item["remarque"],
            "affichage": item["affichage"],
            "date_created": item["date_created"],
            "date_updated": item["date_updated"]
        }
    }

for item in data:
    coordinates = tuple(map(float, item["coord_gps"].split(',')))
    feature = create_feature(item)
    if coordinates in seen_coordinates:
        duplicates_geojson["features"].append(feature)
    else:
        seen_coordinates.add(coordinates)
        geojson["features"].append(feature)

# Save the GeoJSON to a file
output_file_path = os.path.join(folder_path, "bookcases.geojson")
with open(output_file_path, 'w', encoding='utf-8') as file:
    json.dump(geojson, file, ensure_ascii=False, indent=4)

# Save duplicates to a separate GeoJSON file
duplicates_file_path = os.path.join(folder_path, "duplicates.geojson")
with open(duplicates_file_path, 'w', encoding='utf-8') as file:
    json.dump(duplicates_geojson, file, ensure_ascii=False, indent=4)

# Log the final number of bookcases parsed
print(f"GeoJSON file has been created at {output_file_path}")
print(f"Number of bookcases parsed: {len(geojson['features'])}")
print(f"Number of duplicates found: {len(duplicates_geojson['features'])}")

# Additional console logs
print(f"# Total: {num_objects}")
print(f"# Uniques: {len(geojson['features'])}")
print(f"# Duplicates: {len(duplicates_geojson['features'])}")
print("Done.")
