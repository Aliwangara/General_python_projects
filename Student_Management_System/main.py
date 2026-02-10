from student import Student
from manager import StudentManager


def create_student(name,student_id):
    return Student(
        name,
        student_id
    )


def add_marks(student, new_marks):
    marks = new_marks.split(",")
    marks = [int(m.strip()) for m in marks]
    student.add_marks(marks)


def save_marks(student):
  student_manager = StudentManager()
  student_manager.save_student(student)

    
    



while True:
    name = input("Enter Student's name:  ").lower().strip()
    student_id = input("Enter students id:  ").strip()
    new_marks = input("Enter marks for three subjects (use , to split):  ").strip()

    student = create_student(name,student_id)

    
    add_marks(student, new_marks)
    save_marks(student)




