import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# Sample data
data = {"Fruits": ["Apples", "Oranges", "Bananas", "Grapes"], "Count": [25, 35, 30, 20]}

# Convert to DataFrame
df = pd.DataFrame(data)

sns.set_palette("rocket")

# Plotting
sns.barplot(x="Fruits", y="Count", data=df)
plt.show()
