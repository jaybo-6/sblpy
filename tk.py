import tkinter as tk

def start_button_clicked():
    login = login_entry.get()
    password = password_entry.get()
    # You can perform actions with login and password here
    print("Login:", login)
    print("Password:", password)

# Create the main window
root = tk.Tk()
root.title("Login Form")

# Create a label for Login field
login_label = tk.Label(root, text="Login:")
login_label.pack()

# Create an Entry field for Login
login_entry = tk.Entry(root)
login_entry.pack()

# Create a label for the Password field
password_label = tk.Label(root, text="Password:")
password_label.pack()

# Create an Entry field for Password
password_entry = tk.Entry(root, show="*")  # Use 'show' option to hide the password
password_entry.pack()

# Create a Start button
start_button = tk.Button(root, text="Start", command=start_button_clicked)
start_button.pack()

# Run the GUI application
root.mainloop()
