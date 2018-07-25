# K2FootprintFiles

***Machine-readable files that detail the footprints of the K2 Campaign fields on the sky.***

This repository enables users of 
[NASA's K2 mission](http://keplerscience.arc.nasa.gov)
to create custom visualisations of the space telescope's footprint in the sky.

The files in this repository specify the celestial coordinates
of the corners of each CCD channel
in each of the mission's 80-day long campaigns. 
The files also detail observing dates and CCD identifiers.

## JSON and CSV text files

The footprint coordinates are made available in JSON and CSV format
for K2 Campaigns 0 through 20:
 * [json/k2-footprint.json](https://github.com/KeplerGO/K2FootprintFiles/raw/master/json/k2-footprint.json)
 * [csv/k2-footprint.csv](https://github.com/KeplerGO/K2FootprintFiles/raw/master/csv/k2-footprint.csv)

These files were created using `scripts/create-text-files.py`.

## MOC HealPix files

In addition to JSON and CSV files,
this repository also [offers files in the MOC data format](https://github.com/KeplerGO/K2FootprintFiles/tree/master/moc-files).
MOC is a HealPix-based VO standard which can be loaded into [Aladin interactive sky atlas](http://aladin.u-strasbg.fr)
and be used to query remote databases there.

## K2fov dependency

These files are derived entirely from the
[K2fov](https://github.com/KeplerGO/K2fov) tool,
which should be considered to be the authorative tool
for detailing the K2 footprints

## More info

See http://keplerscience.arc.nasa.gov/k2-fields.html#footprint-files
