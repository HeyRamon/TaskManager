import tkinter as tk
from tkinter import simpledialog, messagebox
import heapq

class TaskManager:
    def __init__(self):
        self.tasks = []  # min-heap
        self.counter = 0  # to maintain insertion order for same priority

    def add_task(self, description, priority):
        heapq.heappush(self.tasks, (-priority, self.counter, description))
        self.counter += 1

    def pop_task(self):
        if not self.tasks:
            return "No tasks!"
        return heapq.heappop(self.tasks)[2]

    def get_tasks(self):
        # return tasks in order without removing them
        return [desc for _, _, desc in sorted(self.tasks, reverse=True)]

class TaskGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Task Manager")
        self.manager = TaskManager()

        self.task_list = tk.Listbox(root, width=50)
        self.task_list.pack(pady=10)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Add Task", command=self.add_task).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Pop Task", command=self.pop_task).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Refresh", command=self.refresh_tasks).grid(row=0, column=2, padx=5)

    def add_task(self):
        desc = simpledialog.askstring("Task", "Task Description:")
        if not desc:
            return
        prio = simpledialog.askinteger("Priority", "Task Priority (1-5):", minvalue=1, maxvalue=5)
        if prio is None:
            return
        self.manager.add_task(desc, prio)
        self.refresh_tasks()

    def pop_task(self):
        result = self.manager.pop_task()
        messagebox.showinfo("Popped Task", result)
        self.refresh_tasks()

    def refresh_tasks(self):
        self.task_list.delete(0, tk.END)
        for i, task in enumerate(self.manager.get_tasks(), start=1):
            self.task_list.insert(tk.END, f"{i}. {task}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskGUI(root)
    root.mainloop()