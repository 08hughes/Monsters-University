class Batch:

    batch_id = 0
    batch_record = []
    batch_record_names = []

    def __init__(self, module, start_date, list_of_students = []):
        self.batch_id = Batch.batch_id + 1
        self.module = module
        self.start_date = start_date
        self.__list_of_students = list_of_students
        Batch.batch_record_names.append(str(self.batch_id) + "."  + self.module)
        Batch.batch_record.append(self)
        Batch.batch_id = self.batch_id

    def add_student(self, student_name):
        return self.__list_of_students.append(student_name)

    def print_stu_list(self):
        return self.__list_of_students

