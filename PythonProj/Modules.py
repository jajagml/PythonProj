# python module is file containing set of functions
# file extensiion .py
import MyModuleSample as modSample
import Inheritance
from Inheritance import AllArtists as artists
x = modSample.userInfo["DOB"]
print(x)

# MyModuleSample consists of dictionary 
# modSample represent the MyModuleSample in this file
# as - used to rename the imported module within this file

y = Inheritance.AllArtists(artistName = "Olivia", activeYear = "2023", genre = "Pop")
print(y)

# Inheritance consists of classes and functions 
# line 13 let's you called the Inheritance.AllArtists and sets the argument's parameters

artists.myFunc101()

# from line 5, from keyword lets you import only parts of the module
# in line 19, you can see that I access myFunc101 which is part of AllArtists class 
# AllArtists class was renamed as artists in this file 
