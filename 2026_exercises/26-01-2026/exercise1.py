
class Student:
    def __init__(self,name,student_id):
        self.__name = name
        self.__student_id = student_id
        self.__marks = []

    def add_marks(self,marks_list):
        self.__marks.extend(marks_list)
    def calculate_average(self):
        average = sum(self.__marks)/len(self.__marks)
        return average
    def to_string(self):
        return f"ID: {self.__student_id} | Name: {self.__name} | Average: {self.calculate_average():.2f}"
    


    



class StudentManager:
    def __init__(self):
        self.__file_name = r"2026_exercises\26-01-2026\students.txt"

    def save_student(self,student_object):

        with open(self.__file_name,'a',newline="") as f:
             f.write(student_object.to_string() +"\n")

    def read_student(self):
        with open(self.__file_name,"r") as f:
            for line in f:
                print(line)

student1 = Student("Ali Wangara", 2302518)
student1.add_marks([60, 70, 100])

manager = StudentManager()
manager.save_student(student1)
manager.read_student()


    
    


