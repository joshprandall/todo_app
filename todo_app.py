# todo_app.py
"""
A simple To-Do List Application that allows the user to:
    - Add tasks
    - View tasks
    - Delete tasks
    - Quit the application

Tasks are stored in a Python list. 
Error handling is implemented to manage invalid inputs and operations.
"""

def add_task(tasks):
    """
    Prompts the user to add a new task and appends it to the tasks list.
    Raises an error if the task is empty.
    """
    try:
        task = input("Enter the new task: ").strip()
        if not task:
            raise ValueError("Task cannot be empty.")
    except ValueError as e:
        print("Error:", e)
    else:
        tasks.append(task)
        print(f"Task '{task}' added successfully.")
    finally:
        print("Finished processing add task.\n")


def view_tasks(tasks):
    """
    Displays all tasks in the list.
    Raises an error if there are no tasks to view.
    """
    try:
        if not tasks:
            raise ValueError("No tasks to view.")
    except ValueError as e:
        print("Error:", e)
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    finally:
        print("Finished processing view tasks.\n")


def delete_task(tasks):
    """
    Prompts the user to delete a task by number.
    Raises an error if the tasks list is empty, if the input is invalid,
    or if the specified task does not exist.
    """
    try:
        if not tasks:
            raise ValueError("No tasks to delete.")
        # Show tasks to choose from
        view_tasks(tasks)
        task_number = input("Enter the task number to delete: ").strip()
        if not task_number.isdigit():
            raise ValueError("Invalid input. Please enter a valid task number.")
        task_index = int(task_number) - 1
        if task_index < 0 or task_index >= len(tasks):
            raise IndexError("Task number out of range.")
    except ValueError as ve:
        print("Error:", ve)
    except IndexError as ie:
        print("Error:", ie)
    else:
        removed = tasks.pop(task_index)
        print(f"Task '{removed}' has been deleted successfully.")
    finally:
        print("Finished processing delete task.\n")


def main():
    """
    Main function that runs the CLI loop.
    It displays a menu and performs operations based on user input.
    """
    tasks = []  # Storage for tasks
    print("Welcome to the To-Do List Application!")
    
    while True:
        try:
            print("\nMain Menu:")
            print("1. Add task")
            print("2. View tasks")
            print("3. Delete task")
            print("4. Quit")
            choice = input("Enter your choice (1-4): ").strip()
            
            # Validate menu choice
            if choice not in ['1', '2', '3', '4']:
                raise ValueError("Invalid option. Please choose between 1 and 4.")
            
            if choice == '1':
                add_task(tasks)
            elif choice == '2':
                view_tasks(tasks)
            elif choice == '3':
                delete_task(tasks)
            elif choice == '4':
                print("Thank you for using the To-Do List Application. Goodbye!")
                break

        except ValueError as e:
            print("Error:", e)
        else:
            print("Operation completed successfully.")
        finally:
            print("Returning to main menu...\n")

if __name__ == "__main__":
    main()
