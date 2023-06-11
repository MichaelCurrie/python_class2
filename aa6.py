"""
Visualize the population of the provinces of Thailand
using a horizontal bar chart.

"""
import code
import os
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# The fonts are saved at:
# C:\Users\GL503GE\.conda\envs\env4\Lib\site-packages\matplotlib\mpl-data\fonts\ttf
print(f"font directory is {fm.win32FontDirectory()}")
# This is the font directory
# C:\\Windows\Fonts
# ACTUALLY THIS IS A DIRTY LIE, IT'S ACTUALLY HERE:
# print(f"font names are {fm.get_font_names()}")
# But actually they are saved here:
path_to_font = os.path.join(
    "C:\\",
    "Users",
    "GL503GE",
    "AppData",
    "Local",
    "Microsoft",
    "Windows",
    "Fonts",
    "THSarabun.ttf",
)
assert os.path.isfile(path_to_font)

# Use a font that supports Thai characters
# Define our special Thai font properties
# sarabun_font = FontProperties()
# sarabun_font.set_family('Sarabun')
sarabun_font = fm.FontProperties(fname=path_to_font)
sarabun_font.set_size(12)

# THIS DOESN'T SEEM TO WORK
# plt.rcParams["font.family"] = "TH SarabunPSK"


# Get our province population dataset
url = "https://data.go.th//dataset//c6fb53a5-4d9d-4f21-84a7-9662b25af9c3//resource//225ff892-3874-4072-9787-a2c30128e3f7//download//stat_c.txt"

df = pd.read_csv(url, sep="|")

# Slice to only December 2563
df0 = df.loc[(df["YYMM"] == 6312) & (df["CC-CODE"] != 0), ["CC-DESC", "TOTAL"]]

# Strip out the whitespace
df0 = df0.applymap(lambda x: x.strip() if isinstance(x, str) else x)

df0 = df0.set_index("CC-DESC")

df0["TOTAL"] = df0["TOTAL"].str.replace(",", "").astype(int)
df0 = df0.sort_values("TOTAL", ascending=True)

fig, ax = plt.subplots()

ax.barh(df0.index, df0["TOTAL"])

# Set font properties for labels and title
plt.xlabel("Category", fontproperties=sarabun_font)
plt.ylabel("Values", fontproperties=sarabun_font)
plt.title("Bar plot", fontproperties=sarabun_font)

for label in ax.get_xticklabels():
    label.set_fontproperties(sarabun_font)

for label in ax.get_yticklabels():
    label.set_fontproperties(sarabun_font)

plt.yticks(fontsize=6)

mpl.pyplot.show()

# code.interact(local=locals())
