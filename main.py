import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
from plyer import notification

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do App")
        self.root.geometry("550x550")

        self.tasks = []

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE ,width=100)
        self.task_listbox.pack(pady=10)

        self.add_task_entry = tk.Entry(root, width=80)
        self.add_task_entry.pack(pady=5)

        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.remove_task_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_task_button.pack(pady=5)

        self.complete_task_button = tk.Button(root, text="Complete Task", command=self.complete_task)
        self.complete_task_button.pack(pady=5)

        self.reminder_button = tk.Button(root, text="Set Reminder", command=self.set_reminder)
        self.reminder_button.pack(pady=5)

    def add_task(self):
        task_text = self.add_task_entry.get().strip()
        if task_text:
            self.tasks.append({"text": task_text, "completed": False, "reminder": None})
            self.update_task_list()
            self.add_task_entry.delete(0, tk.END)

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            del self.tasks[selected_index[0]]
            self.update_task_list()

    def complete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks[selected_index[0]]["completed"] = True
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = " [Done]" if task["completed"] else ""
            self.task_listbox.insert(tk.END, f"{task['text']}{status}")

    def set_reminder(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]
            reminder_time = datetime.now() + timedelta(minutes=1)  # Set a reminder for 1 minute from now

            task["reminder"] = reminder_time
            self.show_notification(f"Reminder: {task['text']}", f"Time to complete your task: {task['text']}")

    def show_notification(self, title, message):
        notification.notify(
            title=title,
            message=message,
            app_name="To-Do App",
            timeout=10
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
