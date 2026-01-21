

def save_students(student_name,average_marks):

    with open("2026_exercises/19-01-2026/students.txt",'a',newline="") as f:
        
        average_marks = sum(average_marks)/len(average_marks) 
        writer = f.write(f"{student_name} - {average_marks}\n")


def read_students():
    with open("2026_exercises/19-01-2026/students.txt", 'r') as f:
        for line in f.readlines():
            print(line.strip())


save_students("Ali", [20,30,40,50]) 

read_students()
