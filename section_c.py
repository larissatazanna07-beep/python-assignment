#  this is a Global dictionary that will store student records
# Section C: Gradebook Management System (Without Functions)

# Global dictionary to store student records
gradebook = {}

# Main interactive menu loop
while True:
    print(" GRADEBOOK SYSTEM - MAIN MENU ")
    print("1. Add New Student")
    print("2. Update Student Grades")
    print("3. Remove Student")
    print("4. View Subject-Specific Grades")
    print("5. Search Student by Name")
    print("6. Exit")

    choice = input("Select an option (1-6): ").strip()

    # OPTION 1: ADD NEW STUDENT
    if choice == "1":
        name = input("Enter student name to add: ").strip()

        if not name:
            print("Name cannot be empty! Try again.")
        elif name in gradebook:
            print(
                f"Student '{name}' already exists! Use the update option instead."
            )
        else:
            gradebook[name] = {}

            # Ask how many subjects to add
            while True:
                try:
                    num_subs = int(
                        input(
                            f"How many subjects do you want to add for {name}? "
                        )
                    )
                    if num_subs > 0:
                        break
                    print("Please enter a number greater than 0.")
                except ValueError:
                    print("Invalid input! Please enter a valid integer.")

            # Loop to enter custom subject names and grades
            for i in range(num_subs):
                subject = input(f"Enter name for Subject {i+1}: ").strip()
                while not subject:
                    print("Subject name cannot be empty.")
                    subject = input(f"Enter name for Subject {i+1}: ").strip()

                # Grade input validation
                while True:
                    try:
                        grade = float(
                            input(f" Enter grade for {subject} (0-100): ")
                        )
                        if 0 <= grade <= 100:
                            break
                        else:
                            print(
                                "Error! Grade must be between 0 and 100. Try again."
                            )
                    except ValueError:
                        print("Error! Please enter a valid number.")

                gradebook[name][subject] = [grade]

            print(f"Successfully added {name} to the gradebook.")

    # OPTION 2: UPDATE STUDENT GRADES
    elif choice == "2":
        name = input("Enter student name to update: ").strip()

        if name not in gradebook:
            print(f"Error: Student '{name}' not found. Try again.")
        else:
            existing_subjects = list(gradebook[name].keys())
            if existing_subjects:
                print(f"Subjects available for {name}: {existing_subjects}")

            subject = input(
                "Enter subject to update/add grade for: "
            ).strip()

            if not subject:
                print("Subject name cannot be empty!")
            else:
                # Grade input validation
                while True:
                    try:
                        grade = float(
                            input(f"Enter new grade for {subject} (0-100): ")
                        )
                        if 0 <= grade <= 100:
                            break
                        else:
                            print(
                                "Error! Grade must be between 0 and 100. Try again."
                            )
                    except ValueError:
                        print("Error! Please enter a valid number.")

                if subject in gradebook[name]:
                    gradebook[name][subject].append(grade)
                else:
                    gradebook[name][subject] = [grade]

                print(f"Updated {subject} grade for {name}.")

    # OPTION 3: REMOVE STUDENT
    elif choice == "3":
        name = input("Enter student name to remove: ").strip()

        if name in gradebook:
            del gradebook[name]
            print(f"Removed {name} from the gradebook.")
        else:
            print(f"Error: Student '{name}' not found in the record.")

    # OPTION 4: VIEW SUBJECT-SPECIFIC GRADES
    elif choice == "4":
        if not gradebook:
            print("Gradebook is currently empty!")
        else:
            subject = input(
                "Enter subject name to view (e.g., Math, English, Science): "
            ).strip()
            found = False

            print(f" ALL GRADES FOR SUBJECT: {subject}")
            for name, subjects_dict in gradebook.items():
                if subject in subjects_dict:
                    grades_list = subjects_dict[subject]
                    print(f" {name}: {grades_list}")
                    found = True

            if not found:
                print(f"No records found for subject: '{subject}'")

    # OPTION 5: SEARCH STUDENT BY NAME
    elif choice == "5":
        name = input("Enter student name to search for: ").strip()

        if name not in gradebook:
            print(f"Error: Student '{name}' was not found.")
        else:
            print(f" RECORD FOR {name.upper()}")
            total_marks = 0
            total_count = 0

            for subject, grades in gradebook[name].items():
                sub_avg = sum(grades) / len(grades) if grades else 0
                print(f"  {subject}: {grades} (Average: {sub_avg:.2f})")

                total_marks += sum(grades)
                total_count += len(grades)

            overall_avg = total_marks / total_count if total_count > 0 else 0
            print(f"  Overall Average: {overall_avg:.2f}")

    # OPTION 6: EXIT
    elif choice == "6":
        print("Exiting program... Goodbye!")
        break

    # INVALID SELECTION
    else:
        print("Invalid selection! Please pick a number from 1 to 6.")