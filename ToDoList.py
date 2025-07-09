# TO DO LIST
tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added.")

def show_tasks():
    print("\nTo-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

while True:
    print("\n1. Add Task\n2. Show Tasks\n3. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        break
    else:
        print("Invalid choice.")
