
import random

# Welcome message
print("=" * 40)
print("WELCOME TO MY PERSONAL MINI-TOOLKIT!")
print("=" * 40)


# TOOL 1: SIMPLE CALCULATOR
# Performs basic mathematical operations.
def calculator():
    print("\n--- SIMPLE CALCULATOR ---")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        operation = input("Enter your choice: ")

        if operation == "1":
            result = num1 + num2
            print(f"The answer is: {result}")

        elif operation == "2":
            result = num1 - num2
            print(f"The answer is: {result}")

        elif operation == "3":
            result = num1 * num2
            print(f"The answer is: {result}")

        elif operation == "4":
            if num2 != 0:
                result = num1 / num2
                print(f"The answer is: {result}")
            else:
                print("Sorry! You cannot divide by zero.")

        else:
            print("Invalid operation. Please try again.")

    except ValueError:
        print("Please enter valid numbers.")


# TOOL 2: TO-DO LIST
# Allows users to add, view and remove tasks.
def todo_list():
    tasks = []

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter your task: ")

            if task.strip():
                tasks.append(task)
                print(f"Task '{task}' added successfully!")
            else:
                print("Task cannot be empty.")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your to-do list is empty.")
            else:
                print("\nYour Tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if len(tasks) == 0:
                print("There are no tasks to remove.")
            else:
                print("\nYour Tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                try:
                    task_number = int(input("Enter task number to remove: "))

                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        print(f"Task '{removed_task}' removed successfully!")
                    else:
                        print("Invalid task number.")

                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            print("Returning to the main menu...")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3 or 4.")


# TOOL 3: NUMBER GUESSING GAME
# Challenges the user to guess a secret number.
def guessing_game():
    secret_number = random.randint(1, 10)
    attempts = 0

    print("\n--- NUMBER GUESSING GAME ---")
    print("I have chosen a number between 1 and 10.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 10:
                print("Please choose a number between 1 and 10.")

            elif guess < secret_number:
                print("Too low! Try again.")

            elif guess > secret_number:
                print("Too high! Try again.")

            else:
                print(f"Congratulations! You guessed correctly.")
                print(f"You used {attempts} attempts.")
                break

        except ValueError:
            print("Please enter a valid whole number.")


# MAIN MENU
# Keeps the program running until the user chooses Quit.
while True:
    print("\n========== MAIN MENU ==========")
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Number Guessing Game")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        calculator()

    elif choice == "2":
        todo_list()

    elif choice == "3":
        guessing_game()

    elif choice == "4":
        print("\nThank you for using my Personal Mini-Toolkit!")
        print("Goodbye and have a wonderful day!")
        break

    else:
        print(f"Sorry, '{choice}' is not a valid choice.")
        print("Please select a number between 1 and 4.")
