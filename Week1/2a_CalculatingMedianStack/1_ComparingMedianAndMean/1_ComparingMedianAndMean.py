# Write your list_stats function here.

def list_stats(listOfNumbers):
	lengthOfListOfNumbers = len(listOfNumbers)
	if lengthOfListOfNumbers == 0:
		return 0, 0
		
	listOfNumbers.sort()
	middleIndex = lengthOfListOfNumbers // 2
	
	if (lengthOfListOfNumbers % 2 == 0):
		median = (listOfNumbers[middleIndex -1] + listOfNumbers[middleIndex + 1]) / 2
	else:
		median = listOfNumbers[middleIndex]

	sumOfNumbers = 0
	for number in listOfNumbers:
		sumOfNumbers += number
	mean = sumOfNumbers / lengthOfListOfNumbers

	return median, mean

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example in the question.
  m = list_stats([1.3, 2.4, 20.6, 0.95, 3.1, 2.7])
  print(m)

  # Run your function with the second example in the question
  m = list_stats([1.5])
  print(m)