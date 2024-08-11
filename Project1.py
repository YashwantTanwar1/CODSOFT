import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)
        messagebox.showwarning("Todo App", "task added.")
    else:
        messagebox.showwarning("Todo App", "Please enter a task.")

def delete_task():
    try:
        index = task_list.curselection()[0]
        task_list.delete(index)
        messagebox.showwarning("Todo App", "Task Deleted.")
    except IndexError:
        messagebox.showwarning("Todo App", "No task selected.")

def complete_task():
    try:
        index = task_list.curselection()[0]
        task = task_list.get(index)
        task_list.delete(index)
        task_list.insert(tk.END, f"✅ {task}")
    except IndexError:
        messagebox.showwarning("Todo App", "No task selected.")

root = tk.Tk()
root.title("Todo App")
root.geometry("300x500")  
root.resizable(False, False)
root.config(bg="skyblue")

entry = tk.Entry(root)
entry.place(x=50, y=20, width=200, height=50)
entry.config(bg="lightblue")  

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.place(x=100, y=80, width=100, height=30)

task_list = tk.Listbox(root)
task_list.place(x=50, y=120, width=200, height=300)
task_list.config(bg="lightblue") 

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.place(x=100, y=430, width=100, height=30)
delete_button.config(bg="red")

complete_button = tk.Button(root, text="Complete Task", command=complete_task)
complete_button.place(x=100, y=470, width=100, height=30)

root.mainloop()
