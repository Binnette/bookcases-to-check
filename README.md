## Summary
In this repository, you will find "public bookcases" exported from website: https://www.boite-a-lire.com/

Note: boite-a-lire.com publish those data under [CC-BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/2.0/) license.

Those bookcases are mainly located in France and french speaking countries. You can display them in OsmAnd, JOSM, uMap etc.

### View all bookcases (OSM + boite-a-lire.com)

[Map of OSM bookcases and 2020-09-28 dataset](http://u.osmfr.org/m/394538/)

In this map:
- OSM bookcases are displayed in **green** ![](https://placehold.it/12/32CD32/000000?text=+) on zoom 14+ with 1 hour cache
- boite-a-lire.com bookcases are displayed in **red** ![](https://placehold.it/12/DC143C/000000?text=+)


### View only boite-a-lire.com

You can view all bookcases from those data here: 

|Date      |Bookcases|Map                                       |
|----------|---------|------------------------------------------|
|2020-09-28|6740     |[Map with 2020-09-28 data](https://umap.openstreetmap.fr/en/map/public-bookcases-from-boite-a-lirecom-2020-09-28_504237)|
|2019-12-01|5551     |[Map with 2019-12-01 data](https://umap.openstreetmap.fr/en/map/public-bookcases-from-boite-a-lirecom-2019-12-01_394535)|
|2019-09-07|5206     |[Map with 2019-09-07 data](https://umap.openstreetmap.fr/fr/map/public-bookcases_362282#6/46.606/3.889)|
|2019-05-27|4795     |[Map with 2019-05-27 data](https://umap.openstreetmap.fr/fr/map/2019-05-27-public-bookcases_362245#6/46.606/3.889)|

### Repo hierarchy

- **YYYY-MM-DD**: date I export data from the website.
  - **bookcase.gpx**: file to use in OsmAnd, JOSM, etc.
  - **bookcases_from_website.csv**: file from website.
  - **bookcases_from_website_fixed.csv**: manualy refined data, I fixed some errors.

## WARNING !!! DO NOT IMPORT IN OPENSTREETMAP !!!

:warning: **DO NOT IMPORT THOSE DATA IN OPENSTREETMAP !!!** :warning:

Those "*supposed bookcases*" needs to be checked by a survey **in real life**, on the field.

You need to go on each "*supposed bookcases*", **check if it exists**, then you can add this bookcase in OSM.

## How to use data ?

The main goal of those data is to find potential bookcases.
So you can grab/exchange some books.
You may also want to use those data to improve OpenStreetMap.
But you need to check if those bookcases exists in real life before adding it in OpenStreetMap

### With OsmAnd ?

NB: i do not recommand to import the whole file "bookcase.gpx" because OsmAnd will become lagguy. Instead use the gpx in "Régions Françaises" folder.

1. Download bookcase.gpx from the latest export
1. Copy bookcase.gpx to your device
1. Open OsmAnd on your device
1. Go to Favorites
1. Use the button **+** (import button)
1. Select file bookcase.gpx
1. It's done, bookcases are displayed on the map

<img alt="Bookcases in OsmAnd" src="/assets/OsmAnd.png" height="30%" width="30%">

### With JOSM ?

1. Download bookcase.gpx from the latest export
1. Use button Open File in JOSM
1. Select file bookcase.gpx
1. It's done, bookcase are displayed on the map

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

## Stats

|Date      |Bookcases|Bookcase without description|
|----------|---------|----------------------------|
|2020-09-28|     6740|                        1093|    
|2019-12-01|     5551|                         919|
|2019-09-07|     5206|                         842|
|2019-05-27|     4795|                         764|

## Stats by region 2019-12-01

|Region                 |Bookcases|
|-----------------------|---------|
|France                 |     5291|
|Nouvelle Aquitaine     |      871|
|Ile de France          |      671|
|Auvergne Rhone-Alpes   |      646|
|Grand Est              |      448|
|Occitanie              |      436|
|Hauts de France        |      361|
|Pays de la Loire       |      361|
|Bretagne               |      359|
|Normandie              |      311|
|Centre Val de Loire    |      300|
|Bourgogne Franche-Comte|      288|
|PACA                   |      240|
|Corse                  |        9|


NB: I duplicate some bookcases on boundaries.
