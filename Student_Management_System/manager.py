from student import Student
import json
import os

students_json = "Student_Management_System/data/students.json"

class StudentManager:
    # def __init__(self):
        
    def save_student(self,student):
        student_dict = {
             "ID": student.student_id,
             "name": student.name,
             "marks": student.marks

         }
        try:
            with open(students_json,"r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []
        except json.JSONDecodeError:
            data = []
        
        data.append(student_dict)

        with open(students_json,"w") as f:
            json.dump(student_dict,f,indent=4)
        


    def read_students(self):
            with open(students_json,'r') as f:
                json.load(f)
    
    def delete_student(self,name):
        with open(students_json,'w') as f:
            loader = json.load(f)
            del loader[name]
            



    
        
  
        