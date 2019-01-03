import pandas as pd
import numpy as np

baseball = pd.read_csv("baseball.csv")[['Height', 'Weight']].as_matrix().tolist()
# baseball is available as a regular list of lists


# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)
