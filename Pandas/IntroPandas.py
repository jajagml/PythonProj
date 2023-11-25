# Pandas - python library for working with data sets
# functions for analyzing, cleaning, exploring, manipulating data
# pandas will give answers about the data like:
# Correlation between 2 columns
# Max value
# Min value 

import pandas as pd

dateSet1 = {
    'songs':["Feathers", "Clean", "Happier"],
    'rank' : ["1", "2", "3"]
}

pdVar = pd.DataFrame(dateSet1)
print(pdVar)
print(pd.__version__)

#-----#
# Series - is like a column in a table; it's a one-dimensional array holding data of any type. 

mySeries = [1, 23, 56]

myVar = pd.Series(mySeries)

print(myVar)
print(myVar[2]) # index is the default label if there is no specified label 

# wait what is label? it used to access a specified value/ it acts like an index in my opinion :P
myVar1 = pd.Series(mySeries, index = ["Label 1", "Label 2", "Label 3"])
print(myVar1)
print(myVar1["Label 2"])

# pandas series for dictionary 
myScores = {"Math": 85, "English": 86, "History": 87}
myVar2 = pd.Series(myScores)
print(myVar2)
myVar3 = pd.Series(myScores, index = ["Math", "English"])
print(myVar3) # the History part will only return the data type

# Data Frames = multi-dimensional tables; it's the whole table
mySemGrades = {
    "Semester":["1st Sem", "2nd Sem", "3rd Sem", "4th Sem"], #1st column
    "grades" : [85,91,82,88] #2nd column
}
myVar4 = pd.DataFrame(mySemGrades)
print(myVar4)
print(myVar4.loc[2]) # will display the index 2 column
print(myVar4.loc[[3,1]]) # will display the index 3 and index 1 column, remember [] within []

myVar5 = pd.DataFrame(mySemGrades, index = ["Sem 1", "Sem 2", "Sem 3", "Sem 4"])
print(myVar5) # print the data using the assigned index name, 
# number of index should match the number of rows, else it will return error
print(myVar5.loc["Sem 4"]) # locates the data with the index name Sem 4

myVar6 = pd.read_csv('Pandas\\times.csv') # read csv and load it to dataframe
print(myVar6)
# print(myVar6.to_string()) # return dataframe into string

myVar7 = pd.read_json('Pandas\\donut.json') # read json and load it to dataframe
print(myVar7)

myJson = {
    "Semester":{
        "Sem 1":"1st Sem",
        "Sem 2":"2nd Sem",
        "Sem 3":"3rd Sem",                
    },
    "Grade":{
        "Sem 1": 87,
        "Sem 2": 85,
        "Sem 3": 90
    }
}

myVar8 = pd.DataFrame(myJson) # loadin a data from python file
print(myVar8)

# Analyzing DataFrames 
# head() - returns the headers and specified number of row, starting from the top
# if no specified number of rows, it will return the first 5 rows
myVar9 = pd.read_csv('Pandas\\times.csv') # read csv and load it to dataframe
print(myVar9.head(10)) # display index 0 ~ 9 
print(myVar9.head()) # default display is 5 rows

# tail() - viewing the last rows of dataFrames
print(myVar9.tail(10)) # display index 0 ~ 9, starting from the bottom
print(myVar9.tail()) # default display is 5 rows, starting from the bottom

# info() - gives more information about the dataset
print(myVar9.info()) # display data typs, memory usage


