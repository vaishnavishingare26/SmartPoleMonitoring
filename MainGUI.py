from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import Monitoring_Engine
from tkinter import messagebox


# ---------- WINDOW CENTER FUNCTION ----------

def center_window(w, h):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = int((ws / 2) - (w / 2))
    y = int((hs / 2) - (h / 2))
    root.geometry(f"{w}x{h}+{x}+{y}")


# ---------- BUTTON FUNCTION ----------

def read_input():

    admin_name = textBox1.get()
    admin_password = textBox2.get()
    mob = textBox3.get()

    if admin_name == "" or admin_password == "" or mob == "":
        messagebox.showerror("Error", "Please fill all fields")
        return

    if len(mob) != 10:
        messagebox.showerror("Error", "Enter valid mobile number")
        return

    messagebox.showinfo("System", "Monitoring Started")

    Monitoring_Engine.read_thingspeak_data(admin_name, admin_password, mob)


# ---------- MAIN WINDOW ----------

root = Tk()
root.configure(background='#6495ED')
root.title("SMART ELECTRICAL POLE MONITORING SYSTEM")
center_window(800, 600)


# ---------- BACKGROUND IMAGE ----------

image = Image.open("logo.png")
resize_image = image.resize((800, 600))
img = ImageTk.PhotoImage(resize_image)

label_bg = Label(root, image=img)
label_bg.place(x=0, y=0)


# ---------- TITLE ----------

title = Label(
    root,
    text="SMART ELECTRICAL POLE MONITORING SYSTEM",
    font=("Courier", 20, 'bold'),
    fg='#FF0000',
    bg='#6495ED'
)

title.place(x=80, y=40)


# ---------- LABELS ----------

label1 = Label(root, text="ADMIN Name:", bg='#6495ED', font=("Arial", 12))
label1.place(x=140, y=180)

label2 = Label(root, text="ADMIN Password:", bg='#6495ED', font=("Arial", 12))
label2.place(x=140, y=240)

label3 = Label(root, text="Mobile No:", bg='#6495ED', font=("Arial", 12))
label3.place(x=140, y=300)


# ---------- TEXTBOX ----------

textBox1 = Entry(root, width=30)
textBox1.place(x=350, y=180, height=30)

textBox2 = Entry(root, width=30, show="*")
textBox2.place(x=350, y=240, height=30)

textBox3 = Entry(root, width=30)
textBox3.place(x=350, y=300, height=30)


# ---------- BUTTONS ----------

start_button = Button(
    root,
    height=1,
    width=20,
    font=("Arial", 11, 'bold'),
    text="START MONITORING",
    command=read_input
)

start_button.place(x=180, y=380)


exit_button = Button(
    root,
    height=1,
    width=15,
    font=("Arial", 11, 'bold'),
    text="Exit",
    command=root.destroy
)

exit_button.place(x=420, y=380)


# ---------- MAIN LOOP ----------

root.mainloop()