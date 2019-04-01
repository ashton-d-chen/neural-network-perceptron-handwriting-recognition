
from Tkinter import *



class theList:
    def __init__(self,root):
        global list
        frame = Frame(root, height=20, width=30, bg="black")
        frame.pack()


        list = Listbox(frame, height=10, width=15,bg = "black", fg="green")
        scroll = Scrollbar(frame, command=list.yview)

        list.configure(yscrollcommand=scroll.set)
        list.pack(side=LEFT)
        scroll.pack(side=RIGHT, fill=Y)
        frame.pack(expand=1, fill=X,pady=10,padx=5,sid="top")

    def insertItem(self,message):
        list.insert(END, message)



root = Tk()
root.title('Scrollbar')
l = theList(root)
l.insertItem("hi...")
root.mainloop()
