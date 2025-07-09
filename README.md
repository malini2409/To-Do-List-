
---

## 📁 3. To-Do List (CLI) — `README.md`

```markdown
# 📋 To-Do List App (Command Line)

A basic command-line task manager that allows users to add and view tasks.

---

## ✨ Features
- Add tasks dynamically
- View all tasks
- Simple and menu-driven

---

## ✅ Prerequisites
- Python 3.x

---

## ▶️ How to Run
1. Save the file as `todo_list.py`
2. Execute using:
```bash
python todo_list.py

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
