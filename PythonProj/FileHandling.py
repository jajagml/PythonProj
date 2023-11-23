# python - file handling

# open() - function responsible for opening a file for reading
myFile = open("MyTextFile.txt", "r")
# myFile = open("MyTextFile.txt", "rt") - read the text
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# print(myFile.read(17))
print(myFile.readline())  # not working to be investigate
for line in myFile:
    print(line)

myFile.close() # good practice to close the file











