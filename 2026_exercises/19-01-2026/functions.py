
def calculate_average(number_list):

    return sum(number_list)/len(number_list)



def student_result(student_name,marks_list):

    average_function = calculate_average(marks_list)

    if average_function >=80:
        result = "A"
    elif average_function >=60:
        result = "B"
    elif average_function >=40:
        result = "C"
    else:
        result = "FAIL"

    print(f"Name: {student_name}, Average: {average_function:.2f}, Grade: {result}") 


list_marks = [40,70,80,90]

student_result("Ali wangara",marks_list=list_marks)