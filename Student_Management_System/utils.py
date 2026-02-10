import os

file_path = "data/students.json"
def file_exists(file_path ="data/students.json"):
    os.path.exists(file_path)

file_exists()

def get_file_size(file_path="data/students.json"):
    os.path.getsize(file_path)

get_file_size()