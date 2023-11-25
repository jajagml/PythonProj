# Condition if else where indentation is important

# If
if 500 > 100:
    print("500 is greater than 100")

if True:
    print("True expression")    

# else
a = 250.23
b = 674.23
if a < b:
    print("true expression: a < b")
else:
    print("false expression")

# elif is else if equivalent in c#
if a == 250.23:
    print("a = 250.23")
elif b == 250.23:
    print("b = 250.23")
else:
    print("all incorrect")

# one line if
if b == 674.23: print("b = 674.23")

# one line if else
mySum = "%0.02f" %(150 + 100.23) # this is to set the number to 2 decimal places
print(a) if a == float(mySum) else print(b) 

# one line if elif else
print(a) if a == float(mySum) else print(b) if b == float(mySum) else print("nothing")
# if a == float(mySum):
# 	print(a)
# elif b == float(mySum):
# 	print(b)
# else:
# 	print("nothing")

# While loop
# initialization
# while condition statement
# true expression
# iteration

# while sample
j = 0
while j < 4:
    print(j)
    j += 1

# while with if
k = 1
while k < 10:
    if k % 2 == 1:
        print("odd number")
    else:
        print("prime number")
    k += 1

# while with continue
k = 0
while k < 10:
    k += 1
    if k == 4:
        continue
    print(k)

# For loop
myList = ["Mobile legends", "Usagi Shima", "Monster Hunter", "Subway Surfer", "Antistress", "Genshin Impact",]
for l in myList:
    print(l)

# loop through letters
myGame = "Usagi"
for x in myGame:
    print(x)

# loop with break
for l in myList:
    if l == "Subway Surfer":
        break
    print(l)

# values from 1 to 6, but 6 is not included. 2 is the increment, default is 1 in increment
for j in range(1, 6, 2):
    print(j)

myList1 = ["1", "2", "3", "4", "5", "6",]
for x in myList:
    for y in myList1:
        print(x, y)

# pass - to avoid getting error for the for loop with no content


