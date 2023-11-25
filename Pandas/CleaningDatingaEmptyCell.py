import pandas as pd 

myVar = pd.read_csv('Pandas\\data1.csv')

# dropna() - by default returns new DataFrame, and will not change the original
newDataFrame = myVar.dropna()
print(newDataFrame)

# by changing original dataframe, inplace = True argument is used in dropna
# by using that argument, the dropna will not return a new dataFrame
myVar1 = pd.read_csv('Pandas\\data1.csv')
myVar1.dropna( inplace = True)
print(myVar1.to_string())

# fillna() - allows to replace empty cells with a value
myVar2 = pd.read_csv('Pandas\\data1.csv')
myVar2.fillna(130, inplace = True)
print(myVar2)

# replace specific column
# need to add the column header/name
myVar3 = pd.read_csv('Pandas\\data1.csv')
myVar3["Calories"].fillna(130, inplace = True)
print(myVar3)

# mean - will replace null values with the average value (the sum of all values divided by number of values)
myVar4 = pd.read_csv('Pandas\\data1.csv')
myVar4["Calories"].fillna(myVar4["Calories"].mean(), inplace = True)
print(myVar4)

# median = will replace null values with value in the middle, after sorting all values in ascending order.
myVar5 = pd.read_csv('Pandas\\data1.csv')
myVar5["Calories"].fillna(myVar5["Calories"].median(), inplace = True)
print(myVar5)

# mode - will replace null values with the value that appears frequently
myVar6 = pd.read_csv('Pandas\\data1.csv')
myVar6["Calories"].fillna(myVar6["Calories"].mode()[0], inplace = True)
print(myVar6)

#-----#








