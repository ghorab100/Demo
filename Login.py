import tkinter as tk
from tkinter import messagebox

# Dummy credentials for testing
USERNAME = "admin"
PASSWORD = "1234"

def login():
    user = username_entry.get()
    pwd = password_entry.get()
    if user == USERNAME and pwd == PASSWORD:
        messagebox.showinfo("Login", "Login successful!")
    else:
        messagebox.showerror("Login", "Invalid username or password.")

# Create main window
root = tk.Tk()
root.title("Login Page")
root.geometry("300x180")

# Username label and entry
tk.Label(root, text="Username:").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack()

# Password label and entry
tk.Label(root, text="Password:").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Login button
tk.Button(root, text="Login", command=login).pack(pady=15)

# Run the GUI loop
root.mainloop()
