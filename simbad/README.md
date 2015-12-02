# Simbad catalog of candidate K2 targets

The file `K2-C9-C18-Simbad.xml.gz` in this directory is a VOTable
that contains all the Simbad entries that lie on Silicon 
in Campaigns 9 through 18, which are the future Campaigns for which
targets can still be requested.

*Notes:* the positions of Campaigns 14 through 18 are preliminary
and likely to change, at which point these table will need to be updated.

### Contents

The table details Simbad IDs, coordinates, magnitudes, [object types](http://simbad.u-strasbg.fr/simbad/sim-display?data=otypes),
spectral types, proper motions, citation counts, and campaign numbers.


### Usage

We recommend using [TopCat](http://www.star.bristol.ac.uk/~mbt/topcat/)
or [AstroPy](http://www.astropy.org)'s `Table.read()` to inspect the table.


###  Author

Created by Geert Barentsen on 1 Dec 2015.
