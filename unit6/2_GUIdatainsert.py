import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
from tkinter import messagebox

# Initialize SQLite database and create table if not exists
def init_db():
    with sqlite3.connect("form_data.db") as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                gender TEXT,
                hobbies TEXT,
                country TEXT
            )
        """)

# Save form data to database
def submit_form():
    name_val = name_entry.get().strip()
    gender_val = gender.get()
    country_val = country.get()
    hobbies_val = [hobby for hobby, var in hobby_vars.items() if var.get() == 1]
    hobbies_str = ", ".join(hobbies_val)

    if not name_val:
        messagebox.showerror("Error", "Name is required!")
        return

    try:
        with sqlite3.connect("form_data.db") as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO users (name, gender, hobbies, country) VALUES (?, ?, ?, ?)",
                (name_val, gender_val, hobbies_str, country_val)
            )
        messagebox.showinfo("Success", "Data saved successfully!")
        clear_form()
    except Exception as e:
        messagebox.showerror("Database Error", f"Could not save data:\n{e}")

# Clear all form inputs
def clear_form():
    name_entry.delete(0, tk.END)
    gender.set("Male")
    for var in hobby_vars.values():
        var.set(0)
    country.set("Nepal")

# Show saved records in a nice table with scrollbar
def view_records():
    try:
        with sqlite3.connect("form_data.db") as conn:
            cur = conn.cursor()
            cur.execute("SELECT id, name, gender, hobbies, country FROM users ORDER BY id DESC")
            rows = cur.fetchall()
    except Exception as e:
        messagebox.showerror("Database Error", f"Could not read data:\n{e}")
        return

    if not rows:
        messagebox.showinfo("Records", "No records found.")
        return

    win = tk.Toplevel(root)
    win.title("Saved Records")
    win.geometry("600x300")

    columns = ("ID", "Name", "Gender", "Hobbies", "Country")
    tree = ttk.Treeview(win, columns=columns, show="headings")

    # Define headings
    for col in columns:
        tree.heading(col, text=col)

    # Define column widths and alignment
    tree.column("ID", width=40, anchor=tk.CENTER)
    tree.column("Name", width=150)
    tree.column("Gender", width=80, anchor=tk.CENTER)
    tree.column("Hobbies", width=200)
    tree.column("Country", width=80, anchor=tk.CENTER)

    # Insert rows
    for row in rows:
        tree.insert("", tk.END, values=row)

    # Add vertical scrollbar
    scrollbar = ttk.Scrollbar(win, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tree.pack(expand=True, fill=tk.BOTH)

# --- Tkinter UI setup ---
root = tk.Tk()
root.title("Frame Example")
root.geometry("360x340")

# Name input frame
frame_name = tk.Frame(root, pady=5)
frame_name.pack()
tk.Label(frame_name, text="Name:").pack(side="left")
name_entry = tk.Entry(frame_name)
name_entry.pack(side="left")

# Gender selection frame
frame_gender = tk.Frame(root, pady=5)
frame_gender.pack()
gender = tk.StringVar(value="Male")
for g in ["Male", "Female", "Other"]:
    tk.Radiobutton(frame_gender, text=g, variable=gender, value=g).pack(side="left")

# Hobby selection frame
frame_hobby = tk.Frame(root, pady=5)
frame_hobby.pack()
hobby_vars = {}
for hobby in ["Reading", "Sports", "Music"]:
    var = tk.IntVar()
    hobby_vars[hobby] = var
    tk.Checkbutton(frame_hobby, text=hobby, variable=var).pack(side="left")

# Country selection frame
frame_country = tk.Frame(root, pady=5)
frame_country.pack()
country = tk.StringVar(value="Nepal")
tk.OptionMenu(frame_country, country, "Nepal", "India", "USA", "Japan").pack()

# Buttons frame
frame_buttons = tk.Frame(root, pady=5)
frame_buttons.pack()
tk.Button(frame_buttons, text="Submit", command=submit_form).pack(side="left", padx=5)
tk.Button(frame_buttons, text="View Records", command=view_records).pack(side="left")

# Initialize database
init_db()

root.mainloop()