import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "tasks.json"

# Load tasks
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks
def save_tasks():
    tasks = task_list.get(0, tk.END)
    with open(FILE_NAME, "w") as file:
        json.dump(list(tasks), file)

# Add task
def add_task():
    task = task_entry.get().strip()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Delete task
def delete_task():
    try:
        selected = task_list.curselection()[0]
        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this task?"
        )
        if confirm:
            task_list.delete(selected)
            save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task first.")

# Mark task as completed
def complete_task():
    try:
        selected = task_list.curselection()[0]
        task = task_list.get(selected)

        if not task.startswith("✓ "):
            task_list.delete(selected)
            task_list.insert(selected, "✓ " + task)

        save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task first.")

# Clear all tasks
def clear_tasks():
    confirm = messagebox.askyesno(
        "Clear All",
        "Delete all tasks?"
    )
    if confirm:
        task_list.delete(0, tk.END)
        save_tasks()

# GUI Window
root = tk.Tk()
root.title("To-Do List Manager")
root.geometry("500x550")
root.resizable(False, False)

# Heading
title = tk.Label(
    root,
    text="To-Do List Manager",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)

# Entry box
task_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=30
)
task_entry.pack(pady=10)

# Add button
add_btn = tk.Button(
    root,
    text="Add Task",
    font=("Arial", 12),
    command=add_task
)
add_btn.pack(pady=5)

# Listbox Frame
frame = tk.Frame(root)
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)

task_list = tk.Listbox(
    frame,
    width=45,
    height=15,
    font=("Arial", 12),
    yscrollcommand=scrollbar.set
)

scrollbar.config(command=task_list.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_list.pack()

# Buttons Frame
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

complete_btn = tk.Button(
    btn_frame,
    text="Complete",
    width=12,
    command=complete_task
)
complete_btn.grid(row=0, column=0, padx=5)

delete_btn = tk.Button(
    btn_frame,
    text="Delete",
    width=12,
    command=delete_task
)
delete_btn.grid(row=0, column=1, padx=5)

clear_btn = tk.Button(
    btn_frame,
    text="Clear All",
    width=12,
    command=clear_tasks
)
clear_btn.grid(row=0, column=2, padx=5)

# Load saved tasks
for task in load_tasks():
    task_list.insert(tk.END, task)

root.mainloop()