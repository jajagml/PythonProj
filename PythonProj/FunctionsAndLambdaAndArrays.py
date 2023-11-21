# function - block of code that only runs when it is called. 
# def - use in creating function in python

# defining a function
def myFunction():
    print("My first function in Python")

# calling a function
myFunction()

# function with arguments - use to pass information in to function
def myFuncWithArgs(myName, myAge):
    print("My name: " + myName + "\nMy age: " + myAge)

myFuncWithArgs("Anne", "54")

# function with arguments and return
def myFuncWithArgsAndReturns(myName, myAge, x, y):
    print("My name: " + myName + "\nMy age: " + myAge)
    return x * y

print(myFuncWithArgsAndReturns("Kris", "23", 10, 5))

# function with unknown number of args is using * before the argument name
# this will return a tuple of arguments
def myFuncUnknownArgs(*myArgs):
    print("My arguments: " + myArgs[2])

myFuncUnknownArgs("Args1", "Args2", "Args3")

# function with unknown number of args is using ** before the argument name
# this will return a dictionary of arguments
def myFuncUnknownArgsDictionary(**myArgs):
    print("My arguments: " + myArgs["fname"])
    print("My arguments: " + myArgs["lname"])

myFuncUnknownArgsDictionary(fname = "Minnie", lname = "Mouse")

# default parameter
def myFuncDefParam(defParam = "My param"):
    print(defParam)

myFuncDefParam()
myFuncDefParam("Your param") # default param can be replace

# --------------------------
# Lambda - small anonymous function, it can take any number of arguments but can only have 1 expression
# lambda arguments : expression
myLambda = lambda a, b : a * b
print(myLambda(4,5))

# --------------------------
# Arrays - does not have built-in support for arrays, but List can be used instead.
# if need to use array, import NumPy library
# arrays used to store multiple values on a single variable

myArray = ["QA1", "QA2", "QA3", "QA4"]
print(myArray[3])
# get the length of the array
print(len(myArray))
# loop across array 
for array in range(len(myArray)):
    printThis = "[{0}] : " + "{1}"
    print(printThis.format(array, myArray[array]))

# add array elements
myArray.append("QA1")
print(myArray)
# remove array elements
myArray.pop(4) # remove the item based on specified index
print(myArray)
myArray.remove("QA3") # remove the item based on specified text
print(myArray)

