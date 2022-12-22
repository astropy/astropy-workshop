from astropy.table import QTable
import numpy as np
from photutils.segmentation import SourceCatalog

# load the F160W source catalog table
f160w_catalog_filename = 'xdf_f160w_catalog.ecsv'
f160w_tbl = QTable.read(f160w_catalog_filename)

# (re-)create the F105W source catalog
f105w_cat = SourceCatalog(f105w_data, f160w_segm)

# calculate the AB magnitudes using the filter zero points
f105w_abmag = -2.5 * np.log10(f105w_cat.segment_flux.value) + 26.2687
f160w_abmag = -2.5 * np.log10(f160w_tbl['segment_flux'].value) + 26.9463

# calculate the Y-H colors
yh_colors = f105w_abmag - f160w_abmag
print(yh_colors)

# add the values to the table
f160w_tbl['f105w_abmag'] = f105w_abmag
f160w_tbl['f160w_abmag'] = f160w_abmag
f160w_tbl['yh_color'] = yh_colors

# finally, find the table indices that sort the yh_color column.
# reverse=True sorts the table from largest to smallest value
# then select the reddest 3 sources
idx = f160w_tbl.argsort('yh_color', reverse=True)
brightest = f160w_tbl[idx][0:3]
print(brightest)
