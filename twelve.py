import pandas as pd

# Creating a Data Series
data_series = pd.Series([85, 92, 78, 96], name='Marks')
print("Data Series:")
print(data_series)

# Creating a DataFrame from a Dictionary
data = {
    'Name': ['jay', 'bee', 'tay', 'z'],
    'ID': [101, 102, 103, 104],
    'Location': ['navi mumbai', 'mumbai', 'thane', 'navi mumbai'],
    'Marks': [85, 92, 78, 96]
}

df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)

# Accessing Specific Rows and Columns
print("\nAccessing specific rows and columns:")
print(df['Name'])         # Access the 'Name' column
print(df['Marks'])        # Access the 'Marks' column
print(df.loc[2])           # Access the row at index 2

# Adding a New Column
df['Grade'] = ['A', 'A', 'B', 'A']
print("\nDataFrame with a new 'Grade' column:")
print(df)

# Filtering Data Based on Conditions
print("\nFiltering data based on conditions:")
high_marks = df[df['Marks'] > 90]
print("Students with marks > 90:")
print(high_marks)

location_filter = df[df['Location'] == 'navi mumbai']
print("Students from navi mumbai:")
print(location_filter)
