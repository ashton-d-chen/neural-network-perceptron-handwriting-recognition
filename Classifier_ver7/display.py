from Tkinter import *


class theDisplay:
  def __init__(self,container,name,location):
      
    frame = Frame(container, bd=0, relief=RAISED,  background ="black")
    frame.pack(expand=1, fill=X, pady=10, padx=5, side=location)
    lb2 = Label(frame, text = name, fg = "#3cecff", bg = "black", font = ("times",14,"bold"))
    lb2.pack(side="top")
    self.canvas = Canvas(frame, width=235, height=300,background="black")
    self.canvas.pack()   

if __name__=='__main__':
  root = Tk()
  iDisplay = theDisplay(root)