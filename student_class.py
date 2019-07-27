
# def stud
# inharit
# have monster id
# skills - list
from user_class import *
import random

class Student(User):

    def __init__(self, student_id, name, age, legs, scare_level = 0):
        super().__init__(name, age, legs, scare_level)
        self.student_id = student_id