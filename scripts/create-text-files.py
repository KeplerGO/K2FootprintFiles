"""Export the channel corner coordinates of K2 campaigns to JSON/CSV files."""
import json
from collections import OrderedDict

import numpy as np

from astropy.table import Table
from astropy import log
from astropy.utils.console import ProgressBar
from astropy.coordinates import SkyCoord

from K2fov import getFieldNumbers, getFieldInfo, getKeplerFov

"""Configuration constants"""
# Which channels are no longer in use?
# Note: K2fov defines the FGS chips as "channels" 85-88; we ignore these
CHANNELS_TO_IGNORE = [5, 6, 7, 8,
                      17, 18, 19, 20,
                      85, 86, 87, 88]
# Module 4 failed during Campaign 10
CHANNELS_TO_IGNORE_FROM_C11 = CHANNELS_TO_IGNORE + [9, 10, 11, 12]

if __name__ == "__main__":
    tbl = []
    tbl_prelim = []
    json_dict = OrderedDict([])
    json_dict_prelim = OrderedDict([])

    for campaign in ProgressBar(getFieldNumbers()):
        # Obtain the metadata
        fieldinfo = getFieldInfo(campaign)
        corners = getKeplerFov(campaign).getCoordsOfChannelCorners()

        # Convert the footprint into a user-friendly format
        channels = OrderedDict([])
        for ch in np.arange(1, 89, dtype=int):
            if (ch in CHANNELS_TO_IGNORE) or (campaign > 10 and ch in CHANNELS_TO_IGNORE_FROM_C11):
                continue  # certain channel are no longer used
            idx = np.where(corners[::, 2] == ch)
            mdl = int(corners[idx, 0][0][0])
            out = int(corners[idx, 1][0][0])
            channel_name = "{}".format(ch)  # JSON requires keys to be strings
            ra = corners[idx, 3][0]
            dec = corners[idx, 4][0]
            crd = SkyCoord(ra, dec, unit='deg')
            glon = crd.galactic.l
            glat = crd.galactic.b
            channels[channel_name] = OrderedDict([
                                        ('module', str(mdl)),
                                        ('output', str(out)),
                                        ('corners_ra', list(ra)),
                                        ('corners_dec', list(dec)),
                                        ('corners_glon', list(glon.value)),
                                        ('corners_glat', list(glat.value)),
                                        ])
            tbl_row = {
                      "campaign": campaign,
                      "start": fieldinfo["start"],
                      "stop": fieldinfo["stop"],
                      "channel": ch,
                      "module": mdl,
                      "output": out,
                  }
            for corner_idx in range(4):
                tbl_row["ra{}".format(corner_idx)] = ra[corner_idx]
                tbl_row["dec{}".format(corner_idx)] = dec[corner_idx]

            if "preliminary" in fieldinfo:
                tbl_prelim.append(tbl_row)
            else:
                tbl.append(tbl_row)

        # Add the metadata to the JSON dictionary
        campaign_dict = OrderedDict([
                                    ("campaign", campaign),
                                    ("start", fieldinfo["start"]),
                                    ("stop", fieldinfo["stop"]),
                                    ("ra", fieldinfo["ra"]),
                                    ("dec", fieldinfo["dec"]),
                                    ("roll", fieldinfo["roll"]),
                                    ("comments", fieldinfo["comments"]),
                                    ("channels", channels)
                                    ])

        if "preliminary" in fieldinfo:
            json_dict_prelim["c{}".format(campaign)] = campaign_dict
        else:
            json_dict["c{}".format(campaign)] = campaign_dict

    # Write the results to disk
    output_fn = "../json/k2-footprint.json"
    log.info("Writing {}".format(output_fn))
    json.dump(json_dict, open(output_fn, "w"), indent=2)

    #output_fn = "../json/k2-footprint-proposed.json"
    #log.info("Writing {}".format(output_fn))
    #json.dump(json_dict_prelim, open(output_fn, "w"), indent=2)

    # Also save a csv table
    names = ["campaign", "start", "stop", "channel", "module", "output",
             "ra0", "dec0", "ra1", "dec1", "ra2", "dec2", "ra3", "dec3"]
    output_fn = "../csv/k2-footprint.csv"
    log.info("Writing {}".format(output_fn))
    Table(tbl, names=names).write(output_fn, format="ascii.csv", overwrite=True)

    #output_fn = "../csv/k2-footprint-proposed.csv"
    #log.info("Writing {}".format(output_fn))
    #Table(tbl_prelim, names=names).write(output_fn, format="ascii.csv", overwrite=True)
