# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Tuple is a variable that can contain multiple items
# built-in data types in Python
# Tuple items are ordered, unchangeable, and allow duplicate value. 
# Since it was indexed, it allows duplicate value
# one item tuple should still have a comma
# tuple can have multiple data types values

imTuple = ("Theo", "Taiga", "Chonky", "Cow", "Gray", 1 , 2, True)
print(type(imTuple))

print(imTuple[4]) # access via index
# negative indexing - access starts at the end
print(imTuple[-1])
print(imTuple[-6])

# return the items based on the specified starting index up to specified end index. end index is not included
print(imTuple[3:7])

# return the items from the starting index up to specified end index. end index is not included
print(imTuple[:3])

# return the items based on the specified starting index up to end index.
print(imTuple[3:])

imTuple = ("Theo", "Taiga", "Chonky", "Cow", "Gray", 1 , 2, True)

# return the items based on the specified starting index up to specified end index. - BUT REVERSE, end index is not included
print(imTuple[-7:-3])

# return the items from the starting index up to specified end index. - BUT REVERSE, end index is not included
#print(imTuple[:-2])

# return the items based on the specified starting index up to end index. - BUT REVERSE
# print(imTuple[-3:])

# Work around to change tuple
# convert tuple to list, and convert it back to tuple after the update
imTuple = ("Theo", "Taiga", "Chonky", "Cow", "Gray", 1 , 2, True)
listTuple = list(imTuple)
listTuple[5] = False
imTuple =tuple(listTuple)
print(imTuple)
# add via converting to list and then convert it back to tuple after the add
listTuple.append("Chonky~yahh")
imTuple = tuple(listTuple)
print(imTuple)
# can add tuple to tuple 
addTuple = ("Kittens", "Cat")
imTuple += addTuple
print(imTuple)

# remove tuple item: converting to list and then convert it back to tuple after the remove
listTuple = list(imTuple)
listTuple.remove("Cat")
imTuple = tuple(listTuple)
print(imTuple)

# del - will delete intire tuple - if print it will result as error 

# Unpacking tuple
# tuple items should match the variables to be assigned in to
unpTuple = ("Theo", "Taiga", "Chonky")
(cat1, cat2, cat3) = unpTuple
print(cat1 + " " + cat2 + " " + cat3)

# add * to make the variable as a list, in the example below, the third variable will have the last item from the tuple
unpTuple += addTuple
(cat1, *cat2, cat3) = unpTuple
print(cat1 + " "  + " " + cat3)

# Loop tuple
lpTuple = ("Theo", "Taiga", "Chonky", "Cow", "Gray")
for j in lpTuple:
    print(j)

for j in range(len(lpTuple)):
    print(j)

i = 0
while i < len(lpTuple):
    printThis = "[{}]: " + listTuple[i]
    print(printThis.format(i))
    i += 1

# Join Tuple
tuple1 = ("Theo", "Taiga", "Chonky", "Cow", "Gray")
tuple2 = ("Teo", "Monette", "Margaret", "Moneng")
sumTuple = tuple1 + tuple2
print(sumTuple)
prodTuple = tuple1 * 2
print(prodTuple)
