#This is To-Do list Application created by Rohan Tripathi
import tkinter as tk
from tkinter import messagebox
import json

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []
        self.file_name = "tasks.json"
        self.load_tasks()

        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack(pady=10)

        self.add_entry = tk.Entry(root, width=40)
        self.add_entry.pack(pady=5)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Mark as Complete", command=self.mark_complete)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.refresh_task_list()

    def add_task(self):
        task = self.add_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.add_entry.delete(0, tk.END)
            self.save_tasks()
            self.refresh_task_list()

    def mark_complete(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["completed"] = True
            self.save_tasks()
            self.refresh_task_list()

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks.pop(index)
            self.save_tasks()
            self.refresh_task_list()

    def refresh_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task["completed"] else "✗"
            self.task_listbox.insert(tk.END, f"{task['task']} [{status}]")

    def save_tasks(self):
        with open(self.file_name, "w") as f:
            json.dump(self.tasks, f)

    def load_tasks(self):
        try:
            with open(self.file_name, "r") as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            self.tasks = []

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

#Done by Rohan


    
