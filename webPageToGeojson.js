/*
 * This script create a geojson out of all bookcase json lines
 * Visit https://www.boite-a-lire.com/ and wait until the map is fully loaded
 * Save the web page on your desktop. Search inside for "var json"
 * Grab those lines and put them behind in the "var data" by following the example
 * Then run this script in nodejs to create bookcase.geojson
 */
const fs = require('fs');
const { convert } = require('html-to-text');

// Parameters
const folder = "./2022-09-17/"

// This function get rid of " and html markup. So it keep only the text
function getText(toConvert) {
    toConvert = toConvert || "";
    toConvert = toConvert.replaceAll('"', '');
    var text = convert(toConvert, { wordwrap: false });
    text = text.replaceAll('Dénichée par :', 'Par ');
    text = text.replaceAll('Crédit photo :', '©');
    text = text.replaceAll('. . .', '');
    text = text.replace(/\s+/g, ' ');
    return text.trim();
}

function saveFile(file, content, nb) {
    try {
        fs.writeFileSync(file, content, { flag: 'w+' });
        console.log('OK ' + file + ' ' + nb + ' features')
    } catch (err) {
        console.error('KO ' + file + ' ' + err);
    }
}

function convertAndSave(data, filename) {
    var count = data.length;
    console.log('Converting...');

    // Create default geojson object structure
    var geo = {
        "type": "FeatureCollection",
        "features": []
    };

    // Loop through all the bookcase
    for (var i = 0; i < count; i++) {
        var b = data[i];
        var coord = b.coord_gps.split(",");
        var id = parseFloat(b.id);
        var lon = parseFloat(coord[0]);
        var lat = parseFloat(coord[1]);
        // Create the geojson feature
        var f = {
            "type": "Feature",
            "properties": {
                "id": getText(b.id),
                "name": getText(b.nom),
                "html": getText(b.html),
                "img": b.image || "",
                "imgAdmin": b.image_admin || "",
                "email": b.email || "",
                "addr:street": getText(b.adresse),
                "addr:zipcode": getText(b.code_postal),
                "addr:city": getText(b.ville),
                "addr:country": getText(b.pays),
                "note": getText(b.remarque),
                "created": getText(b.date_created),
                "updated": getText(b.date_updated),
                "credit": getText(b.creditimage),
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    lat, lon
                ]
            }
        };
        // Adding the feature in the geojson object
        geo.features.push(f);
    }

    // Convert the geojson object to string
    var txt = JSON.stringify(geo, null, 4);

    saveFile(folder + filename + ".geojson", txt, count);
}

var data = require(folder + 'data.json');

console.log("Sort data...");
// sort by id desc
data = data.sort(function (a, b) { return parseInt(b.id) - parseInt(a.id) });

// remove duplicates
var coords = [];
var duplicates = [];
var uniques = [];

for (var i = 0; i < data.length; i++) {
    var cur = data[i];
    var curCoords = cur.coord_gps.replaceAll(' ', '');
    if (coords.includes(curCoords)) {
        // This is a duplicate!
        duplicates.push(cur);
    } else {
        // Not a duplicate
        uniques.push(cur);
        coords.push(curCoords);
    }
}

console.log("# Total: " + data.length);
console.log("# Uniques: " + uniques.length);
convertAndSave(uniques, "bookcase");
console.log("");

console.log("# Duplicates: " + duplicates.length);
convertAndSave(duplicates, "duplicates");
console.log("Done.");