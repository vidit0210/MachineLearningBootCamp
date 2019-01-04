# Import necessarily libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
titanic = sns.load_dataset("titanic")

# Set up a factorplot, now known as catplot()
g = sns.catplot("class", "survived", "sex", data=titanic, kind="bar", palette="muted", legend=False)

# colors should be displayed with the "palette" argument

# Show plot
plt.show()
