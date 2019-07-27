class Batch:

    def __init__(self, module, start_date, list_of_students = []):
        self.module = module
        self.start_date = start_date
        self.__list_of_students = list_of_students

    def add_student(self, student_name):
        return self.__list_of_students.append(student_name)

    def print_stu_list(self):
        return self.__list_of_students

