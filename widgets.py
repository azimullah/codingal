import tkinter as tk

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_label.config(text=f"Product: {product}")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

root = tk.Tk()
root.title("Product Calculator")

tk.Label(root, text="Enter first number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Button(root, text="Calculate Product", command=calculate_product).pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()