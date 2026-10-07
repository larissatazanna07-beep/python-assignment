

num_students = int(input("Enter number of students: "))
while num_students <= 0:
    print("Please enter a number greater than 0.")
    num_students = int(input("Enter number of students: "))

subjects = ["Math", "English", "Science"]
students_data = []


for i in range(num_students):
    print("Student", i + 1)
    name = input("Enter student name: ")

    math_grade = float(input("Enter Math grade (0-100): "))
    while math_grade < 0 or math_grade > 100:
        print("Grade must be between 0 and 100!")
        math_grade = float(input("Enter Math grade (0-100): "))

    eng_grade = float(input("Enter English grade (0-100): "))
    while eng_grade < 0 or eng_grade > 100:
        print("Grade must be between 0 and 100!")
        eng_grade = float(input("Enter English grade (0-100): "))

    sci_grade = float(input("Enter Science grade (0-100): "))
    while sci_grade < 0 or sci_grade > 100:
        print("Grade must be between 0 and 100!")
        sci_grade = float(input("Enter Science grade (0-100): "))


    grades_list = [math_grade, eng_grade, sci_grade]
    student_tuple = (name, grades_list)
    students_data.append(student_tuple)


math_all = []
eng_all = []
sci_all = []

for student in students_data:
    math_all.append(student[1][0])
    eng_all.append(student[1][1])
    sci_all.append(student[1][2])




for student in students_data:
    s_name = student[0]
    s_grades = student[1]
    s_avg = sum(s_grades) / len(s_grades)
    print(s_name + str(s_grades[0])  + str(s_grades[1]) +  str(s_grades[2]) +  str(
        round(s_avg, 2)))

print("Highest" + str(max(math_all))  + str(max(eng_all)) +  str(max(sci_all)))
print("Lowest" + str(min(math_all)) + str(min(eng_all)) + str(min(sci_all)))