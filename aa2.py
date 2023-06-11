"""
Visualize flight data over time
"""

import seaborn as sns
import matplotlib.pyplot as plt
import code

# Load the flights dataset
flights = sns.load_dataset("flights")

# Let's check the first few rows of the dataframe to see what the data looks like.
print(flights.head())

# Pivot the dataframe
flights_pivot = flights.pivot(index="month", columns="year", values="passengers")

print(flights_pivot)  # Create a heatmap

# UGLY
# flights_pivot.sum().plot(kind='bar', legend=False)


# BEAUTIFUL:
sns.set(style="whitegrid")
flights_by_year = flights_pivot.sum().to_frame("flights").reset_index()
sns.barplot(x="year", y="flights", data=flights_by_year, palette="cubehelix")
plt.title("Total Flights by Year")
plt.show()


plt.figure(figsize=(10, 8))
sns.heatmap(flights_pivot, annot=True, fmt="d", cmap="YlGnBu")

# Show the plot
plt.show()
