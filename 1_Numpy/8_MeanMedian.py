import pandas as pd

np_baseball = pd.read_csv("baseball.csv")[['Height', 'Weight', 'Age']].values
# np_baseball[slice(0, 1015, 50), 0] = np_baseball[slice(0, 1015, 50), 0] * 1000
print(np_baseball)
# np_baseball is available

# Import numpy
import numpy as np

# Create np_height_in from np_baseball
np_height_in = np_baseball[:, 0]

# Print out the mean of np_height_in
print(np.mean(np_height_in))

# Print out the median of np_height_in
print(np.median(np_height_in))
