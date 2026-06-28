def student_database():
    students = {} 

    while True:
        print("\n===== STUDENT DATABASE MENU =====")
        print("1. Add Student")
        print("2. Search Student by Roll No")
        print("3. Display All Students")
        print("4. Exit")

        choice = input("Enter your choice: ")
 

        if choice == "1":
            try:
                roll = input("Enter roll number: ")

                if roll in students:
                    print("Student already exists!")
                    continue

                name = input("Enter name: ")
                age = int(input("Enter age: "))
                city = input("Enter city: ")

                students[roll] = {
                    "name": name,
                    "age": age,
                    "city": city
                }

                print("Student added successfully!")

            except ValueError:
                print("Invalid input! Age must be a number.")


        elif choice == "2":
            roll = input("Enter roll number to search: ")

            student = students.get(roll)

            if student:
                print("\n Student Found ")
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("City:", student["city"])
            else:
                print("Student not found!")

        
        elif choice == "3":
            if not students:
                print("No students found!")
            else:
                print("\n All Students ")
                for roll, info in students.items():
                    print("Roll No:", roll)
                    print("Name:", info["name"])
                    print("Age:", info["age"])
                    print("City:", info["city"])
                    print("----------------------")

        
        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")



student_database()