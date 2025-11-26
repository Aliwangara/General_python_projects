from models.student import Student
from storage.storage_file import save_to_file,get_from_file
from datetime import date


def add_student():
    student_id = input("Enter Students Id:  ")
    name  = input("Enter students name:  ")
    dob = input(f"Enter {name}'s Date of birth:  ")
    gender = input(f"Enter {name}'s gender: ")
    admission_date = input(f"What is {name}'s admission date:  ")
    notes = input("Enter Notes:  ")

    student = Student(student_id,name,dob,gender,admission_date,notes)
    student_dict = student.to_dict()
    existing_students = get_from_file()
    existing_students.append(student_dict)
    save_to_file(existing_students)

def list_students():
    get_data = get_from_file()
    for i, student in enumerate(get_data,1):
        print(f"{i}.{student}")

def view_details():
    name = input("Enter name of the student to get details:   ").lower()

    get_data = get_from_file()

    for student in get_data:
        if name in student.get("Name").lower():
            print(student)
        else:
            print("Student not available")

def delete_student():
    get_data = get_from_file()
    student_id = input("Enter Student Id for the student you want to delete:  ").strip()

    for i, student in enumerate(get_data):
        # print(f"{i}.{student}")  
        if student.get("Student_Id") == student_id:
           removed =  get_data.pop(i)
           print("Removed", removed)
           break
    save_to_file(get_data)
           
        

   

    
    

while True:
    print("1. Add student")
    print("2. View students")
    print("3.View individual detail")
    print("4. Delete student")
    print("5. Exit")
    choice = int(input("Choose an option from the ones above:  "))

    if choice == 1:
        add_student()
    elif choice == 2:
        list_students()
    elif choice == 3:
        view_details()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        break
    else:
        print("Please select options from the one below!")



