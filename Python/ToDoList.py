def display_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
    else:
        print("Your tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def todo_list():
    tasks = []
    while True:
        print("\nOptions: \n1. Add task\n2. Remove task\n3. View tasks\n4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter a new task: ")
            tasks.append(task)
            print(f"'{task}' has been added.")
        elif choice == '2':
            display_tasks(tasks)
            task_no = int(input("Enter the task number to remove: ")) - 1
            if 0 <= task_no < len(tasks):
                removed_task = tasks.pop(task_no)
                print(f"'{removed_task}' has been removed.")
            else:
                print("Invalid task number.")
        elif choice == '3':
            display_tasks(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

todo_list()