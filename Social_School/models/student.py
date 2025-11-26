


class Student:
    def __init__(self,student_id,name,dob,gender,admission_date,notes):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob
        self.__gender = gender
        self.__admission_date = admission_date
        self.__notes = notes
        self.__attendance = []
        self.__grades = {}

    def to_dict(self):
        return{
            "Student_Id": self.__student_id,
            "Name": self.__name,
            "DOB": self.__dob,
            "Gender": self.__gender,
            "Admission_date": self.__admission_date,
            "Notes": self.__notes,
            "Attendance": self.__attendance,
            "Grades": self.__grades
        }
    def from_dict(self,data):
        self.__student_id = data["Student_Id"]
        self.__name = data["Name"]
        self.__dob = data["DOB"]
        self.__gender = data["Gender"]
        self.__admission_date = data["Admission_date"]
        self.__notes = data["Notes"]
        self.__attendance = data.get("Attendance", [])
        self.__grades = data.get("Grades", {})


        