#math - built-in math functions

myNum1 = 120.23
myNum2 = 54.34

print(min(myNum1, myNum2))
print(max(myNum1, myNum2))
print(abs(-11.223))

# math module - extended list of mathematical functions
import math
print(math.sqrt(9)) # square root
print(math.ceil(45.87)) # ceiling
print(math.floor(45.87)) # floor

#----#
# JSON - syntax for storing and exchanging data
# JavaScript object notation
# python built-in package for json
import json
myJson = '{"albumName":"Paradise", "Artist" : "Lana", "Singles": [{"songName": "My song 1"}, {"songName": "My song 2"}]}'

# parsing
parsed = json.loads(myJson) # remember loads as in with s
print(parsed["Singles"][1]) # output: My song 2

# converting python object to json using dumps()
#dict, list, tuple, string, int, float, True, False, None
imTuple = ("Theo", "Taiga", "Chonky", "Cow", "Gray", 1 , 2, True)

imJson = json.dumps(imTuple)
print(imTuple)


# try except else finally
try:
    print(vc)
except NameError: # the possible error to be detected is defined
    print("undefine variable")
except: # undefine error detected
    print("error occurred")
else: # will run if there is no error detected
    print("no error detected")
finally: # this will execute regarless if there's an error or none 
    print("This try and except happenned")