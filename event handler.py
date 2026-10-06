from tkinter import *
window=Tk()
window.title("Hello")
window.geometry("150x200")
def keypress(event):
    print(event.char)
window.bind("<Key>",keypress)
def click(event):
    print("the button was clicked")
button=Button(text="click")
button.pack()
button.bind("<Button-1>",click)
window.mainloop()

