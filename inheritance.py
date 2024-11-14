#study types of inheritance for quiz
#singeling inheritance
#class person with age name and gender, student class only student id

class Person:
  counter=0
  def __init__(self, name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        Person.counter=+1
        # keeps track of how many people are created

    def intro(self):
        print(f"Hello my name is {[self.name]} my age is {self.age} my gender is {self.gender}")

  def information(self):
    print(self.name,self.age,self.gender,self.counter)

class Student(Person):
    def __init__(self, name,age,gender,idnum):
        self.id = idnum
        super().__init__(name,age,gender)
        self.idnum=idnum
class Assitant(Student):
    def __init__(self, name,age,gender,idnum,salary):
        super().__init__(name, age, gender,idnum)
        self.salary=salary

class Teacher(Person):
    def __init__(self, name,age,gender,empnum):
       self.empnum=empnum
class Parttime(Assitant, Teacher):
    def __init__(self, name,age,gender,idnum,salary,time):
        super().__init__(name,age,gender,idnum,salary)
        self.time=time


teachers=[]
t1=Teacher("Ms Be",76,"f",4)
t2=Teacher("Ms Bu",66,"f",9)

teachers.append(t1)
teachers.append(t2)

for teacher in teachers:
    print(teacher.intro)

a1=Assitant("Becky",24,"female",2,300)
p1=Person("pegger",420,"female")
s1=Student("John",23,"Male",1)
print(s1.id,s1.name,s1.age,s1.gender)
print(p1.name,p1.age,p1.gender)
print(a1.name,a1.age,a1.gender,a1.idnum,a1.salary)
