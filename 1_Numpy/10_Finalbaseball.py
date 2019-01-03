import pandas as pd

baseball = pd.read_csv("baseball.csv", skipinitialspace=True, usecols=['Position', 'Height'])
Position = list(baseball.Position)
Height = list(baseball.Height)

# heights and positions are available as lists

# Import numpy
import numpy as np

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(Position)
np_heights = np.array(Height)

# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'Catcher']

# Heights of the other players: other_heights
other_heights = np_heights[np_positions != 'Catcher']

# Print out the median height of goalkeepers
print("Median height of Catchers: " , np.median(gk_heights))

# Print out the median height of other players
print("Median height of other players: " , np.median(other_heights))
