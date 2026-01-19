
name = input("Enter Full name:  ")
age_input = int(input("Enter age:  "))
subjects_taken = int(input("Enter number of subjects taken:  "))
marks_scored = float(input("enter total marks scored: "))

average_marks = marks_scored/subjects_taken

if average_marks >= 50:
    print("Yes")
else:
    print("No")

if age_input > 18:
    print("Adult")
else:
    print("Minor")

