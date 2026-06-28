def manage_marks():
    marks = [] 

    print("Enter marks of 5 subjects:")

    for i in range(5):
        try:
            mark = float(input(f"Enter mark {i+1}: "))
            marks.append(mark)
        except ValueError:
            print("Invalid input! Please enter numeric value only.")
            return 

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

   
    marks.sort(reverse=True)

   
    print("\n--- Results ---")
    print("Marks list (descending):", marks)
    print("Average:", average)
    print("Highest mark:", highest)
    print("Lowest mark:", lowest)


manage_marks()