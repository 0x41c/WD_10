#!/usr/bin/python

class School:

    shared = None

    def __init__(self, name):
        if School.shared is not None:
            print("Cannot initialize a school when one is already defined")
            return School.shared
        self.name = name
        self.teachers = []
        School.shared = self
    
    def printDescription(self):
        print("Welcome to " + self.name)
        print("We have " + str(len(self.teachers)) + " staff!")
        print("Here they are:")
        for i in range(0, len(self.teachers)):
            ourTeacher = self.teachers[i]
            print("----------------------------------------------------------------")
            ourTeacher.introduceYourself()

class Teacher:

    def __init__(self, name):
        if School.shared is None:
            print("Cannot create a teacher when there is no school!")
            return None
        
        self.name = name
        self.students = []
        School.shared.teachers.append(self)

    def addStudent(self, student):
        if self.students.__contains__(student) is True: return
        self.students.append(student)

    def getStudentCount(self):
        return len(self.students)

    def introduceYourself(self):
        print("Hi! my name is " + self.name)
        print("I teach " + str(self.getStudentCount()) + " students!")
        for i in range(0, len(self.students)):
            student = self.students[i]
            print("----------------------------------------------------------------")
            student.displayDetails()



class Student:

    def __init__(self, name, age, graduatingYear, teacher):
        self.teacher = teacher
        self.name = name
        self.age = age
        self.gradYear = graduatingYear
        if teacher is not None:
            teacher.addStudent(self)

    def displayDetails(self):
        print ("Name:", self.name, " Age:", self.age, " Graduating Year:", self.gradYear)

# initiate shared school object
School("Kleos")
# create a teacher and assign students to it
myTeacher = Teacher("Ms, Chen")
Student("Me", 15, 2024,  myTeacher) # I pre-registered XD

someTeacherlessStudent = Student("Kat", 16, 2024, None)

myTeacher.addStudent(someTeacherlessStudent) # Fine you can have this teacher too Kat :eyeroll:

School.shared.printDescription() # Really ugly but whatever
