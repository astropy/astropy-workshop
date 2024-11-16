import astropy.units as u
from astropy.io import fits
from photutils.segmentation import SegmentationImage, SourceCatalog

# read in the F105W science data
f105w_data = fits.getdata('data/xdf_hst_wfc3ir_60mas_f105w_sci.fits')
f105w_data <<= (u.electron / u.s)

# read in the previously-saved F160W segmentation image data
# and create a `SegmentationImage` object
f160w_segm_filename = 'xdf_f160w_segm.fits'
f160w_segm_data = fits.getdata(f160w_segm_filename)
f160w_segm = SegmentationImage(f160w_segm_data)

# apply the F160W segmentation image to the F105W data
f105w_cat = SourceCatalog(f105w_data, f160w_segm)
f105w_cat.segment_flux
