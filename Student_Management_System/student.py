
class Student:
    def __init__(self,name,student_id):
        self.name = name
        self.student_id = student_id
        self.marks = []
    
    def add_marks(self,new_marks):
        self.marks.append(new_marks)

    def calculate_average(self):
        return sum(self.marks)/len(self.marks)

    def to_dict(self):

        return{
            "id": self.student_id,
            "marks":self.marks
        }
    def to_string(self):
        return f"ID: {self.student_id} | Name: {self.name} | Average: {self.calculate_average():.2f}"
        
