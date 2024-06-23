tasks = []

def add_task(task):
    """Add a task to the to-do list."""
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_tasks():
    """View all tasks in the to-do list."""
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def complete_task(task_index):
    """Mark a task as complete and remove it from the to-do list."""
    if 1 <= task_index <= len(tasks):
        completed_task = tasks.pop(task_index - 1)
        print(f"Task '{completed_task}' marked as complete.")
    else:
        print("Invalid task index.")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            view_tasks()
            task_index = int(input("Enter the task number to mark as complete: "))
            complete_task(task_index)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()