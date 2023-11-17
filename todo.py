import os

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.filename = "tasks.txt"
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                lines = file.readlines()
                for line in lines:
                    task_info = line.strip().split(",")
                    task_id, title, description, completed = map(str.strip, task_info)
                    task = {"id": int(task_id), "title": title, "description": description, "completed": completed == "True"}
                    self.tasks.append(task)

    def save_tasks(self):
        with open(self.filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task['id']},{task['title']},{task['description']},{task['completed']}\n")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        print("ID  | Title            | Description")
        print("-----------------------------------")
        for task in self.tasks:
            print(f"{task['id']:3} | {task['title'][:15]:15} | {task['description'][:30]}")

    def add_task(self, title, description):
        task_id = len(self.tasks) + 1
        task = {"id": task_id, "title": title, "description": description, "completed": False}
        self.tasks.append(task)
        print(f"Task added: {title}")

    def mark_complete(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                print(f"Task {task_id} marked as complete.")
                return
        print(f"No task found with ID {task_id}.")

    def mark_uncomplete(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = False
                print(f"Task {task_id} marked as uncompleted.")
                return
        print(f"No task found with ID {task_id}.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                print(f"Task {task_id} deleted.")
                return
        print(f"No task found with ID {task_id}.")

    def menu(self):
        while True:
            print("\n===== To-Do List =====")
            print("1. Add Task")
            print("2. List Tasks")
            print("3. Mark Task as Complete")
            print("4. Mark Task as Uncompleted")
            print("5. Delete Task")
            print("6. Save and Exit")

            choice = input("Enter your choice (1-6): ")
            if choice == '1':
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                self.add_task(title, description)
            elif choice == '2':
                self.display_tasks()
            elif choice == '3':
                task_id = int(input("Enter task ID to mark as complete: "))
                self.mark_complete(task_id)
            elif choice == '4':
                task_id = int(input("Enter task ID to mark as uncompleted: "))
                self.mark_uncomplete(task_id)
            elif choice == '5':
                task_id = int(input("Enter task ID to delete: "))
                self.delete_task(task_id)
            elif choice == '6':
                self.save_tasks()
                print("Tasks saved. Exiting.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.menu()
