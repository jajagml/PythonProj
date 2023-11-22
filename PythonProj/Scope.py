def MyFunc():
    x = 1245
    print(x)
#print(x) 

# local scope - only belongs to the function/ method
# it can only be used inside the fuction/ method
# line 5 will return error since variable x only exist in MyFunc function

def myFunc1():
    y = "Hello"
    def mySubFunc1():
        x = "Hi"
        print(x + " " + y)
    #x = "Hola"
    mySubFunc1()   
myFunc1()

# line 15 will return error since x variable only exists in mySubFunc1
# line 14 - y can be acces in the func mySubFunc1 since they are both part of MyFunc1

k = 56
def myFunc2():
    print(k)
myFunc2()
print(k)
#global variable - created outside the function 
# k is global variable - it is used in line 24 and line 26

g = 67
def myFunc3():
    global g
    g = 25
myFunc3()    
print(g)

# global keyword lets you change the value of a global variable 
# if myFunc3 is not called from line 34, the value of g in line 38 will still be 67
# since myFunc3 is called, line 32 where global keyword was used, changed the value of g to 25
# line 35 output would be 25
