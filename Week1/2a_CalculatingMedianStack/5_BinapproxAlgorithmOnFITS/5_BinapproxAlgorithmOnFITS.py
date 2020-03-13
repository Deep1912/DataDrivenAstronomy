# Import the running_stats function
from helper import running_stats
# Write your median_bins_fits and median_approx_fits here:
from astropy.io import fits
import numpy as np

def median_bins_fits(fileNameArray, B):
    if len(fileNameArray) == 0:
        return 0, 0, 0, 0

    firstFileName = fits.open(fileNameArray[0])
    firstFileData = firstFileName[0].data
    numberOfRows = len(firstFileData)
    numberOfColumns = len(firstFileData[0])

    mu, sigma = running_stats(fileNameArray)
    
    minval = mu - sigma
    maxval = mu + sigma
    width = 2 * sigma / B

    numberOfSmallerValues = np.zeros((numberOfRows, numberOfColumns))
    binCountArray = np.zeros((numberOfRows, numberOfColumns, B))

    for fileName in fileNameArray:
        hdulist = fits.open(fileName)
        data = hdulist[0].data

        for index, value in np.ndenumerate(data):
            if value < minval[index]:
                numberOfSmallerValues[index] += 1
            elif value >= maxval[index]:
                continue
            else:
                binIndex = int((value - minval[index]) // width[index])
                binCountArray[index][binIndex] += 1

    return mu, sigma, numberOfSmallerValues, binCountArray

def median_approx_fits(fileNameArray, B):
    mu, sigma, numberOfSmallerValues, binCountArray = median_bins_fits(fileNameArray, B) 

    numberOfFiles = len(fileNameArray)
    firstFileName = fits.open(fileNameArray[0])
    firstFileData = firstFileName[0].data
    numberOfRows = len(firstFileData)
    numberOfColumns = len(firstFileData[0]) 

    cumulativeNumberOfValues = numberOfSmallerValues
    indexOfMedian = np.full((numberOfRows, numberOfColumns), -1)

    for row in range(0, numberOfRows):
        for column in range(0, numberOfColumns):
            for binNumber in range(0, B):
                if cumulativeNumberOfValues[(row, column)] >= (numberOfFiles + 1 ) / 2 :
                    break
                cumulativeNumberOfValues[(row, column)] += binCountArray[(row, column, binNumber)]
                indexOfMedian[(row, column)] += 1

    minval = mu - sigma
    width = 2 * sigma / B
    median = minval + (width * indexOfMedian) + (width / 2)

    return median


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
    # Run your function with examples from the question.
    mean, std, left_bin, bins = median_bins_fits(['image0.fits', 'image1.fits', 'image2.fits'], 5)
    median = median_approx_fits(['image0.fits', 'image1.fits', 'image2.fits'], 5)
