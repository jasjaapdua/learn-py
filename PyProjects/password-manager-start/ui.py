'''
    Specify details for the GUI for the password manager application.
'''

from tkinter import *

window = Tk()
window.title("Password Manager")

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)


window.mainloop()