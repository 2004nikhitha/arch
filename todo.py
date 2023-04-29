tasks = []


def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully!")


def remove_task():
    task = input("Enter task to remove: ")
    if task in tasks:
        tasks.remove(task)
        print("Task removed successfully!")
    else:
        print("Task not found!")


def display_tasks():
    if len(tasks) == 0:
        print("No tasks found!")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")


while True:
    print("\n1. Add Task")
    print("2. Remove Task")
    print("3. Display Tasks")
    print("4. Quit")

    choice = input("Enter choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        remove_task()
    elif choice == "3":
        display_tasks()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
