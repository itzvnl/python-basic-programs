class Parent:
     def __init__(self):
          print("This is the parent class")
     def parentFunc(self):
          print("This is the parent func")

p = Parent()
p.parentFunc()


#Child Class 
class Child(Parent):
     def __init__(self):
          print("This is the Child Class")
     def childFunc(self):
          print("This is the Child func")
c = Child()
c.childFunc()

#Child calls the parent function
c.parentFunc()
          
