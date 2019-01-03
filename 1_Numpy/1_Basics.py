# Import the numpy package as np
import numpy as np

# Create 2 new lists height and weight
height = [1.87, 1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

print(type(height))
print(type(weight))

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

print(type(np_height))
print(type(np_weight))

print("np_height: ", np_height)
print("np_weight: ", np_weight)

# Calculate bmi
bmi = np_weight / np_height ** 2

# Print the result
print("BMI = ", bmi)

# Print only the results greater than 25
print(bmi[bmi > 25])
