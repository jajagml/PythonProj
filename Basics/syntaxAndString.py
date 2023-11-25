
# syntax 
# print
print("Hello World")

# indentation
a = 1
b = 2
if a == b:
    print("a is equal to b")
else:
    print("a is not equal to b")

# Comments in Python
# first type is using "#"
""" 2nd type is 3 " for
multiple line of comments
"""

# Casting
x = 4.12345       # x is of type int
#x = "John Doe" # x is now of type str
print(str(x))
print(int(x))
print(float(x))

# Variable naming
myVar = "python variable starts with alphabet"
_myVar = "python variable starts with underscore"
# it cannot be start with numbers
_my_Var_1 = "python variable can only contain with alpha-numeric characters and underscore"
# it cannot be any of the python keywords
# case-sensitive myVar and MYVar are 2 different variables

# Assignment: mulitple values to multiple variables 
# variables are separated by comma ,
firstName, middleName, lastName = "James", "Smith", "Doe"
print(firstName) # output: James
print(middleName) # output: Smith
print(lastName) # output: Doe

# Assignment: one value to multiple variables
# variables using equal sign =
a = b =c = "Software Engineer"
print(a) #output: "Software Engineer"
print(b) #output: "Software Engineer"
print(c) #output: "Software Engineer"

# Assignment: collection of values in a list
# indicator []
myGrades = [90, 87, 88]
math, english, history = myGrades
print(math)
print(english)
print(history)

# Output variable 
bx = 4
bv = "John"
bn = bx , bv
print(bx , bv)

# Global variables - created outside the function
myVar_1 = "I'm a global variable"

def myFunc():
# Local variable - can be the same name as global variable but can only be used inside its function
    myVar_1 = "I'm a local variable"
    print(myVar_1)

myFunc()
print(myVar_1)

# String: multiline strings

myStr1 = """ I am a multi-line
string. using 3 double quotes"""

myStr2 = '''I am a multi-line string. 
I am using 3 single quotes'''

print(myStr1)
print(myStr2)

# Slicing
# index always starts with 0
# returns the characters from of specify range. Where to start and where to end the range.
# In this case, it will start at [2] and stop [9], end of the range is NOT INCLUDED . eg:
# [0][1][2][3][4][5][6][7][8][9][10][11]
# [C][r][u][e][l][ ][S][u][m][m][e] [r]
strSlicing = "Cruel Summer"
print(strSlicing[2:9] + "-----------------------------------") # uel Sum

# Slicing from the start and end to the specific position(NOT INCLUDED). eg.
print(strSlicing[:8]) # Cruel Su

# Slicing from the specific postion to the end of the string. eg.
print(strSlicing[4:]) # l Summer

# Slicing: Negative indexing starts the slicing from the end of the string. 
# e.g. slicing starts at [-6] and ends in [-3] which is NOT INCLUDED in the output
# [-12][-11][-10][-9][-8][-7][-6][-5][-4][-3][-2][-1]
# [C]  [r]  [u]  [e] [l] [ ] [S] [u] [m] [m] [e] [r]
print(strSlicing[-6:-3]) # Sum

# Modify Strings
strMS = " Video- Games "
print(strMS.upper()) #uppercase
print(strMS.lower()) #lowercase
print(strMS.strip()) # strip - removes whitespace before and after the text
print(strMS.replace("Video", "Mobile")) # replace the character with new character note: case-sensitive
print(strMS.split("-")) # splits the string to substring if it finds the separator, in this case, it is -

# Concatenation 
strC = "Mountain Dew"
print("Diet" + " " + strC)

# Format
strF1 = "Flamingo pink"
strF2 = "Aquamarine"
strF3 = "moonlit"
strLyrics = """{0}, Sunrise Boulevard
Clink, clink, being this young is art
{1}, {2} swimming pool
What if all I need is you?"""
print(strLyrics.format(strF1, strF2, strF3))

# Escape characters - just like in c#, using backslash \
print("\"The waiting is a sadness\" \n\'Fading into madness\'")

# String Method
strSM = "My empty pockets"
print(strSM.casefold()) # casefold - converts string to lower case
print(strSM.endswith("pockets")) # endswith - returns true if the string ends with specified value
print(strSM.find("empty")) #return the position of the specified value
print(strSM.index("pockets")) #returns the index position of specified value

strSMTuple = ("JamesSmith","JamesDean","JamesDoe")
print(" ".join(strSMTuple))

