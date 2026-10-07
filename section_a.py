num_students =int(input("Enter number of students: "))
while num_students <= 0:
    print("Please enter a number greater than 10.")
    num_students =int(input("Enter number of students: "))

    student_name =[]
    student_grades = []
    total_grade = 0

    # Loop through each student
    for i in range(num_students):
        print("Student", i + 1)
        name = input("Enter student name: ")

        # Simple grade entry with range validation
        grade = float(input("Enter grade (0-100): "))
        while grade < 0 or grade > 100:
            print("Invalid grade! Must be between 0 and 100.")
            grade = float(input("Enter grade (0-100): "))

            student_names.append(name)
            student_grades.append(grade)
            total_grade = total_grade + grade
        class_average = total_grade / num_students


        prin("RESULTS")
        print("Total Grade:", total_grade)
        print("Class Average:", round(class_average, 2))

        for i in range(num_students):
            print(student_names[i], "Grade:", student_grades[i], "Class Average:", round(class_average, 2))