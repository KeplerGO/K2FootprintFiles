# Simbad catalog of candidate K2 targets

The file `K2-C9-C18-Simbad.xml.gz` in this directory is a VOTable
that lists all the [SIMBAD](http://simbad.u-strasbg.fr/simbad/) entries that will lie on Silicon 
in Campaigns 9 through 18, i.e. for which pixel masks can be
requested via calls for proposals or Director's Discretionary Time (DDT).

### Contents
The table details Simbad IDs, coordinates, magnitudes, [object types](http://simbad.u-strasbg.fr/simbad/sim-display?data=otypes),
spectral types, proper motions, citation counts, and campaign numbers.

### Usage
We recommend using [TopCat](http://www.star.bristol.ac.uk/~mbt/topcat/)
or [AstroPy](http://www.astropy.org)'s `Table.read()` to inspect the table.

### Caveats
* Objects on or near the edges of CCD detectors have been included in this catalog,
eventhough they may not be observable (depending on their brightness i.e. mask size required).
* The positions of Campaigns 14 through 18 are preliminary and will certainly change by a few arcminutes, or more, e.g. to accommodate the guide star selection. This catalog is hence preliminary for those Campaigns.

###  Author
Created by Geert Barentsen on 1 Dec 2015.
