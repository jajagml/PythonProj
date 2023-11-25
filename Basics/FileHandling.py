# python - file handling

# open() - function responsible for opening a file for reading
# myFile = open("MyTextFile.txt", "r")
# myFile = open("MyTextFile.txt", "rt")  # open the file and returns file object
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# myFile = open("MyTextFile.txt", "rt") # read text
# print(myFile.read()) # returns the whole text
# print(myFile.read(8)) # specify how many characters you want to return
# print(myFile.readline())  # return one line only
# for line in myFile:
#     print(line)

# myFile = open("MyTextFile.txt", "a") # append
# myFile.write("\nI am the new line")

# myFile = open("MyTextFile.txt", "w") # write or overwrite
# myFile.write("\nI delete them all")

# myFile = open("myfile.txt", "w") # create new file if the specified file does not exist | w-write
# myFile = open("myfile.txt", "a") # create new file if the specified file does not exist same with Write from line 26 | a-append
# myFile = open("myfile.txt", "x") # create new file but return error if the file already existing | x-create

# myFile.close() # good practice to close the file


import os # this library is used to delete file

# os.remove("zzz.txt") # remove/delete file | remove
# os.rmdir("myfolder") # remove/delete folder | rmdr




