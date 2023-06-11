"""
Titanic survivors
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import seaborn as sns
import code

# You can replace the file path with your local path where the CSV file is located.
df = pd.read_csv(
    "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
)

# Let's check the first few rows of the dataframe to see what the data looks like.
print(df.head())

# Group the data by 'Sex' and 'Survived', and then count the number of passengers.
survived_by_sex = df.groupby(["Sex", "Survived"]).size().unstack()

# code.interact(local=locals())

# normalized_df = survived_by_sex / survived_by_sex.sum()
# Normalize the data grouping by gender
normalized_df = survived_by_sex.div(survived_by_sex.sum(axis=1), axis=0)

# Plot the bar chart.
# normalized_df.plot(kind="bar", stacked=True)

# plt.title("Survival by Sex")
# plt.xlabel("Sex")
# plt.ylabel("Count")
# plt.show()

df0 = df.loc[~pd.isna(df["Age"]), :]

# Split the DataFrame into features and target
feature_cols = df0.loc[:, ["Age", "Fare", "Pclass", "PassengerId"]]  # Feature columns
target_col = df0.loc[:, "Survived"]  # Target column

X_train, X_test, y_train, y_test = train_test_split(
    feature_cols, target_col, test_size=0.3, random_state=0
)

# Create a Logistic Regression object
logreg = LogisticRegression()

# Fit the model to the training data
logreg.fit(X_train, y_train)

# Use the model to make predictions on the test data
y_pred = logreg.predict(X_test)

print(
    "Accuracy of logistic regression classifier on test set: {:.2f}".format(
        logreg.score(X_test, y_test)
    )
)

"""
for column in feature_cols:
    plt.figure(figsize=(5, 5))
    sns.scatterplot(data=df0, x=column, y="Survived")
    plt.title(f"Survived vs {column}")
    plt.show()
"""

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df0, x="Age", y="Fare", hue="Survived")
plt.title("Survival by Age and Fare")
plt.show()
