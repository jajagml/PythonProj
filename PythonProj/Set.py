# Set
# - is a collection which is unordered, unchangeable* and unindexed. No duplicate member
# can remove or add item
# Set uses {}
# cannot be access by index since set doesn't have index
mySet = {"Harry", "Ron", "Hermione", False, 1, 200} # 0 and false are treated the same # way 1
print(mySet)
mySet1 = set(("Fred", "George")) # way 2 using set()
print(mySet1)

# access Set
for x in mySet: # way 1
    print(x)
print("Harry" in mySet) #case sensitive

# Add Set
mySet.add("Draco") # way 1 # add 1 item
print(mySet)

addSet = ["Bella", "Molly"] # way 2, using update - can add list, tuple, dictionary in the set
mySet.update(addSet)
print(mySet)

# Remove Set item
mySet.remove("Ron")
print(mySet)
mySet.discard("xx") # will not return an error if the item is not in the list
print(mySet)
print(mySet.pop()) # remove random item, it will return the poppped item
mySet1.clear() # clears or empties the set
del mySet1 # delete the set intirely

# Join Set - it's like combining 2 sets 
jSet1 = {"Drama", "Action", "Comedy"}
jSet2 = {"Tragedy", "Slice of Life", "Drama"}
jSet3 = jSet1.union(jSet2)
print(jSet3)

# intersection_update() - will keep the items that are present in both sets.
jSet1.intersection_update(jSet2)
print(jSet1)

# intersection() - return new set consists of items present in both sets.
jset4 = jSet1.intersection(jSet2)
print(jset4)

# symmetric_difference_update() - keep all but not the duplicates
sduSet1 = {"Drama", "Action", "Comedy"}
sduSet2 = {"Tragedy", "Slice of Life", "Drama"}
sduSet1.symmetric_difference_update(sduSet2)
print(sduSet1)

# symmetric_difference - will create new list and keep all but not the duplicates
sduSet1 = {"Drama", "Action", "Comedy"}
sduSet2 = {"Tragedy", "Slice of Life", "Drama"}
sduSet3 = sduSet1.symmetric_difference(sduSet2)
print(sduSet1)


