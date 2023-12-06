import pandas as pd

# Creating a Pandas Series
series_data = pd.Series([10, 20, 30, 40])
print(series_data)

# Creating a Pandas DataFrame
data = {'Name': ['Nir', 'Hit', 'Ko', 'Nir'],
        'Age': [25, 30, 22, 52]}
df = pd.DataFrame(data)
print(df)

# Selecting a column by label
ages = df['Age']
print(ages)

# Selecting rows based on a condition
young_people = df[df['Age'] < 30]
print(young_people)

# Handling missing values
df.dropna()  # Drop rows with missing values
df.fillna(2)  # Fill missing values with a specified value
print(df)

# Applying transformations
df['Age'] = df['Age'] + 1  # Incrementing ages by 1
print(df)

# Grouping by a column and calculating the mean
average_age_by_name = df.groupby('Name')['Age'].mean()
print(average_age_by_name)

# Reading data from a CSV file
df = pd.read_csv('/content/iris_csv.csv')
df.head()

# Writing data to a CSV file
df.to_csv('new_iris.csv', index=False)
print("New data:")
df1 = pd.read_csv('/content/new_iris.csv')
df1.head()
