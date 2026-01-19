# Listst

number_list = [1,2,3,4,5,6]

print("First three numbers are: ",number_list[:3])
print("Last two numbers are: ",number_list[-2:])

number_list.append(7)
# number_list.remove(2)
print(number_list)

for number in number_list:
    print(number*2)

# TUPLES

subjects_tuple = ("math","English","swahili","science","CRE")

print("first subject: ",subjects_tuple[0],"\nlast subject: ",subjects_tuple[-1],"\nMiddle three subjects: ",subjects_tuple[1:4])

for subj_tuple in subjects_tuple:
    print(subj_tuple.lower())

# subj_tuple["math"] = "SOS"

# SETS

programming_sets = {"Python","Javascript","GO",'Python',"Ruby","Javascript"}

print("sets: ", programming_sets)
programming_sets.add("C#")
print("new_sets: ", programming_sets)
programming_sets.remove("Javascript")
print("removed_sets: ", programming_sets)

for loop_set in programming_sets:
    print(loop_set.upper())

# DICTIONARIES

student_info = {
    "Ali":[50,80,70,100] 
}

for key , value in student_info.items():
    print("Name: ", key, "total marks: ", sum(value), "Average marks: ", sum(value)/len(value))

student_info["Wangara"] = [60,70,80,90]
print(student_info)

student_info.pop("Ali")
print(student_info)
