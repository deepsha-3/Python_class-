# this program adding data to the table 
import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
""")

student_data = [

    ("Aashish Mijar", 18),
    ("Kartik Bhusal", 23),
    ("Dipisha Dumre", 12),
    ("Diskshya Subedi", 20)
]
cursor.executemany("""Insert INTO students (name, age) VALUES (?, ?)
""", student_data)
conn.commit()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print("Data in the students table:")
for row in rows:
    print(row)

conn.close()


