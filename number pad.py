from tkinter import *
window=Tk()
window.title("number pad")
window.geometry("320x400")
list1=[[9,8,7],[6,5,4],[3,2,1],["#",0,"*"]]
for i in range(4):
    window.columnconfigure(1,weight=1,minsize=80)
    window.rowconfigure(i,weight=1,minsize=60)
    for j in range(3):
        frame=Frame(master=window,relief=RAISED,borderwidth=2)
        frame.grid(row=i,column=j)
        label=Label(master=frame,text=list1[i][j])
        label.pack(padx=5,pady=5)
window.mainloop()



