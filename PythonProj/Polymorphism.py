# polymorphism - means many form
# it refers to methods/functions/operators with the same name that can be executed on many objects or classes
class MyElements:
  def msgLog(self):
    print("Element msg log")

class myButton(MyElements):
  def click():
    print("Button clicked.") # just representation

  def msgLog(self):
    print("Button msg log")

class MyLink(MyElements):
  def linkText(self):
    print("This is link text") # just representation

  def msgLog(self):
    print("Link msg log")  

class MyTextbox(MyElements):
  pass

myBtn = myButton()
myLink1 = MyLink()
myTB = MyTextbox()

for log in (myBtn, myLink1, myTB):
  log.msgLog()

# msgLog() is the one that represents the polymorphism
# msgLog() is present in each of the child class but it has different implementation
# for class TextBox, it is using the msgLog from the parent class: MyElements 
# class Button and Link, has their own implementation of msgLog()
