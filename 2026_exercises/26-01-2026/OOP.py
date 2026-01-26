

class Student:
    def __init__(self,name,student_id):
        self.__name = name
        self.__id = student_id
        self.__marks = []
    def add_marks(self, new_marks):
        self.__marks.append(new_marks)

    def calculate_average(self):
        average = sum(self.__marks)/len(self.__marks)
        return average
    def display_students(self):
        print(f"Name {self.__name}\nID: {self.__id}\nAverage marks {self.calculate_average():.2f}")

student1 = Student("Ali wangara",2275)

student1.add_marks(50)
student1.add_marks(70)
student1.add_marks(80)
student1.add_marks(100)

student1.display_students()
