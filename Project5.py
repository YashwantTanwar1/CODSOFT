import tkinter as tk
from tkinter import messagebox

# Contact Book Application with Tkinter

contacts = {}

def add_contact():
    name = name_var.get()
    number = number_var.get()
    email = email_var.get()
    address = address_var.get()
    if name and number and email and address:
        contacts[name] = {'number': number, 'email': email, 'address': address}
        messagebox.showinfo("Success", f"Contact {name} added successfully.")
        clear_fields()
    else:
        messagebox.showwarning("Input Error", "All fields are required.")

def view_contact():
    name = name_var.get()
    if name in contacts:
        contact = contacts[name]
        messagebox.showinfo("Contact Info", f"Name: {name}\nPhone Number: {contact['number']}\nEmail: {contact['email']}\nAddress: {contact['address']}")
    else:
        messagebox.showwarning("Not Found", f"Contact {name} not found.")

def search_contact():
    name = name_var.get()
    if name in contacts:
        contact = contacts[name]
        name_var.set(name)
        number_var.set(contact['number'])
        email_var.set(contact['email'])
        address_var.set(contact['address'])
    else:
        messagebox.showwarning("Not Found", f"Contact {name} not found.")

def update_contact():
    name = name_var.get()
    if name in contacts:
        contacts[name] = {'number': number_var.get(), 'email': email_var.get(), 'address': address_var.get()}
        messagebox.showinfo("Success", f"Contact {name} updated successfully.")
        clear_fields()
    else:
        messagebox.showwarning("Not Found", f"Contact {name} not found.")

def delete_contact():
    name = name_var.get()
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Success", f"Contact {name} deleted successfully.")
        clear_fields()
    else:
        messagebox.showwarning("Not Found", f"Contact {name} not found.")

def clear_fields():
    name_var.set("")
    number_var.set("")
    email_var.set("")
    address_var.set("")

# Setting up the main window
root = tk.Tk()
root.title("Contact Book CODSOFT")

# Variables
name_var = tk.StringVar()
number_var = tk.StringVar()
email_var = tk.StringVar()
address_var = tk.StringVar()

tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=name_var).grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Phone Number").grid(row=1, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=number_var).grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email").grid(row=2, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=email_var).grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Address").grid(row=3, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=address_var).grid(row=3, column=1, padx=10, pady=5)

tk.Button(root, text="Add Contact", command=add_contact).grid(row=4, column=0, padx=10, pady=5)
tk.Button(root, text="View Contact", command=view_contact).grid(row=4, column=1, padx=10, pady=5)
tk.Button(root, text="Search Contact", command=search_contact).grid(row=5, column=0, padx=10, pady=5)
tk.Button(root, text="Update Contact", command=update_contact).grid(row=5, column=1, padx=10, pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).grid(row=6, column=0, padx=10, pady=5)
tk.Button(root, text="Clear Fields", command=clear_fields).grid(row=6, column=1, padx=10, pady=5)

root.mainloop()
