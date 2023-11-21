# polymorphism - means many form
# it refers to methods/functions/operators with the same name that can be executed on many objects or classes
class MyElements:
  def msgLog():
    print("Element msg log")

class Button(MyElements):
  def click():
    print("Button clicked.") # just representation
  
  def msgLog():
    print("Button msg log")

class Link(MyElements):
  def linkText():
    print("This is link text") # just representation
    
  def msgLog():
    print("Link msg log")  

class MyTextbox(MyElements):
  pass

myBtn = myButton()
myLink = MyLink()
myTextBox = MyTextbox()

for log in (myBtn, myLink, myTextBox):
  print(log.msgLog())

# msgLog() is the one that represents the polymorphism
# msgLog() is present in each of the child class but it has different implementation
# for class TextBox, it is using the msgLog from the parent class: MyElements 
# class Button and Link, has their own implementation of msgLog()
