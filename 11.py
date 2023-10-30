import tkinter as tk

def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Error: Invalid Input")

root = tk.Tk()
root.title("Multiplication Calculator")

entry1 = tk.Entry(root, width=10)
entry1.grid(row=0, column=0)

entry2 = tk.Entry(root, width=10)
entry2.grid(row=0, column=1)

multiply_button = tk.Button(root, text="Multiply", command=multiply)
multiply_button.grid(row=0, column=2)

result_label = tk.Label(root, text="")
result_label.grid(row=1, column=0, columnspan=3)

root.mainloop()
