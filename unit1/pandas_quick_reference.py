import pandas as pd

df = pd.read_csv('AmesHousing.csv')

# print(df.shape)    # Rows, Columns
# print(df.columns)  # Column names
# print(df.dtypes)   # Column types
#
# print(df.head())   # Preview the data itself
# print(df.tail())   # Preview the data itself
#
# print(df.isnull().sum())          # Missing values per column
#
# print(df.describe())              # Descriptive statistics for numeric columns
# print(df.describe(include='all')) # Descriptive statistics for all columns
# print(df['SalePrice'].describe()) # Descriptive statistics for given column
#
# print(df.duplicated().sum())      # Check for duplicates
# print(df.info())                  # Non-null counts per column

# print(df.corr(numeric_only=True))   # Correlation matrix, each-to-each
                                      # Correlation given column to others
# print(df.corr(numeric_only=True)['SalePrice'].sort_values(ascending=False))

