import tkinter as tk
from datetime import date

def calculate_age():
    try:
        d = int(day_entry.get())
        m = int(month_entry.get())
        y = int(year_entry.get())
        dob = date(y, m, d)
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        result_label.config(text=f"Your age is: {age}")
    except Exception:
        result_label.config(text="Invalid input!")

root = tk.Tk()
root.title("Age Calculator")

tk.Label(root, text="Day:").grid(row=0, column=0)
day_entry = tk.Entry(root)
day_entry.grid(row=0, column=1)

tk.Label(root, text="Month:").grid(row=1, column=0)
month_entry = tk.Entry(root)
month_entry.grid(row=1, column=1)

tk.Label(root, text="Year:").grid(row=2, column=0)
year_entry = tk.Entry(root)
year_entry.grid(row=2, column=1)

tk.Button(root, text="Calculate Age", command=calculate_age).grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()