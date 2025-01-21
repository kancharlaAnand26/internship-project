# Simulating a sample Titanic dataset for demonstration purposes
import pandas as pd
data = {
    "PassengerId": range(1, 11),
    "Survived": [1, 0, 1, 1, 0, 0, 1, 0, 1, 0],
    "Pclass": [1, 3, 2, 1, 3, 3, 2, 1, 3, 2],
    "Name": [
        "Allen, Miss. Elisabeth",
        "Smith, Mr. John",
        "Brown, Mrs. Margaret",
        "Williams, Mr. Charles",
        "Johnson, Miss. Emily",
        "Taylor, Mr. James",
        "Clark, Mrs. Alice",
        "Walker, Mr. George",
        "Harris, Miss. Sarah",
        "Martin, Mr. William",
    ],
    "Sex": ["female", "male", "female", "male", "female", "male", "female", "male", "female", "male"],
    "Age": [22, 35, 30, 45, 18, 28, 38, 50, 14, 60],
    "SibSp": [0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
    "Parch": [0, 0, 1, 0, 0, 0, 2, 0, 0, 0],
    "Ticket": ["A/5 21171", "PC 17599", "STON/O2. 3101282", "113803", "113783", "373450", "17463", "345763", "CA. 2343", "345764"],
    "Fare": [7.25, 71.28, 7.92, 53.1, 8.05, 8.45, 71.28, 8.05, 7.23, 8.05],
    "Cabin": [None, "C85", None, "C123", None, None, "E46", None, None, None],
    "Embarked": ["S", "C", "Q", "S", "C", "S", "C", "S", "Q", "S"],
}

# Create a DataFrame
titanic_data = pd.DataFrame(data)

# Display the first few rows
titanic_data.head()
# Checking for missing values and data types
titanic_data.info()

# Statistical summary of numerical features
titanic_data.describe()
# Dropping irrelevant columns: 'Cabin', 'PassengerId', and 'Name'
titanic_cleaned = titanic_data.drop(columns=["Cabin", "PassengerId", "Name"])

# Checking for duplicate rows
duplicates = titanic_cleaned.duplicated().sum()

# Display the cleaned dataset and duplicates count
titanic_cleaned, duplicates
