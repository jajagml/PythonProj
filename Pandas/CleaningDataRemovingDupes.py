import pandas as pd

myData = pd.read_csv('Pandas\\data1.csv')

# Remove duplicate
# duplicated() - it used to check for duplicate values
# will return True per row if duplicate value occur
print(myData.duplicated())

# Remove duplicate
# syntax: drop_duplicates(inplace = True)
# Note: inplace : bool, default False
#    Whether to modify the DataFrame rather than creating a new one.
myData.drop_duplicates(inplace = True)
print(myData.to_string())

