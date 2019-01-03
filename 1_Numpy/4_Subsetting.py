import pandas as pd

mlb = pd.read_csv("baseball.csv")
height_in = mlb['Height'].tolist()
weight_lb = mlb['Weight'].tolist()

# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Store weight and height lists as numpy arrays
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height: index 100 up to and including index 110
print(np_height_in[100:111])

print(np_height_in[:10:2])
