# To-Do List CLI App — CodSoft Project by Ashutosh

tasks = []

def show_menu():
    print("\n=== TO-DO MENU ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

def add_task():
    task = input("Task description: ")
    tasks.append({"task": task, "done": False})
    print("Task added.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    print("\nYour tasks:")
    for i, t in enumerate(tasks, start=1):
        status = "Done" if t["done"] else "Pending"
        print(f"{i}. {t['task']} [{status}]")

def mark_done():
    view_tasks()
    try:
        idx = int(input("Enter task number to mark as done: ")) - 1
        tasks[idx]["done"] = True
        print("Task updated.")
    except:
        print("Invalid input.")

def delete_task():
    view_tasks()
    try:
        idx = int(input("Enter task number to delete: ")) - 1
        removed = tasks.pop(idx)
        print(f"Deleted: {removed['task']}")
    except:
        print("Invalid input.")

# Main loop
while True:
    show_menu()
    option = input("Select an option (1-5): ")

    if option == '1':
        add_task()
    elif option == '2':
        view_tasks()
    elif option == '3':
        mark_done()
    elif option == '4':
        delete_task()
    elif option == '5':
        print("Exiting. See you next session.")
        break
    else:
        print("Invalid option. Try again.")