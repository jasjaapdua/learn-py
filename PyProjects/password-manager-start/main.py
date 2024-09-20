import tkinter

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.minsize(width=500, height=300)
window.title("My First GUI Program")

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

window.mainloop()