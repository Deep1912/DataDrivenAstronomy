# Write your function median_FITS here:
from astropy.io import fits
import numpy as np
import time
import sys

def median_fits(fileNameArray):
	if len(fileNameArray) == 0:
		return 0
	
	startTime = time.perf_counter()

	firstFileName = fits.open(fileNameArray[0])
	firstFileData = firstFileName[0].data
	numberOfRows = len(firstFileData)
	numberOfColumns = len(firstFileData[0])
	
	allFileData = np.array([firstFileData.flatten()])

	if len(fileNameArray) > 1:
		for fileName in fileNameArray[1:]:
			hdulist = fits.open(fileName)
			data = hdulist[0].data
			allFileData = np.vstack([allFileData, data.flatten()])

	medianOfAllData = np.median(allFileData, axis=0)
	medianOfAllData = np.reshape(medianOfAllData, (numberOfRows, numberOfColumns))

	endTime = time.perf_counter()

	memoryUsedInkB = sys.getsizeof(allFileData) / 1024
	timeUsed = endTime - startTime

	return medianOfAllData, timeUsed, memoryUsedInkB



# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with first example in the question.
  result = median_fits(['image0.fits', 'image1.fits'])
  print(result[0][100, 100], result[1], result[2])
  
  # Run your function with second example in the question.
  result = median_fits(['image{}.fits'.format(str(i)) for i in range(11)])
  print(result[0][100, 100], result[1], result[2])