# Write your load_fits function here.
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

def load_fits(fileName):
	hdulist = fits.open(fileName)
	data = hdulist[0].data
	indexOfBrightest = np.argmax(data)
	
	numberOfColumn = len(data[0])
	rowOfBrightest = np.floor(indexOfBrightest/numberOfColumn)
	columnOfBrightest = indexOfBrightest%numberOfColumn
	
	return rowOfBrightest, columnOfBrightest

if __name__ == '__main__':
  # Run your `load_fits` function with examples:
  bright = load_fits('image1.fits')
  print(bright)

  # You can also confirm your result visually:
  from astropy.io import fits
  import matplotlib.pyplot as plt

  hdulist = fits.open('image1.fits')
  data = hdulist[0].data

  # Plot the 2D image data
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()

 








hdulist = fits.open('image0.fits')
data = hdulist[0].data

print(data.shape)