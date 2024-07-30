def add_task(tasks):
    task = input("Enter a task:")
    tasks.append(task)
    print("Task added!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks):
            print(f"{index + 1}.{task}")

def delete_task(tasks):
    try:
        index = int(input("Enter the task number to delete:"))-1
        if 0<= index < len(tasks):
            deleted_task = pop(index)
            print(f"Task'{deleted_task}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.Please enter a number.")

def main():
    tasks = []
    while True:
        print("\nTo-Do List")
        print("1. Add task")
        print("2. View task")
        print("3. Delete task")
        print("4. Quit")
        choice = input("Enter your choice:")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()