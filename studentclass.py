class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks_list = []  

  
    def add_mark(self, mark):
        try:
            mark = float(mark)

       
            if mark < 0 or mark > 100:
                print("Invalid mark! Must be 0 to 100")
                return

            self.marks_list.append(mark)
            print("Mark added successfully")

        except ValueError:
            print("Invalid input! Please enter a number")

    def get_average(self):
        if len(self.marks_list) == 0:
            return 0
        return sum(self.marks_list) / len(self.marks_list)


    def display_info(self):
        print("\n--- Student Details ---")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks_list)
        print("Average:", self.get_average())





name = input("Enter student name: ")
roll = input("Enter roll number: ")

s1 = Student(name, roll)

n = int(input("How many marks to add? "))

for i in range(n):
    mark = input(f"Enter mark {i+1}: ")
    s1.add_mark(mark)


s1.display_info()