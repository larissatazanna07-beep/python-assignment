#  this is a Global dictionary that will store student records
gradebook = {}

def get_valid_grade(prompt):
    # A Loop continuously until valid numeric input between 0 and 100 is provided
    while True:
        try:
            val = float(input(prompt))
            if 0 <= val <= 100:
                return val
            else:
                print("Error! Grade must be between 0 and 100. Try again.")
        except ValueError:
            print("Error! Please try enter a valid number.")


def add_student():

    name = input("Enter student name to add: ").strip()
    # Validate that name field is not empty
    if not name:
        print("Name cannot be empty! try again")
        return

    # Check if student already exists in dictionary to prevent which will prevent overwriting
    if name in gradebook:
        print(f"Student '{name}' already exists! Use the update option instead.")
        return

    gradebook[name] = {}

    subjects = ["Math", "English", "Science"]
    print(f"Entering grades for {name}:")
    # Loop through subjects and prompt user for initial grades
    for sub in subjects:
        grade = get_valid_grade(f" Enter grade for {sub} (0-100): ")
        # Store as a list of grades under the subject key
        gradebook[name][sub] = [grade]

    print(f" Successfully added {name} to the gradebook.")


def update_student():
    # Get student name to update
    name = input("Enter student name to update: ").strip()
    # Check if the student name  exists in gradebook
    if name not in gradebook:
        print(f"Error: Student '{name}' not found try again.")
        return
    # Show  the available subjects for  the selected student
    print(f"Subjects available for {name}: {list(gradebook[name].keys())}")
    subject = input("Enter subject to update/add grade for: ").strip()

    grade = get_valid_grade(f"Enter new grade for {subject} (0-100): ")

    if subject in gradebook[name]:
        gradebook[name][subject].append(grade)
    else:
        gradebook[name][subject] = [grade]

    print(f" Updated {subject} grade for {name}.")


def remove_student():
    # Get student name to remove
    name = input("Enter student name to remove: ").strip()
    # Delete the student entry from gradebook if key exists
    if name in gradebook:
        del gradebook[name]
        print(f" Removed {name} from the gradebook.")
    else:
        print(f"Error: Student '{name}' not found in the record.")


def view_subject_grades():
    # Check if the  gradebook is empty
    if not gradebook:
        print("Gradebook is currently empty!")
        return

    subject = input(
        "Enter subject name to view (e.g., Math, English, Science): "
    ).strip()
    found = False

    print(f" ALL GRADES FOR SUBJECT: {subject} ")
    # Loop through the dictionary items to filter grades by subject key
    for name, subjects_dict in gradebook.items():
        if subject in subjects_dict:
            grades_list = subjects_dict[subject]
            print(f" {name}: {grades_list}")
            found = True

    if not found:
        print(f"No records found for subject: '{subject}'")


def search_student():
    # Search for student record by the key name
    name = input("Enter student name to search for: ").strip()

    if name not in gradebook:
        print(f"Error: Student '{name}' was not found.")
        return

    print(f"RECORD FOR {name.upper()}")
    total_marks = 0
    total_count = 0

    for subject, grades in gradebook[name].items():
        sub_avg = sum(grades) / len(grades) if grades else 0
        print(f"  {subject}: {grades} (Average: {sub_avg:.2f})")

        total_marks += sum(grades)
        total_count += len(grades)

    overall_avg = total_marks / total_count if total_count > 0 else 0
    print(f"  Overall Average: {overall_avg:.2f}")


def display_menu():
    """Main menu loop for student management system."""
    while True:

        print("  GRADEBOOK SYSTEM - MAIN MENU (SEC C)")
        print("1. Add New Student")
        print("2. Update Student Grades")
        print("3. Remove Student")
        print("4. View Subject-Specific Grades")
        print("5. Search Student by Name")
        print("6. Exit")

        # Get the user option selection
        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            update_student()
        elif choice == "3":
            remove_student()
        elif choice == "4":
            view_subject_grades()
        elif choice == "5":
            search_student()
        elif choice == "6":
            print(" Exiting program... Goodbye!")
            break
        else:
            print("Invalid selection! Please pick a number from 1 to 6.")


if __name__ == "__main__":
    display_menu()