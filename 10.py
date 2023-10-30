import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('mydb.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a 'students' table in the database
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
)
''')

# Insert data into the 'students' table
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ('jay', 21))
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ('z', 21))

# Commit the changes to the database
conn.commit()

# Select data from the 'students' table and print the results
cursor.execute("SELECT * FROM students")
results = cursor.fetchall()
for row in results:
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")

# Update the age of the student named 'z' to 32
cursor.execute("UPDATE students SET age = 32 WHERE name = 'z'")
conn.commit()

# Close the database connection
conn.close()
