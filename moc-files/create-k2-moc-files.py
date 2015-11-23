"""Creates MOC files showing the approximate sky coverage of K2 Campaigns.

MOC files can be loaded into Aladin for visualisation and for querying
other databases by the moc-defined footprint.

This script was created with help from Thomas Boch at CDS, thanks Thomas!
"""
import json
import numpy as np

from astropy import log
from astropy.utils.console import ProgressBar

import healpy as hp
import mocpy
from mocpy.utils import radec2thetaphi


# Which campaigns do we want to MOCs for?
CAMPAIGNS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
CAMPAIGNS_PROPOSED = [14, 15, 16, 17]
# What is the best healpix resolution we desire?
NORDER_MOC = 14
# Load the K2 footprint corners?
FOOTPRINT = json.load(open("../k2-footprint.json"))
FOOTPRINT.update(json.load(open("../k2-footprint-proposed.json")))

def write_k2_moc(campaign=0, norder_moc=NORDER_MOC, output_fn=None):
    if output_fn is None:
        if campaign in CAMPAIGNS_PROPOSED:
            output_fn = "k2-footprint-c{:02d}-proposed.moc".format(campaign)
        else:
            output_fn = "k2-footprint-c{:02d}.moc".format(campaign)
    # Obtain the footprint corners in polar coordinates
    log.info("Preparing footprint polygons for C{}".format(campaign))
    polygons = []
    for _, channel in FOOTPRINT["c{}".format(campaign)]["channels"].items():
        polygon = [np.pi/2. - np.radians(channel["corners_dec"]),
                   np.radians(channel["corners_ra"])]
        polygons.append(polygon)
    # Obtain the healpix diamonds that cover the polygons entirely
    # and add these to a `MOC` object
    log.info("Converting polygons into healpix format")
    moc = mocpy.MOC(moc_order=norder_moc)
    for p in polygons:
        pix_list = hp.query_polygon(2**norder_moc,
                                    hp.ang2vec(p[0], p[1]),
                                    inclusive=True, nest=True)
        for pix in pix_list:
            moc.add_pix(norder_moc, pix)
    # Finally, write the resulting MOC file to disk
    log.info("Writing {}".format(output_fn))
    moc.plot()  # IMPORTANT! moc.write is corrupt if plot is not called first
    moc.write(output_fn)


if __name__ == "__main__":
    # Write MOC files for all campaigns in parallel
    ProgressBar.map(write_k2_moc, CAMPAIGNS_PROPOSED,
                    multiprocess=True)
