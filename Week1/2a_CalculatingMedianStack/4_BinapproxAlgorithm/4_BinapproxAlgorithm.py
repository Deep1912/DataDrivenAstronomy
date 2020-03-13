# Write your median_bins and median_approx functions here.
import numpy as np

def median_bins(listOfValues, B):
	data = np.array(listOfValues)

	mu = np.mean(data)
	sigma = np.std(data)
	
	minval = mu - sigma
	maxval = mu + sigma
	width = 2 * sigma / B

	numberOfSmallerValues = 0
	binCountArray = np.zeros(B)
	for value in np.nditer(data):
		if value < minval:
			numberOfSmallerValues += 1
		elif value >= maxval:
			continue
		else:
			binIndex = int((value - minval) // width)
			binCountArray[binIndex] += 1	

	return mu, sigma, numberOfSmallerValues, binCountArray

def median_approx(listOfValues, B):
	mu, sigma, numberOfSmallerValues, binCountArray = median_bins(listOfValues, B)	

	cumulativeNumberOfValues = numberOfSmallerValues
	indexOfMedian = -1
	for numberOfValues in binCountArray:
		if cumulativeNumberOfValues >= ((len(listOfValues)) + 1 ) / 2 :
			break
		cumulativeNumberOfValues += numberOfValues
		indexOfMedian += 1

	minval = mu - sigma
	width = 2 * sigma / B
	median = minval + (width * indexOfMedian) + (width / 2)

	return median


# You can use this to test your functions.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your functions with the first example in the question.
  print(median_bins([1, 1, 3, 2, 2, 6], 3))
  print(median_approx([1, 1, 3, 2, 2, 6], 3))

  # Run your functions with the second example in the question.
  print(median_bins([1, 5, 7, 7, 3, 6, 1, 1], 4))
  print(median_approx([1, 5, 7, 7, 3, 6, 1, 1], 4))
