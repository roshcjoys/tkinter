from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Hello")
window.geometry("150x200")
def message():
    messagebox.showwarning("alert","virus has been detected")
button=Button(text="click",command=message)
button.pack()
window.mainloop()
