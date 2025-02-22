# Simbad catalog of candidate K2 targets

The files `K2-C9-C13-Simbad.xml.gz` and `K2-C14-C16-Simbad.xml.gz` in this directory are VOTables
that lists all the [SIMBAD](http://simbad.u-strasbg.fr/simbad/) entries that will lie on silicon 
in [Campaigns 9 through 16](http://keplerscience.arc.nasa.gov/k2-fields.html), i.e. future campaigns
for which pixel masks can be requested via the 
standard [calls for proposals](http://keplerscience.arc.nasa.gov/k2-proposing-targets.html) 
or via [Director's Discretionary Time](http://keplerscience.arc.nasa.gov/k2-ddt.html) (DDT).

### Contents
The table details Simbad IDs, coordinates, magnitudes, [object types](http://simbad.u-strasbg.fr/simbad/sim-display?data=otypes),
spectral types, proper motions, citation counts, and campaign numbers.

### Usage
We recommend using [TopCat](http://www.star.bristol.ac.uk/~mbt/topcat/)
or [AstroPy](http://www.astropy.org)'s `Table.read()` to inspect the table.

### Caveats
* SIMBAD does ***not*** list every object in the sky!
* Objects on or near the edges of CCD detectors have been included in this catalog,
eventhough they may not be observable.  The true observability will depend on the brightness, i.e. the pixel mask size required.
* The positions of Campaigns 14 through 18 are preliminary and will certainly change by a few arcminutes or more, e.g. to accommodate the guide star selection. This catalog is hence preliminary for those Campaigns.

### More info about K2 science

Visit [http://keplerscience.arc.nasa.gov](http://keplerscience.arc.nasa.gov)

###  Author
Created by Geert Barentsen on 1 Dec 2015.
