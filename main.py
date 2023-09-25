from tkinter import *
from random import choice
from tkinter import messagebox

NO_ALPHA = 4
NO_INT = 3
NO_char = 4
back_ground_color = "#3085C3"
FONT = "Cascadia Mono", 15, "normal"
list_cap = [[
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
    [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
    ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
    [
        '!', '@', '#', '$', '%', '^', '&', '*', '_', '+', '-', '|', '?', '~'
    ]]


# PASSWORD GENERATOS
def pass_word():
    entry_password.delete(0, "end")
    alpha = "".join(set([choice(i) for i in list_cap for j in range(3)]))
    entry_password.insert(0, string=alpha)


def add_fun():
    web = entry_web.get()
    email = entry_email.get()
    p = entry_password.get()
    if len(web) <= 0 or len(p) <= 0 or len(email) <= 0:
        if len(web) <= 0:
            m1 = messagebox.showerror(title="Warning", message="Website should not be empty")
        elif len(p) <= 0:
            m1 = messagebox.showerror(title="Warning", message="Password should not be empty")
        elif len(email) <= 0:
            m1 = messagebox.showerror(title="Warning", message="E-mail should not be empty")
    else:
        m = messagebox.askokcancel(title="Entered details", message=f"{web}\n{email}\n{p}")
        if m:
            with open("data.txt", "a") as data:
                data = data.write(f"{web} | {email} | {p}\n")
            entry_web.delete(0, END)
            entry_password.delete(0, END)


# UI SETUP
window = Tk()
window.config(padx=50, pady=50, bg=back_ground_color)
window.title("Set Your password")
canvas = Canvas(height=200, width=189, bg=back_ground_color, highlightthickness=0)
canvas.grid(column=1, row=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=image)

label_web = Label(text="Website:", font=(FONT), highlightthickness=0, bg=back_ground_color)
label_web.grid(column=0, row=1)
entry_web = Entry(width=35, highlightthickness=1, highlightcolor="blue", font=(FONT))
entry_web.grid(column=1, row=1, columnspan=2)

label_email = Label(text="E-Mail:", font=(FONT), bg=back_ground_color, highlightthickness=0)
label_email.grid(column=0, row=2)
entry_email = Entry(width=35, highlightthickness=1, highlightcolor="blue", font=(FONT))
entry_email.insert(0, string="kanukuvinay75@gmail.com")
entry_email.grid(column=1, row=2, columnspan=2, pady=8)

label_password = Label(text="Password:", font=(FONT), bg=back_ground_color, highlightthickness=0)
label_password.grid(column=0, row=3)
entry_password = Entry(width=20, highlightthickness=1, highlightcolor="blue", font=("Cascadia Mono", 16, "normal"))
entry_password.grid(column=1, row=3)

button_genp = Button(text="Generate password", font=("Arial", 14, "normal"), command=pass_word, width=15)
button_genp.grid(column=2, row=3)

button_add = Button(text="Add", width=42, command=add_fun, font=("Cascadia Mono", 13, "normal"))
button_add.grid(column=1, row=5, columnspan=2, pady=5)

window.mainloop()