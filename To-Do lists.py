import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        tasks_list.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = tasks_list.curselection()
    if selected_task_index:
        tasks_list.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def mark_completed():
    selected_task_index = tasks_list.curselection()
    if selected_task_index:
        task_text = tasks_list.get(selected_task_index)
        task_text = f"[Completed] {task_text}"
        tasks_list.delete(selected_task_index)
        tasks_list.insert(tk.END, task_text)
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

root = tk.Tk()
root.title("To-Do List Application")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

mark_completed_button = tk.Button(root, text="Mark Completed", command=mark_completed)
mark_completed_button.pack()

tasks_list = tk.Listbox(root, width=40, height=10)
tasks_list.pack(pady=10)

root.mainloop()
