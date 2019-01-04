# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load iris data
iris = sns.load_dataset("iris")

# Set context to `"paper"`
sns.set_context("paper", font_scale=3, rc={"font.size": 8, "axes.labelsize": 5})

# all context options: "paper", "notebook", "talk" and "poster"

# Construct iris plot
sns.swarmplot(x="species", y="petal_length", data=iris)

# Show plot
plt.show()
