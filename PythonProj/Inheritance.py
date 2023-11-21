class AllArtists:
    def __init__(self, artistName, activeYear, genre):
        self.artistName = artistName
        self.activeYear = activeYear
        self.genre = genre

    def __str__(self):
        return f"Artist Name: {self.artistName} \nActive Year: {self.activeYear} \nGenre: {self.genre}"

class Artist1(AllArtists):
    pass

x = Artist1("Mark T", "2003", "Rock")
print(x)

# parent class is AllAlbums from line 1
# child class is the Artist1_Album from line 10 
# syntax on how to set a class as parent class- class childClassName(parentClassName): 
# the child class Artist1_Album used pass keyword. - it is used when you don't put any other properties or method to the class. 
# the child class inherited the __init__ function of the parent class 

#------#
class Artist2_Album(AllArtists):
    def __init__(self, epName, epRelease, epSales):
        self.epName = epName
        self.epRelease = epRelease
        self.epSales = epSales

    def __str__(self):
        return f"EP name: {self.epName} \nEP Release: {self.epRelease} \nEP Sales: {self.epSales}"

x = Artist2_Album("Twice2","2019","1.3 Billion USD")
print(x)
# parent class is AllAlbums from line 1
# child class is the Artist2_Album from line 23
# in this example, the child class override the __init__ function of parent class

#-----#
class Artist3_Album(AllArtists):
    def __init__(self, singleName, singleRelease, singleSales, artistName="Taylor Swift", activeYear = "2023", genre ="Pop"):
        self.singleName = singleName
        self.singleRelease = singleRelease
        self.singleSales = singleSales
        AllArtists.__init__(self, artistName, activeYear, genre)
x = Artist3_Album("Wildest Dream", "2022", "1 Million USD")
print(x)
# the sample above is to keep the inheritance from the parent class
# syntax - parentClassName(self, other arguments..), it should be part of def __init__ of the class

#-----#
class Artist4_Album(AllArtists):
    def __init__(self, singleName, singleRelease, singleSales, artistName="Ben & Ben", activeYear = "2023", genre ="Pop"):
        self.singleName = singleName
        self.singleRelease = singleRelease
        self.singleSales = singleSales
        super().__init__(artistName, activeYear, genre)

    def myFunc(self): 
        print("Artist:", self.artistName, " \tActive Year: ", self.activeYear, " \tGenre: ", self.genre)
        print("Single name:", self.singleName, "\tSingle Release: ", self.singleRelease, "\tSingle Sales: ", self.singleSales)

x = Artist4_Album("Limasawa Street", "2019", "1 Million PHP")
x.myFunc()
# the sample above used super() - will make all of the properties and methods of parent class to be inherited by child class
# don't forget to add self keyword if the function will be using the constructor 
