import datetime
import os
import tkinter as tk
from tkinter import messagebox

task_filename = "tasks.txt"


class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")

        self.tasks = self.load_tasks()

        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)

        self.task_display = tk.Text(self.frame, height=10, width=60)
        self.task_display.grid(row=0, column=0, columnspan=3)

        self.new_task_label = tk.Label(self.frame, text="Enter the task:")
        self.new_task_label.grid(row=1, column=0)

        self.new_task_entry = tk.Entry(self.frame)
        self.new_task_entry.grid(row=1, column=1)

        self.due_date_label = tk.Label(
            self.frame, text="Enter due date (YYYY-MM-DD) [optional]:"
        )
        self.due_date_label.grid(row=2, column=0)

        self.due_date_entry = tk.Entry(self.frame)
        self.due_date_entry.grid(row=2, column=1)

        self.category_label = tk.Label(self.frame, text="Enter task category:")
        self.category_label.grid(row=3, column=0)

        self.category_entry = tk.Entry(self.frame)
        self.category_entry.grid(row=3, column=1)

        self.priority_label = tk.Label(self.frame, text="Enter priority level:")
        self.priority_label.grid(row=4, column=0)

        self.priority_entry = tk.Entry(self.frame)
        self.priority_entry.grid(row=4, column=1)

        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=5, column=0, columnspan=2)

        self.task_index_label = tk.Label(
            self.frame, text="Enter the task number to delete:"
        )
        self.task_index_label.grid(row=6, column=0)

        self.task_index_entry = tk.Entry(self.frame)
        self.task_index_entry.grid(row=6, column=1)

        self.delete_button = tk.Button(
            self.frame, text="Delete Task", command=self.delete_task
        )
        self.delete_button.grid(row=7, column=0, columnspan=2)

        self.save_button = tk.Button(
            self.frame, text="Save and Quit", command=self.save_tasks
        )
        self.save_button.grid(row=8, column=0, columnspan=2)

        self.display_tasks(self.tasks)

    def display_tasks(self, task_list):
        self.task_display.delete(1.0, tk.END)
        if not task_list:
            self.task_display.insert(tk.END, "No tasks to display.")
        else:
            self.task_display.insert(tk.END, "Tasks:\n")
            for idx, task in enumerate(task_list, start=1):
                due_date = task.get("due_date", "Not set")
                category = task.get("category", "Not set")
                priority = task.get("priority", "Not set")
                self.task_display.insert(
                    tk.END,
                    f"{idx}. {task['description']} (Due: {due_date}, Category: {category}, Priority: {priority})\n",
                )

    def add_task(self):
        new_task = self.new_task_entry.get()
        due_date = self.due_date_entry.get()
        category = self.category_entry.get()
        priority = self.priority_entry.get()

        if new_task:
            task = {"description": new_task}

            if due_date:
                try:
                    due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
                    task["due_date"] = due_date
                except ValueError:
                    messagebox.showerror(
                        "Error",
                        "Invalid date format. Please use YYYY-MM-DD format.",
                    )
                    return

            if category:
                task["category"] = category

            if priority:
                try:
                    priority = int(priority)
                    task["priority"] = priority
                except ValueError:
                    messagebox.showerror(
                        "Error", "Priority level must be an integer."
                    )
                    return

            self.tasks.append(task)
            self.display_tasks(self.tasks)
            self.new_task_entry.delete(0, tk.END)
            self.due_date_entry.delete(0, tk.END)
            self.category_entry.delete(0, tk.END)
            self.priority_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            task_index = int(self.task_index_entry.get())
            if 1 <= task_index <= len(self.tasks):
                removed_task = self.tasks.pop(task_index - 1)
                self.display_tasks(self.tasks)
                self.task_index_entry.delete(0, tk.END)
                messagebox.showinfo(
                    "Success",
                    f"Task '{removed_task['description']}' deleted successfully.",
                )
            else:
                messagebox.showerror("Error", "Invalid task index.")
        except ValueError:
            messagebox.showerror("Error", "Invalid task index.")

    def save_tasks(self):
        self.save_tasks_to_file(self.tasks, task_filename)
        messagebox.showinfo("Success", "Tasks saved. Exiting.")
        self.root.quit()

    def load_tasks(self):
        return self.load_tasks_from_file(task_filename)

    def save_tasks_to_file(self, task_list, filename):
        with open(filename, "w") as file:
            for task in task_list:
                description = task["description"]
                due_date = task.get("due_date", "Not set")
                category = task.get("category", "Not set")
                priority = task.get("priority", "Not set")
                file.write(
                    f"{description},{due_date},{category},{priority}\n"
                )

    def load_tasks_from_file(self, filename):
        task_list = []
        if os.path.exists(filename):
            with open(filename, "r") as file:
                for line in file.readlines():
                    description, due_date, category, priority = line.strip().split(",")
                    task = {"description": description}
                    if due_date != "Not set":
                        task["due_date"] = datetime.datetime.strptime(
                            due_date, "%Y-%m-%d"
                        ).date()
                    if category != "Not set":
                        task["category"] = category
                    if priority != "Not set":
                        task["priority"] = int(priority)
                    task_list.append(task)
        return task_list


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
