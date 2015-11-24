# K2FootprintFiles

***Machine-readable files that detail the footprints of the K2 Campaign fields.***

This repository enables users of [NASA's K2 mission](http://keplerscience.arc.nasa.gov)
to create custom visualisations of the space telescope's footprint in the sky.

The files in this repository specify the celestial coordinates of the corners of each CCD
in each of the mission's 80-day long campaigns. 
The files also detail observing dates and CCD identifiers.

## JSON and CSV files

The footprint coordinates are made available in JSON and CSV format
for K2 Campaigns 0 through 13:
 * [k2-footprint.json](https://github.com/KeplerGO/K2FootprintFiles/raw/master/k2-footprint.json)
 * [k2-footprint.csv](https://github.com/KeplerGO/K2FootprintFiles/raw/master/k2-footprint.csv)

The coordinates of Campaigns 14 through 17 have not been fixed at the time of writing
and are certain to be changed slightly based on community feedback.
Their footprints are made available in preliminary files:
 * [k2-footprint-proposed.json](https://github.com/KeplerGO/K2FootprintFiles/raw/master/k2-footprint-proposed.json) (preliminary!)
 * [k2-footprint-proposed.csv](https://github.com/KeplerGO/K2FootprintFiles/raw/master/k2-footprint-proposed.csv) (preliminary!)

## MOC files

In addition to JSON and CSV files,
this repository also [offers files in the MOC data format](https://github.com/KeplerGO/K2FootprintFiles/tree/master/moc-files).
MOC is a HealPix-based VO standard which can be loaded into [Aladin interactive sky atlas](http://aladin.u-strasbg.fr)
and be used to query remote databases there.

## More info

See http://keplerscience.arc.nasa.gov/k2-fields.html#footprint-files

