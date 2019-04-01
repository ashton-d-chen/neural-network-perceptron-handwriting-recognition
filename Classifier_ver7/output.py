from Tkinter import *

class theOutput:
  def __init__(self,container,location):
    self.canvas = []
    self.label = []
    self.save = []
    frame = Frame(container, bd=0, relief=RAISED,
                  background ="black")
    
    # Display Input Character
    self.label.append(Label(frame, text = "Input Character", fg = "#3cecff",
                bg = "black", font = ("times",14,"bold")))
    self.label[0].pack(side="top")
    self.canvas.append(Canvas(frame, bg='white', width=130,
                     height=60, background="black"))
    self.canvas[0].pack()
    self.save.append(0)

    # Display Guess Character
    self.label.append(Label(frame, text = "Guess Character", fg = "#3cecff",
                bg = "black", font = ("times",14,"bold")))
    self.label[1].pack(side="top")
    self.canvas.append(Canvas(frame, bg='white', width=130,
                     height=60, background="black"))
    self.canvas[1].pack()
    self.save.append(0)   

    
    frame.pack(expand=1, fill=X, pady=10, padx=5, side=location)
    
  def display(self,sel,item):
    if self.save[sel] != 0:
      self.canvas[sel].delete(self.save[sel]) 
    self.save[sel] = self.canvas[sel].\
                     create_text(65, 30, text=item,
                                 fill="#3cecff",
                                 justify=CENTER,
                                 font=('times', 24, 'bold'))

  
   
if __name__=='__main__':
  root = Tk()
  iOutput=theOutput(root,TOP)
  iOutput.display(0,"cp1")
  iOutput.display(1,"cp2")
