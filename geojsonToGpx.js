// Parameters
const folder = './2022-09-17/';
const file = 'data.json';

// Constantes
const regions = 'Régions Françaises/';
const livres = 'BoiteLire';
const horsFrance = 'BoiteLire hors France métro';

// Globals
var t;

// Libs
const fs = require('fs');
const path = require('path');


function saveFile(file, content) {
    try {
        fs.writeFileSync(file, content, { flag: 'w+' });
        console.log('OK ' + file)
    } catch (err) {
        console.error('KO ' + file + ' ' + err);
    }
}

function w(line) {
    t += line + '\n';
}

// Write GPX headers
function wHeader() {
    w("<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>");
    w('<gpx version="1.1" creator="Binnette" xmlns="http://www.topografix.com/GPX/1/1" xmlns:osmand="https://osmand.net" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd">');
}

// Write GPX footer
function wFooter(title) {
    w("  <extensions>");
    w("    <osmand:points_groups>");
    w('      <group name="' + title + '" color="#ff5020" icon="public_bookcase" background="square" />');
    w("    </osmand:points_groups>");
    w("  </extensions>");
    w("</gpx>");
}

function clean(text) {
    text = text || '';
    text = text.replace('&',' et ');
    text = text.replace(/\s+/g,' ');
    return text.trim();
}

function getAddr(p) {
    var tab = [];
    var street = p["addr:street"];
    var zip = p["addr:zipcode"];
    var city = p["addr:city"];
    var country = p["addr:country"];
    if (street) {
        tab.push(street);
    }
    if (zip || city) {
        tab.push(zip + ' ' + city);
    }
    if (country) {
        tab.push(country);
    }
    var addr = tab.join(', ');
    return clean(addr);
}

function wBookcase(b, i, title) {
    try {
        var p = b.properties;
        var time = clean(p.updated || p.created);
        var addr = getAddr(p);
        var name = clean("b" + p.id + ' ' + p.note);
        var desc = clean(p.html);
        var lat = b.geometry.coordinates[1];
        var lon = b.geometry.coordinates[0];
        w('  <wpt lat="' + lat + '" lon="' + lon + '">');
        w("    <time>" + time + "</time>");
        w("    <name>" + name + "</name>");
        w("    <desc>" + desc + "</desc>");
        w("    <type>" + title + "</type>");
        w("    <extensions>");
        w("      <osmand:address>" + addr + "</osmand:address>");
        w("      <osmand:icon>public_bookcase</osmand:icon>");
        w("      <osmand:background>square</osmand:background>");
        w("      <osmand:color>#ff5020</osmand:color>");
        w("    </extensions>");
        w("  </wpt>");
    } catch (err) {
        console.error(err);
        return;
    }
}

function convert(geo, title) {
    var count = geo.features.length;
    console.log('Converting ' + count + ' features...')

    // reset content
    t = '';
    wHeader();

    for (var i = 0; i < count; i++) {
        var boite = geo.features[i];
        wBookcase(boite, i, title);
    }

    wFooter(title);

    return t;
}

function readFile(file) {
    try {
        const data = fs.readFileSync(file);
        return JSON.parse(data);
    } catch (err) {
        console.error(err);
    }        
}

var mainFiles = fs.readdirSync(folder).filter(f => f.endsWith('.geojson'));
var regionFiles = fs.readdirSync(folder + regions).filter(fn => fn.endsWith('.geojson'));

mainFiles.forEach(function(file) {
    var name = path.basename(file, '.geojson');
    var title = name.startsWith('bookcase') ? livres : horsFrance 
    var data = readFile(folder + file);
    var converted = convert(data, title);
    var gpxPath = folder + name + '.gpx';
    saveFile(gpxPath, converted);
});

regionFiles.forEach(function(file) {
    var name = path.basename(file, '.geojson');
    var title = livres + " " + name;
    var data = readFile(folder + regions + file);
    var converted = convert(data, title);
    var gpxPath = folder + regions + name + '.gpx';
    saveFile(gpxPath, converted);
});

console.log("Done.")