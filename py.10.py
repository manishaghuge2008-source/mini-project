import math
import random
from datetime import datetime


history = {}


def save_result(operation, result):
    time = str(datetime.now())
    history[time] = {"Operation": operation, "Result": result}



def basic_calculator():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        ch = int(input("Choose operation: "))

        if ch == 1:
            res = a + b
            op = "Addition"
        elif ch == 2:
            res = a - b
            op = "Subtraction"
        elif ch == 3:
            res = a * b
            op = "Multiplication"
        elif ch == 4:
            res = a / b
            op = "Division"
        else:
            print("Invalid choice")
            return

        print("Result =", res)
        save_result(op, res)

    except Exception:
        print("Invalid input!")


# Scientific calculations
def scientific_calc():
    try:
        n = float(input("Enter number: "))

        sqrt_val = math.sqrt(n)
        power_val = math.pow(n, 2)

        print("Square root =", sqrt_val)
        print("Square =", power_val)

        save_result("Scientific", sqrt_val)

    except Exception:
        print("Invalid input!")


# Random numbers
def random_numbers():
    nums = [random.randint(1, 100) for _ in range(5)]
    print("Random Numbers:", nums)

    save_result("Random Numbers", nums)


# View history
def view_history():
    if not history:
        print("No history available")
    else:
        print("\n----- HISTORY -----")
        for t, data in history.items():
            print("Time:", t)
            print("Operation:", data["Operation"])
            print("Result:", data["Result"])
            print("-------------------")


# MAIN MENU
while True:
    print("\n====== SMART CALCULATOR ======")
    print("1. Basic Arithmetic")
    print("2. Scientific Calculation")
    print("3. Generate Random Numbers")
    print("4. View History")
    print("5. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            basic_calculator()
        elif choice == 2:
            scientific_calc()
        elif choice == 3:
            random_numbers()
        elif choice == 4:
            view_history()
        elif choice == 5:
            print("Program Ended")
            break
        else:
            print("Invalid choice!")

    except Exception:
        print("Please enter a valid number!")