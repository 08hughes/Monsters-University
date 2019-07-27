from user_class import *
import random


class Student(User):

    student_id = 0
    all_students = []
    all_students_names = []

    def __init__(self, name, age, legs, skills = [], scare_level = 0):
        super().__init__(name, age, legs, scare_level)
        self.student_id = Student.student_id + 1
        self.skills = skills
        Student.student_id = self.student_id
        Student.all_students.append(self)
        Student.all_students_names.append(str(self.student_id) + "." + self.name)
