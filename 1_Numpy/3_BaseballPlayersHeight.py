import pandas as pd
import numpy as np

mlb = pd.read_csv("baseball.csv")
height_in = mlb['Height'].tolist()

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height to m: np_height_m
np_height_m = np_height_in * 0.0254

# Print np_height_m
print(np_height_m)
