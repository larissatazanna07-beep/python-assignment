# Gradebook Management System (ICT201)

A python application for managing student grades in multiple subjects that was built incrementally from basic loops to nested dictionaries.
---

## Overview
This project was initially designed for ICT201 (Coursework 01) to monitor student's performance in various subjects, determine average grades for a particular subject as well as the class and a menu-driven interface to manage students' grades.

## Project Evolution
Section A (Scalars & Loops): Student management system that was built using basic loops and user input with validation (0-100), and calculation of average grades for a single subject and the whole class.
Section B (Lists & Tuples): An enhanced version of the previous section that allows the user to enter and store student's grades in multiple subjects (Math, English, Science) and determine average grades, min and max scores per class.
Section C (Dictionaries): A complete gradebook management system built using dictionaries that allows the user to add, update, delete and search student's grades in different subjects.

Quick Start
Prerequisites
Make sure that Python 3.x is installed in your computer.

Execution
Directly run each of the sections scripts you want to execute in your terminal or IDE (e.g. PyCharm):

Bash
# Running Section A
python section_a.py

# Running Section B
python Section_B.py

# Running Section C (Main)
python section_c.py
Quick Example (Section C)
Plaintext
GRADEBOOK SYSTEM - MAIN MENU (SEC C)
1. Add New Student
2. Update Student Grades
3. Remove Student
4. View Subject-Specific Grades
5. Search Student by Name
6. Exit
Select an option (1-6): 1

Enter student name to add: Alice
Entering grades for Alice:
Enter grade for Math (0-100): 85
Enter grade for English (0-100): 90
Enter grade for Science (0-100): 78
Successfully added Alice to the gradebook.

Key Features (Section C)

• Add Student: Adds a new student with default subject entries.

• Update Grades: Appends new marks to the selected subject.

• Remove Student: Removes the student record by their name.

• View Subject Grades: Views all the student’s marks for the desired subject.

• Search Record: Searches a student by name and calculates their subject and overall average.

• Input Validation: Prevents the program from crashing on wrong input, such as non-integer values and grades lower than 0 and higher than 100.

Quick start
Prerequisites
Python 3.x

Execution
Each section’s code can be run in a terminal or in a Python IDE (e.g., PyCharm):

Bash
# Run Section A
python section_a.py

# Run Section B
python Section_B.py

# Run Section C (Main System)
python section_c.py
Quick example (Section C)
Plaintext
GRADEBOOK SYSTEM – MAIN MENU (SEC C)
1. Add New Student
2. Update Student Grades
3. Remove Student
4. View Subject-Specific Grades
5. Search Student by Name
6. Exit
Select an option (1-6): 1

Enter student name to add: Alice
Entering grades for Alice:
Enter grade for Math (0-100): 85
Enter grade for English (0-100): 90
Enter grade for Science (0-100): 78
Successfully added Alice to the gradebook.
Section B (Lists & Tuples): Multi-subject support (Math, English, Science) implemented with tuples (“Name”, [Grades]), calculating the subject average and class min/max.
Section C (Dictionaries): The whole system is built using the dictionary type:
Python
gradebook = {
“Student Name”: {
“Math”: [85.0],
“English”: [90.0],
“Science”: [78.0]
},

Quick start
Prerequisites
Python 3.x

Execution
Each section’s code can be run in a terminal or in a Python IDE (e.g., PyCharm):

Bash
# Run Section A
python section_a.py

# Run Section B
python Section_B.py

# Run Section C (Main System)
python section_c.py
Quick example (Section C)
Plaintext
GRADEBOOK SYSTEM – MAIN MENU (SEC C)
1. Add New Student
2. Update Student Grades
3. Remove Student
4. View Subject-Specific Grades
5. Search Student by Name
6. Exit
Select an option (1-6): 1

Enter student name to add: Alice
Entering grades for Alice:
Enter grade for Math (0-100): 85
Enter grade for English (0-100): 90
Enter grade for Science (0-100): 78
Successfully added Alice to the gradebook.
