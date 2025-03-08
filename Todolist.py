class Task:
    def __init__(self, name, status="Pending"):
        self.name = name
        self.status = status

    def __repr__(self):
        return f"{self.name} - {self.status}"
tasks = []
def add_task(name):
    task = Task(name)
    tasks.append(task)
    print(f"Task '{name}' added successfully.")

def view_tasks():
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks to show.")

def update_task(index, new_name=None, new_status=None):
    try:
        task = tasks[index - 1]
        if new_name:
            task.name = new_name
        if new_status:
            task.status = new_status
        print("Task updated successfully.")
    except IndexError:
        print("Invalid task number.")

def delete_task(index):
    try:
        task = tasks.pop(index - 1)
        print(f"Task '{task.name}' deleted successfully.")
    except IndexError:
        print("Invalid task number.")

def display_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter task name: ")
            add_task(name)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            index = int(input("Enter task number to update: "))
            new_name = input("New task name (leave blank to keep current): ")
            new_status = input("New status (leave blank to keep current): ")
            update_task(index, new_name, new_status)
        elif choice == '4':
            index = int(input("Enter task number to delete: "))
            delete_task(index)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()