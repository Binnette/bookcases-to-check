## Summary
In this repository, you will find "public bookcases" exported from website : https://www.boite-a-lire.com/

Those bookcases are mainly located in France and french speaking countries. You can display those bookcases in OsmAnd, JOSM, etc.

### View data online
You can view all bookcases from those data here : 

https://umap.openstreetmap.fr/fr/map/2019-05-27-public-bookcases_362245#6/46.314/3.955

### Repo hierarchy
- **YYYY-MM-DD** : date I export data from the website.
  - **bookcase.gpx** : file to use in OsmAnd, JOSM, etc.
  - **bookcases_from_website.csv** : file from website.
  - **bookcases_from_website_fixed.csv** : manualy refined data, I fixed some errors.

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

1. Download bookcase.gpx from the latest export.
1. Copy bookcase.gpx to your device
1. Open OsmAnd on your device
1. Go to Favorites
1. Use the button **+** (import button)
1. Select file bookcase.gpx
1. It's done, bookcases are displayed on the map.

<img alt="Bookcases in OsmAnd" src="/assets/OsmAnd.png" height="30%" width="30%">

### With JOSM ?

1. Download bookcase.gpx from the latest export.
1. Use button Open File in JOSM
1. Select file bookcase.gpx
1. It's done, bookcase are displayed on the map.

## How to extract and transform data ?

If those data are not enougth fresh, you can make new file "bookcase.gpx" yourself.

1. Go to https://www.boite-a-lire.com/
1. Click on link "**Téléchargez toutes les coordonnées**"
1. Go to https://binnette.github.io/bookcases-to-check/bookcase.html
1. Copy CSV content in the input field
1. Click on button "Convert"
1. Wait for the file to be converted
1. Click on button "Copy output to clipboard"
1. Paste it in a new file bookcase.gps
1. Save the file on your computer
1. It's done.

## Stats
|Date      |Bookcases|Bookcase without description|
|----------|---------|----------------------------|
|2019-05-27|4795     |764                         |
|2019-09-07|5206     |842                         |

