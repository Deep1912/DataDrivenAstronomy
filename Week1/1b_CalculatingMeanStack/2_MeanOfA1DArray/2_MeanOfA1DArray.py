# Write your calc_stats function here.
import numpy as np

def calc_stats(fileName):
	data = np.loadtxt(fileName, delimiter=',')
	return np.mean(data), np.std(data)

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your `calc_stats` function with examples:
  mean = calc_stats('data.csv')
  print(mean)