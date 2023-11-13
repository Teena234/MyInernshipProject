import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        self.tasks = []
        self.completed_tasks = []

        #Entry Fields
        self.description_label = tk.Label(master, text="Description:", bg="#90EE90")  
        self.description_entry = tk.Entry(master)

        self.due_date_label = tk.Label(master, text="Due Date:", bg="#90EE90")
        self.due_date_entry = tk.Entry(master)

        self.priority_label = tk.Label(master, text="Priority:", bg="#90EE90")
        self.priority_entry = tk.Entry(master)

        # Listbox to display tasks
        self.tasks_listbox = tk.Listbox(master, selectmode=tk.SINGLE, height=10, width=50, bg="#E0FFFF")  # Light Blue
        self.populate_listbox()

        # Buttons
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task, bg="#87CEEB")  # Sky Blue
        self.display_button = tk.Button(master, text="Display Tasks", command=self.display_tasks, bg="#87CEEB")
        self.complete_button = tk.Button(master, text="Complete Task", command=self.complete_task, bg="#FFA07A")  # Light Salmon
        self.update_button = tk.Button(master, text="Update Task", command=self.update_task, bg="#FFA07A")
        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task, bg="#FF6347")  # Tomato

        # Packing elements
        self.description_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.description_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        self.due_date_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.due_date_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        self.priority_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.priority_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        self.tasks_listbox.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W)

        self.add_button.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
        self.display_button.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)
        self.complete_button.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
        self.update_button.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)
        self.remove_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W)

        self.tasks_listbox.bind("<ButtonRelease-1>", self.load_selected_task)

    def populate_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks):
            self.tasks_listbox.insert(tk.END, f"{idx+1}. {task.description}")

    def add_task(self):
        description = self.description_entry.get()
        due_date = self.due_date_entry.get()
        priority = self.priority_entry.get()

        task = Task(description, due_date, priority)
        self.tasks.append(task)

        messagebox.showinfo("Task Added", "Task added successfully!")

        self.clear_entries()
        self.populate_listbox()

    def display_tasks(self):
        task_list = tk.Toplevel(self.master)
        task_list.title("Task List")

        task_list_label = tk.Label(task_list, text="Task List")
        task_list_label.pack()

        for idx, task in enumerate(self.tasks):
            task_label = tk.Label(task_list, text=f"{idx+1}. Description: {task.description}, Due Date: {task.due_date}, Priority: {task.priority}, Completed: {task.completed}")
            task_label.pack()

    def complete_task(self):
        task_idx = self.get_task_index()
        if task_idx is not None:
            task = self.tasks[task_idx]
            task.completed = True
            self.completed_tasks.append(task)
            self.tasks.pop(task_idx)
            messagebox.showinfo("Task Completed", "Task marked as completed!")
            self.populate_listbox()
        self.clear_entries()

    def update_task(self):
        task_idx = self.get_task_index()
        if task_idx is not None:
            task = self.tasks[task_idx]
            description = self.description_entry.get()
            due_date = self.due_date_entry.get()
            priority = self.priority_entry.get()

            if description:
                task.description = description
            if due_date:
                task.due_date = due_date
            if priority:
                task.priority = priority

            messagebox.showinfo("Task Updated", "Task updated successfully!")
            self.populate_listbox()

        self.clear_entries()

    def remove_task(self):
        task_idx = self.get_task_index()
        if task_idx is not None:
            self.tasks.pop(task_idx)
            messagebox.showinfo("Task Removed", "Task removed successfully!")
            self.populate_listbox()

        self.clear_entries()

    def get_task_index(self):
        selected_task = self.tasks_listbox.curselection()
        if selected_task:
            return selected_task[0]
        else:
            messagebox.showerror("No Task Selected", "Please select a task.")
            return None

    def load_selected_task(self, event):
        task_idx = self.get_task_index()
        if task_idx is not None:
            task = self.tasks[task_idx]
            self.description_entry.delete(0, tk.END)
            self.description_entry.insert(tk.END, task.description)
            self.due_date_entry.delete(0, tk.END)
            self.due_date_entry.insert(tk.END, task.due_date)
            self.priority_entry.delete(0, tk.END)
            self.priority_entry.insert(tk.END, task.priority)


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
