"""
Visualize covid vaccines
"""
import pandas as pd
import code
import matplotlib.pyplot as plt
import matplotlib as mpl
import random
import plotly.express as px
import squarify
import code

df = pd.read_csv("covid.csv")  # , delimeter=",")

df_summary = df.groupby("vaccine").sum(numeric_only=True)

# code.interact(local=locals())

fig, ax = plt.subplots()

if False:
    ax.pie(df_summary["total_vaccinations"], labels=df_summary.index, autopct="%1.1f%%")
    ax.set_title("Vaccination Brands Distribution")

    plt.tight_layout()
    plt.show()


if False:
    fig = px.pie(
        df_summary.reset_index(),
        values="total_vaccinations",
        names="vaccine",
        title="Vaccination Brands Distribution",
    )
    fig.show()


# Create a plot
fig = plt.gcf()
ax = fig.add_subplot()
fig.set_size_inches(5, 5)

# Create a color palette, mapped to these values

if False:
    # cmap = plt.cm.Spectral
    cmap = plt.cm.Set3
    mini = min(df_summary["total_vaccinations"])
    maxi = max(df_summary["total_vaccinations"])
    # norm = plt.Normalize(vmin=mini, vmax=maxi)
    norm = mpl.colors.LogNorm(vmin=mini, vmax=maxi)
    colors = [cmap(norm(value)) for value in df_summary["total_vaccinations"]]

# RANDOM COLORS
colors = []
for _ in range(len(df_summary)):
    random_color = (
        random.uniform(0, 1),
        random.uniform(0, 1),
        random.uniform(0, 1),
        1.0,
    )
    colors.append(random_color)

code.interact(local=locals())


# Create a tree map
df_summary0 = df_summary.reset_index()
squarify.plot(
    sizes=df_summary0["total_vaccinations"],
    label=df_summary0["vaccine"],
    alpha=0.8,
    color=colors,
)
plt.title("Vaccination Brands Distribution", fontsize=23, fontweight="bold")
plt.axis("off")
plt.show()
