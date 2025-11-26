import json

storage_location = "storage/Students.json"


def save_to_file(data,file=storage_location):

    try:
        with open(file,'w') as f:
            json.dump(data,f,indent=4)
    except Exception as e:
        print("File not found",e)
    
def get_from_file(file=storage_location):
    try:
        with open(file,'r') as f:
            return json.load(f)
            
    except Exception as e:
        print("Failed to load data",e)
        return []
