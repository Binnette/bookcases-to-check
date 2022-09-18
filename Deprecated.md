## How to extract and transform data ?

If those data are not enougth fresh, you can make new file "bookcase.gpx" yourself.

### Extract & clean data

1. Go to https://www.boite-a-lire.com/
1. Click on link "**Téléchargez toutes les coordonnées**"
1. Open the CSV with LibreOffice (or anything else)
1. Remove bookcases without no GPS value
1. Remove bookcases with comment like "MAJ : n'existe plus" and so on
1. Repair broken lines (there is some ; in the data)
1. [Not mandatory] Parse GPS in 2 differents columns
1. [Not mandatory] Prepare data:
   * Remove "
   * Remove line with comment "n'existe plus"
1. Save as CSV

### Convert CSV to GPX

1. Go to https://binnette.github.io/bookcases-to-check/bookcase.html
1. Copy CSV content in the input field
1. Click on button "Convert"
1. Wait for the file to be converted
1. Click on button "Copy output to clipboard"
1. Paste it in a new file bookcase.gpx
1. Save the file on your computer

### [Not mandatory] Filter bookcase by french region

1. Open JOSM and import file asset/contours-des-regions-francaises-sur-openstreetmap.geojson
1. Import bookcase.gpx
1. Convert it to OSM data
1. Duplicate this layer for every region
1. Manually remove bookcase for each region

(If someone has a faster way to do it, contact me or create an issue here)