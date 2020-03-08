# Write your mean_fits function here:
from astropy.io import fits
import numpy as np

def mean_fits(fileNameArray):
	if len(fileNameArray) == 0:
		return 0
	
	firstFileName = fits.open(fileNameArray[0])
	firstFileData = firstFileName[0].data
	numberOfRows = len(firstFileData)
	numberOfColumns = len(firstFileData[0])
	
	sumOfFiles = np.zeros((numberOfRows, numberOfColumns))

	for fileName in fileNameArray:
		hdulist = fits.open(fileName)
		data = hdulist[0].data
		sumOfFiles += data

	return sumOfFiles/len(fileNameArray)

if __name__ == '__main__':
  
  # Test your function with examples from the question
  data  = mean_fits(['image0.fits', 'image1.fits', 'image2.fits'])
  print(data[100, 100])

  # You can also plot the result:
  import matplotlib.pyplot as plt
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()