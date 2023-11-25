import pandas as pd

# Correlation - calculates the relationship between each column in the data set.
# the number varies from -1 to 1. 
# 1 - means perfect correlation, the time a value went up in the first column, the other one went up as well
# 0.9 - still a good correlation, however, if you increase one value, the other will probably incease as well. 
# -0.9 - still a good correlation, however, if you increase one value, the other will probably go down. 
# -1 - bad correlation, if one value goes up does not mean that the other will. 

myVar = pd.read_csv('Pandas\\data3.csv')
print(myVar.corr())
