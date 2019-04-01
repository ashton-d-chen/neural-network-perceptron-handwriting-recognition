from Tkinter import *



def callback(event):
    canvas.create_rectangle(event.x,event.y,event.x+1, event.y+1, outline="black")
    print "clicked at", event.x, event.y

root = Tk()
frame = Frame(root, width=100, height=100)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()
