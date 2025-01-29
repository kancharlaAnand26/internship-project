import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {
    'Age': [22, 25, 28, 30, 22, 24, 27, 30, 23, 24, 22, 29, 31, 30, 25],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male', 'Female', 'Female', 
               'Male', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male']
}

df = pd.DataFrame(data)


plt.figure(figsize=(8,6))
sns.histplot(df['Age'],bins=6,kde=True,color='skyblue')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


sns.set_style("whitegrid")


plt.figure(figsize=(8, 6))
sns.countplot(x='Gender', data=df, palette='Set2')


plt.title('Gender Distribution', fontsize=16, fontweight='bold')
plt.xlabel('Gender', fontsize=14)
plt.ylabel('Count', fontsize=14)


plt.show()

