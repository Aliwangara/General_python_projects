import os

print(os.path.abspath("student.txt"))
print(os.path.exists(r"C:\Users\Wangara\Desktop\All_my_projects\Ali backend\General_python_projects\2026_exercises/26-01-2026/student_data/student.txt"))
print(os.path.getsize("2026_exercises/26-01-2026/student_data/student.txt"))
print(os.listdir(r"C:\Users\Wangara\Desktop\All_my_projects\Ali backend\General_python_projects\2026_exercises\26-01-2026\student_data"))
print("Removed:", os.remove(r"C:\Users\Wangara\Desktop\All_my_projects\Ali backend\General_python_projects\2026_exercises/26-01-2026/student_data/student.txt"))
print(os.rmdir(r"C:\Users\Wangara\Desktop\All_my_projects\Ali backend\General_python_projects\2026_exercises\26-01-2026\student_data"))