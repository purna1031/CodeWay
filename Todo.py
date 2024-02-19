class ToDoList:
    def __init__(self):
        self.todos = []

    def add_task(self, task):
        self.todos.append(task)
        print(f"Task '{task}' Added.")

    def remove_task(self, task):
        if task in self.todos:
            self.todos.remove(task)
            print(f"Task '{task}' removed.")
        else:
            print(f"Task '{task}' not found in list.")

    def display_tasks(self):
        if self.todos:
            print("To-Do List:")
            for index, task in enumerate(self.todos, start=1):
                print(f"{index}. {task}")
        else:
            print("To-Do List is empty.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nSelect an option:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
