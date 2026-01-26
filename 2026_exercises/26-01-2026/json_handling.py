import json

students_file = r"C:\Users\Wangara\Desktop\All_my_projects\Ali backend\General_python_projects\2026_exercises\26-01-2026\students.json"


students = {
    "Ali": {"id": 2302518, "marks": [60, 70, 100]},
    "Wangara": {"id": 2302519, "marks": [80, 90, 75]}
}

with open(students_file,'w') as f:
    json.dump(students,f,indent=4)

def read_students_json():
    with open(students_file,'r') as f:
        loader =  json.load(f)

        for key, value in loader.items():
            print(f"Name: {key}\nID {value['id']}\nAvg_marks {sum(value['marks'])/len(value['marks']):.2f}\n")
read_students_json()