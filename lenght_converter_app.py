import tkinter as tk

def convert():
    try:
        inches = float(entry.get())
        cm = inches * 2.54
        result.config(text=f"{cm:.2f} cm")
    except:
        result.config(text="Invalid input!")

root = tk.Tk()
root.title("Inches to Centimeters")

tk.Label(root, text="Inches:").pack()
entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="Convert", command=convert).pack()
result = tk.Label(root, text="")
result.pack()

root.mainloop()