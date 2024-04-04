import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the data from CSV file
df = pd.read_csv("restaurants.csv")

print(df.head())
# Visualize the distribution of ratings
plt.figure(figsize=(10, 6))
sns.histplot(df['Rating'], bins=20, kde=True)
plt.title("Distribution of Ratings")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.show()


# Top Cuisine Analysis
top_cuisines = df['Cuisine'].str.split(', ', expand=True).stack().value_counts().head(10)

# Votes Distribution Analysis across States
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='City', y='Votes')
plt.title("Votes Distribution Across States")
plt.xlabel("State")
plt.ylabel("Votes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Comparison of Average Dining Cost Across Cities
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='City', y='Cost', estimator='mean')
plt.title("Average Dining Cost Across Cities")
plt.xlabel("City")
plt.ylabel("Average Cost")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Distribution of Restaurants Across Cities in India
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='City')
plt.title("Distribution of Restaurants Across Cities in India")
plt.xlabel("City")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Distribution of Restaurant Costs in India
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Cost', bins=20)
plt.title("Distribution of Restaurant Costs in India")
plt.xlabel("Cost")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
