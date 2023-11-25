# List 
# is a collection which is ordered and changeable. Allows duplicate members.
dtList = ["Song","Video", "Sound", "Dance", "Folklore"]

# Access list
print(dtList) # will display all items
print(dtList[1]) # will display item from index 1
print(dtList[-1]) # negative indexing means starts from the end. Will print the last item from the list
print(dtList[2:3]) # display range of indexes from specified index and stop at specified index(NOT INCLUDED)
print(dtList[:3]) # return the items from the start and stop at the specified index(NOT INCLUDED)
print(dtList[3:]) # return the items from the specified index to last
print(dtList[-3:-1]) # negative indexing means starts from the end. output: Video, Sound

# Change list item
dtListCl1 = ["Song","Video", "Sound", "Dance", "Folklore"]
dtListCl1[1:3] = ["Lover", "Ocean"] # [1] and [2] will be updated
print(dtListCl1)
# print(len(dtListCl1))

dtListCl2 = ["Song","Video", "Sound", "Dance", "Folklore"]
dtListCl2[3:4] = ["Lover", "Ocean"] # [3] will be updated, and Ocean will be inserted after [3] output: Song, Video, Sound, Lover, Ocean, Folklore
print(dtListCl2)

dtListCl3 = ["Song","Video", "Sound", "Dance", "Folklore"]
dtListCl3[1:3] = ["Lover"] # [1] and [2] will be replaced by Lover in the list. output: Song, Lover, Dance, Folklore 
print(dtListCl3)

# Add list item
listAdd1 = ["Instagram", "Threads", "Github"]
listAdd1.append("Facebook") # add item in the end of the list
print(listAdd1)
listAdd1.insert(0, "Tumblr") # will add item in the specified index
print(listAdd1)
listAdd2 = ["Viber", "Whatsapp"]
listAdd1.extend(listAdd2) # will combined 2 list
print(listAdd1)
tupleAdd = ("Messenger", "Teams") 
listAdd1.extend(tupleAdd) # can also combined list to dictionary, tuple, set
print(listAdd1)

# Remove list item
listRemove = ["Mobile legends", "Usagi Shima", "Monster Hunter", "Subway Surfer", "Antistress", "Genshin Impact", "Usagi Shima", "Usagi Shima"]
listRemove.remove("Genshin Impact") # remove specified text
print(listRemove)
listRemove.remove("Usagi Shima") # remove 1st occurence of the text
print(listRemove)
listRemove.pop(1) # remove specified index
print(listRemove)
listRemove.pop() # remove last item
print(listRemove)
del listRemove[3] # delete specified index, no mentioned index meaning deleting all items in the list
print(listRemove)
listRemove.clear() #clears or emptied the list
print(listRemove)

# Loop Lists 
loopList = ["Song","Video", "Sound", "Dance", "Folklore"]
for x in loopList: # way 1
    print(x)

for x in range(len(loopList)): # way 2
    myText = "{}: " + loopList[x]
    print(myText.format(x))

j = len(loopList) # way 3 starts at the end 
while j > 0:      
    j = j - 1
    myText = "[{}] : " + loopList[j]  
    print(myText.format(j))

[print(x) for x in loopList] # way 4 easiest way

# list comprehension
# newlist = [expression for item in iterable if condition == True]
compList = ["Instagram", "Threads", "Github", "Facebook", "Twitter"]
outCompList = [j for j in compList if "a" not in j] # will result a new list
print(outCompList)
# new list = [expression for item in iterable] - no condition
outCompList1 = [k for k in compList]
print(outCompList1)
# use range() - k is the divdend
outCompList2 = [k for k in range(5) if k % 2 == 1] # display odd numbers
print(outCompList2)
outCompList2 = [k for k in range(5) if k % 2 == 0] # display even numbers
print(outCompList2)
# expression
exList = [k.lower() for k in compList]
print(exList)
# expression with condition to manipulate the output
manList = [x if x is not "Instagram" else "Youtube" for x in compList]
print(manList)

# Sort list
sortList = ["song","Video", "Sound", "Dance", "folklore"]
# .sort() - will list alphabetically, all upper case letters are being sorted before the lower case letters
sortList.sort()
print(sortList)
# .sort(reverse = True) - descending order
sortList.sort(reverse = True)
print(sortList)
# .sort(key = sortList.lower) - will list alphabetically, regardless of the case 
sortList.sort(key = str.lower)
print(sortList)
# .reverse - reversing regardless of the alphabet
sortList.reverse()
print(sortList)


# copy list
copList = ["Instagram", "Threads", "Github"]    
copiedList = list(copList) # way 1
copiedList1 = copList.copy() # way 2
print(copiedList)
print(copiedList1)

# Join List
joinList = ["Instagram", "Threads", "Github"]
joinList1 = [123,45,67]
joinedList = joinList + joinList1 # way 1
print(joinedList)

joinList.extend(joinList1) # way 2
print(joinList)

joinList2 = ["Instagram", "Threads", "Github"]
for x in joinList2:
    joinList1.append(x)
print(joinList1)





