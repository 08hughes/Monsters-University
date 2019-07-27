# import
from student_class import *
from module_class import *
from batch_class import *


# create 6 students
student_mike = Student("Mike Wazowski",19, 2, ["Teamwork", "Camouflage if surrounding are green"], 1)
student_sully = Student("James P. Sullivan", 18, 2, ["Loud roar", "Quick"], 8)
student_randall = Student("Randall Bloggs", 18, 2, ["Expert camouflage", "Can walk on walls"], 6)
student_roz = Student("Roz", 45, 0, ["Piercing stare", "Intimidating"], 7)
student_waternoose = Student("Henry J. Waternoose III", 50, 6, ["Can walk on walls", "Craftiness"], 9)
student_squishy = Student("Squishy", 16, 2, ["Flexible", "Glows in dark"])

# create 4 modules
module_1 = Module("The art of the Scare", 10)
module_2 = Module("Scare History", 12)
module_3 = Module("Maths", 20)
module_4 = Module("The Jump Scare", 4)

# create 2 batches
batch_1 = Batch(module_1, "02/02/4851", [student_mike.name, student_sully.name, student_randall.name])
batch_2 = Batch(module_2, "09/09/3594", [student_roz.name, student_waternoose.name, student_squishy.name])

# add student to batch
name = input("Enter name: ")
age = input("Enter age: ")
legs = input("Enter number of legs: ")
skills = []
skills.append(input("Enter a skill: "))
scare_level = input("Enter scare level: ")

new_student = Student(name, age, legs, skills, scare_level)
print(new_student.student_id, new_student.name, new_student.skills)

# print modules

print(Module.list_modules())

# As a user I want to add a student monster to a workshop

# As a user I want to list all students in a batch

