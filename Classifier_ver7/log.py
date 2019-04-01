from Tkinter import *

class theLog:
  def __init__(self,root,location):
    frame = Frame(root, height=15, width=18, bg="black")
    lb2 = Label(frame, text = "System Status", fg = "#3cecff", bg = "black", font = ("times",14,"bold"))
    lb2.pack(side="top")
    self.l = Listbox(frame, height=15, width=18,bg = "black",
                     fg="green", font=('times', 12))
    scroll = Scrollbar(frame, command=self.l.yview)
    self.l.configure(yscrollcommand=scroll.set)
    self.l.pack(side=LEFT)
    scroll.pack(side=LEFT, fill=Y)
    frame.pack(expand=1, fill=X, pady=10, padx=5, side=location)

  def insertItem(self,message):
    self.l.insert(END, message)
    self.l.see(END)

if __name__ == "__main__":
  root = Tk()
  iLog = theLog(root,TOP)
  for i in range(40):
    iLog.insertItem(str(i))
