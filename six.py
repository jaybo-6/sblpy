class Person:
    def __init__(self, id, name):
        self.ID = id
        self.name = name

    def display(self):
        print("\nID =", self.ID)
        print("Name =", self.name)

class Student(Person):
    def __init__(self, id, name, sub1, sub2):
        super().__init__(id, name)
        self.sub1 = sub1
        self.sub2 = sub2

    def display(self):
        print("\nStudent ID =", self.ID)
        print("Student Name =", self.name)
        print("Marks in subject 1 =", self.sub1)
        print("Marks in subject 2 =", self.sub2)

class Sports:
    def showsports(self, s=None):
        self.sportsmarks = s
        if s is not None:
            print("\nSports marks =", self.sportsmarks)

class Result(Student, Sports):
    def __init__(self, id, name, sub1, sub2):
        super().__init__(id, name, sub1, sub2)

    def total(self):
        if self.sportsmarks is not None:
            total_marks = self.sub1 + self.sub2 + self.sportsmarks
        else:
            total_marks = self.sub1 + self.sub2
        print("\nTotal Marks =", total_marks, "\n")

print("Enter the student details:")
id = input("Enter Student ID: ")
name = input("Enter Student Name: ")
marks1 = int(input("Enter marks in the first subject: "))
marks2 = int(input("Enter marks in the second subject: "))

obj = Result(id, name, marks1, marks2)
obj.display()

choice = input("Do you want to enter sports marks? (y/n): ")
if choice.lower() == 'y':
    sports_marks = int(input("Enter sports marks: "))
    obj.showsports(sports_marks)
else:
    obj.showsports()

obj.total()
