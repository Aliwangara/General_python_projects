

student_name_input = input("Enter student's name:  ")
number_of_subjects = int(input("Enter number of subjects:  "))

total = 0
for i in range(number_of_subjects):
    subjects_marks = float(input(f"Enter marks for subject {i+1}:  "))

    if subjects_marks < 0:
        continue
    elif subjects_marks > 100:
        break
    


    total += subjects_marks
average = total/number_of_subjects

if average >= 80:
    Grade = "A"
elif average >= 60:
    Grade = "B"
elif average >= 40:
    Grade = "C"

else:
    Grade = "Fail"

print("Name:",student_name_input )
print("Average Mark:", round(average,2))
print("Grade: ", Grade) 
