

def save_students(student_name,average_marks):

    with open("2026_exercises/19-01-2026/students.txt",'a',newline="") as f:
        writer = f.write(f"{student_name} - {average_marks}")

save_students("wangara", 70) 

