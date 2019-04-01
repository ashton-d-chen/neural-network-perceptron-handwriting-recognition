from Tkinter import *


class theTitle:
  def __init__(self,container,location):
    frame = Frame(container, bd=0, relief=FLAT, background ="black")
    frame.pack(expand=1, fill=X, pady=10, padx=5,side=location)
    self.canvas = Canvas(frame, bg='white', width=700,
                     height=50,background="black")
    self.canvas.pack()
    self.sentence = ''
    self.modTitle('Perceptron Handwriting Recognition')
    
    
  def modTitle(self,item):
    if self.sentence != '':
      self.canvas.delete(self.sentence)   
    self.sentence = self.canvas.create_text(330, 25, text=str(item),
                                            fill="#3cecff",
                                            justify=CENTER,
                                            font=('Times', 20, 'bold'))
    

if __name__ == "__main__":
  root = Tk()
  iTitle = theTitle(root)
   
