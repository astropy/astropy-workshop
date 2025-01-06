import astropy.units as u
import numpy as np
from astropy.io import fits
from photutils.aperture import CircularAperture, aperture_photometry

sci_fn = 'data/xdf_hst_wfc3ir_60mas_f160w_sci.fits'
rms_fn = 'data/xdf_hst_wfc3ir_60mas_f160w_rms.fits'
sci_hdulist = fits.open(sci_fn)
rms_hdulist = fits.open(rms_fn)
data = sci_hdulist[0].data.astype(float)
error = rms_hdulist[0].data.astype(float)

positions = [(34.61, 137.99), (184.53, 157.52), (88.75, 184.22)]
aper = CircularAperture(positions, r=4.5)
unit = u.electron / u.s
phot = aperture_photometry(data << unit, aper, error=error << unit)

snr = phot['aperture_sum'] / phot['aperture_sum_err']
phot['snr'] = snr

f160w_zpt = 25.941
abmag = -2.5 * np.log10(phot['aperture_sum'].value) + f160w_zpt
phot['f160w_abmag'] = abmag

phot
