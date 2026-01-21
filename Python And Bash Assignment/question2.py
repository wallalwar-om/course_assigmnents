students = {}
while True:
    print("\nChoose an option:")
    print("1. Add a new student")
    print("2. Update a student's grade")
    print("3. Print all student grades")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        students[name] = grade
        print(f"{name}'s grade added.")
    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print(f"{name}'s grade updated.")
        else:
            print("Student not found!")
    elif choice == "3":
        print("\n--- Student Grades ---")
        if not students:
            print("No records available.")
        else:
            for name, grade in students.items():
                print(f"{name}: {grade}")
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
