# class - blueprint for creating objects
# python is OOP

class MyClass1:
    def __init__(self, subject, time, teacher):
        self.subject = subject
        self.time = time
        self.teacher = teacher

def myFunc():
    class1 = MyClass1("Math","2pm-3pm","Ms. Santos")

    print("Class subject: " + class1.subject)
    print("Class time: " + class1.time)
    print("Class teacher: " + class1.teacher)        

myFunc()
#-----#
class MyClass2:
    def __init__(self, subject, time, teacher):
        self.subject = subject
        self.time = time
        self.teacher = teacher
    
    def __str__(self):
        return f"Class subject: {self.subject} \nClass time: {self.time} \nClass teacher: {self.teacher}"
    
x = MyClass2("Science", "1pm-2pm", "Mr. Smith")
print(x)

# __init__ is function that was called automatically every time the class is being used to create object. 
# __str__ method that returns string representation of the object
# self parameter is a reference to the current instance of class, and is used to access variables that belongs to the class. 


