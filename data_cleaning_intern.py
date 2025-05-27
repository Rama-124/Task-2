# ----------------------------------------
# 1. Import Required Libraries
# ----------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Try importing plotly, show message if not installed
try:
    import plotly.express as px
    plotly_installed = True
except ImportError:
    print("Plotly is not installed. Run: pip install plotly")
    plotly_installed = False

# Set seaborn style
sns.set(style="whitegrid")

# ----------------------------------------
# 2. Load the Dataset (correct local path)
# ----------------------------------------
df = pd.read_csv(r'c:\Users\User\OneDrive\Desktop\task 1\titanic.csv')

# ----------------------------------------
# 3. Dataset Overview
# ----------------------------------------
print("First 5 Rows:\n", df.head())
print("\nDataset Info:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe(include='all'))
print("\nMissing Values:\n", df.isnull().sum())

# ----------------------------------------
# 4. Handle Missing Data
# ----------------------------------------
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df.drop(columns=['Cabin'], inplace=True)  # too many missing values

# ----------------------------------------
# 5. Histograms
# ----------------------------------------
df.hist(bins=20, figsize=(15, 10), color='skyblue')
plt.suptitle("Histograms of Numeric Features")
plt.tight_layout()
plt.show()

# ----------------------------------------
# 6. Boxplots
# ----------------------------------------
sns.boxplot(x=df['Age'])
plt.title("Boxplot of Age")
plt.show()

sns.boxplot(x=df['Fare'])
plt.title("Boxplot of Fare")
plt.show()

# ----------------------------------------
# 7. Correlation Heatmap
# ----------------------------------------
corr = df.corr(numeric_only=True)
print("\nCorrelation Matrix:\n", corr)

plt.figure(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# ----------------------------------------
# 8. Pairplot (Survived, Age, Fare, Pclass)
# ----------------------------------------
sns.pairplot(df[['Survived', 'Age', 'Fare', 'Pclass']], hue='Survived')
plt.suptitle("Pairplot of Key Features", y=1.02)
plt.show()

# ----------------------------------------
# 9. Skewness Check
# ----------------------------------------
print("\nSkewness:")
print("Age:", df['Age'].skew())
print("Fare:", df['Fare'].skew())

# ----------------------------------------
# 10. Categorical Analysis
# ----------------------------------------
# Survival by Gender
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title("Survival Count by Gender")
plt.show()

# Survival by Pclass
sns.barplot(x='Pclass', y='Survived', data=df)
plt.title("Survival Rate by Passenger Class")
plt.show()

# ----------------------------------------
# 11. Age Distribution by Survival (KDE Plot)
# ----------------------------------------
plt.figure(figsize=(10, 6))
sns.kdeplot(data=df[df['Survived'] == 1]['Age'], label='Survived', fill=True)
sns.kdeplot(data=df[df['Survived'] == 0]['Age'], label='Did Not Survive', fill=True)
plt.title("Age Distribution by Survival")
plt.xlabel("Age")
plt.legend()
plt.show()

# ----------------------------------------
# 12. Plotly Interactive Chart (optional)
# ----------------------------------------
if plotly_installed:
    fig = px.scatter(df, x='Age', y='Fare', color=df['Survived'].astype(str),
                     title='Fare vs Age (Colored by Survival)',
                     labels={'color': 'Survived'})
    fig.show()
