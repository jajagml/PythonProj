import pandas as pd

myData = pd.read_csv('Pandas\\data2.csv')

# Convert to correct format
# to_datetime - will convert the specified column to date format, 
# include the format carefully
myData['Date'] = pd.to_datetime(myData['Date'], format = 'mixed', yearfirst = True)
print(myData.to_string())

# Removing rows
# to drop a value w/c is null, use dropna(subset=['Column'], inplace = True)
# subset is the column name where the null values is expected to occur, 
# once null value is found in the specific folder, the row will be remove from the dataframe
myData2 = pd.read_csv('Pandas\\data2.csv')
myData2.dropna(subset = ['Date'], inplace = True)
print(myData2.to_string())
