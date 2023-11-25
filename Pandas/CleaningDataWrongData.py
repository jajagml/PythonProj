import pandas as pd

myData = pd.read_csv('Pandas\\data2.csv')

# wrong data doesn't need to be empty cells or wrong format, 
# wrong data can be noticiable when you observe the data.
#  Upon observing, you can build expectation if what it should be

# Replacing value
# syntax dtFrame.loc[row index of the data, 'Column name'] = new value
myData.loc[0, 'Duration'] = 23
print(myData.to_string())

# Replacing value for big data
# setting up rules for big data by using loops and conditions
myData1 = pd.read_csv('Pandas\\data2.csv')
for j in myData1.index:
    if myData1.loc[j, "Duration"] == 60:
        myData1.loc[j, "Duration"] = 61
print(myData1)

# Removing Rows
# using loop and condition
# using drop to remove the rows that satisfy the condition
myData2 = pd.read_csv('Pandas\\data2.csv')
for j in myData2.index:
    if myData2.loc[j, "Duration"] == 60:
        myData2.drop(j, inplace = True)
print(myData2)
