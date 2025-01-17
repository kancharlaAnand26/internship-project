import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample dataset
data = {
    'Age': [22, 25, 28, 30, 22, 24, 27, 30, 23, 24, 22, 29, 31, 30, 25],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male', 'Female', 'Female', 
               'Male', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male']
}

# Creating a DataFrame
df = pd.DataFrame(data)

#histogram for Age Distribution
plt.figure(figsize=(8,6))
sns.histplot(df['Age'],bins=6,kde=True,color='skyblue')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Setting a style for the plot
sns.set_style("whitegrid")

# Bar chart for gender distribution
plt.figure(figsize=(8, 6))
sns.countplot(x='Gender', data=df, palette='Set2')

# Adding title and labels
plt.title('Gender Distribution', fontsize=16, fontweight='bold')
plt.xlabel('Gender', fontsize=14)
plt.ylabel('Count', fontsize=14)

# Displaying the plot
plt.show()

