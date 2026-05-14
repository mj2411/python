tasks = []

def show_menu():
    print("\n--- TASK TRACKER ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        print("\nYOUR TASKS:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
        if not tasks:
            print("List is empty.")

    elif choice == '2':
        new_task = input("Enter the task: ")
        tasks.append(new_task)
        print("Task added!")

    elif choice == '3':
        try:
            task_num = int(input("Enter task number to remove: "))
            tasks.pop(task_num - 1)
            print("Task removed.")
        except (ValueError, IndexError):
            print("Invalid number!")

    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")