from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.geometry("650x400")
root.title("Denominator Calculator")
root.configure(bg="#4578bb")

uploaded_image = Image.open("app_image.png")
uplaod = upload.resize((300, 300))
img = ImageTk.PhotoImage(uplaod)

Label = Label(root, image=img = image , bg = "#4578bb")
Label.place (x=180, y=20)

label1 = Label(root, text="wELCOME TO THE APP", bg="#4578bb")
label1.place(relx=0.5, y=340 , anchor = CENTER)

def msg():
    MsgBox  = messsagebox.showinfo ('Denominator Calculator','Do you want to calculate the denominator?')
    if MsgBox == 'ok':
        topwin()


btn1 = Button(root, text="Let's Start", bg="#f0f0f0", fg = "wHITE")
btn.place(x=260, y=360)

def topwin():
    top = Toplevel()
    top.geometry("600 x 450")
    top.configure(bg="#4578bb")
    top.title("Denominator Calculator")


    Label = Label(top, text="Enter total amount", bg="#4578bb") 
    entry = Entry(top)
    lbl = Label(top, text="Enter denominator", bg="#4578bb")
    l1 =label(top, text="Result", bg="#4578bb"  )




    def calculate():                                      