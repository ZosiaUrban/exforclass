#what is a constructor= properties of created objects
#class= data type that defines how to build an object
class Dog:
    #defining constructor self=talking abt object so self means object
    def __init__(self, name,age):
        self.name = name
        self.age = age
def __str__(self)
def change_name(self,name):
    self.name = name
    #characteristic of the object change to the new one that is provided

def get_name(self):
    return self.name
def get_age(self):
    return self.age

mydog=Dog("cocoa",20)
yourdog=Dog("mango",30)


print(f"Dogs name: {mydog.name} is {mydog.age} years old")
mydog.change_name("Shiter")
print(yourdog.name)

print(yourdog.getAge())
#string convert whatever is in mydog to a string
print(str(mydog))

