# Write your calc_stats function here.
import numpy as np

def mean_datasets(filenameArray):
	if len(filenameArray) == 0:
		return 0
		
	firstFileData = np.loadtxt(filenameArray[0], delimiter=',')
	numberOfRows = len(firstFileData)
	numberOfColumns = len(firstFileData[0])
	sumOfFiles = np.zeros((numberOfRows, numberOfColumns))

	for fileName in filenameArray:
		fileData = np.loadtxt(fileName, delimiter=',')
		sumOfFiles = sumOfFiles + fileData
	return np.round(sumOfFiles/len(filenameArray), 1)

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example from the question:
  print(mean_datasets(['data1.csv', 'data2.csv', 'data3.csv']))

  # Run your function with the second example from the question:
  print(mean_datasets(['data4.csv', 'data5.csv', 'data6.csv']))
