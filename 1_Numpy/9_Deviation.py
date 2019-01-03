import pandas as pd

np_baseball = pd.read_csv("baseball.csv")[['Height', 'Weight', 'Age']].values
import numpy as np

print(np_baseball)

# Print mean height (first column)
avg = np.mean(np_baseball[:, 0])
print("Average: " + str(avg))

# Print median height.
med = np.median(np_baseball[:, 0])
print("Median: " + str(med))

# Print out the standard deviation on height.
stddev = np.std(np_baseball[:, 0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column.
corr = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])
print("Correlation: " + str(corr))
