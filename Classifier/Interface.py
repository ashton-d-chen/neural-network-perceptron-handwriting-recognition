'''
File: Interface.py
Author: Jann-Chyi Chen
Version: 1.0
Date: 2008-03-19
Description: Interface creates a GUI which contains a control
  panel and a display for computation result. 
  
'''

from Tkinter import * # for creating graphic user interface
import perceptron     # perceptron
import samples        # load or create datum object
import sys
import util           # implements a counter for storing weight information
import time          
import tkFont         # font style 
import temp           # a file which save a set of global temporary
                      # variables or objects
import control        # control panel of the GUI
import convert        # crop, filter, and transforms input image to a datum object    


'''
A class of an object which can be created under a container, such as a frame.
It displays the label a user has entered and guessed label picked up by the
perceptron classifier.
'''
class theOutput:
  def __init__(self,container,location):
    self.canvas = []
    self.label = []
    self.save = []
    frame = Frame(container, bd=0, relief=RAISED,
                  background ="black")
    
    # Display Input Character
    self.label.append(Label(frame, text = "\n\n\nInput\nCharacter", fg = "#3cecff",
                bg = "black", font = ("times",14,"bold")))
    self.label[0].pack(side="top")
    self.canvas.append(Canvas(frame, bg='white', width=50,
                     height=60, background="black"))
    self.canvas[0].pack()
    self.save.append(0)

    # Display Guess Character
    self.label.append(Label(frame, text = " \n\nGuess\nCharacter", fg = "#3cecff",
                bg = "black", font = ("times",14,"bold")))
    self.label[1].pack(side="top")
    self.canvas.append(Canvas(frame, bg='white', width=50,
                     height=60, background="black"))
    self.canvas[1].pack()
    self.save.append(0)   

    frame.pack(expand=1, fill=X, pady=10, padx=5, side=location)

  # a function for changing displayed text   
  def display(self,sel,item):
    if self.save[sel] != 0:
      self.canvas[sel].delete(self.save[sel]) 
    self.save[sel] = self.canvas[sel].\
                     create_text(30, 30, text=item,
                                 fill="#3cecff",
                                 justify=CENTER,
                                 font=('times', 24, 'bold'))

  

'''
A class of object which display program execution history and status
'''
class theLog:
  def __init__(self,root,location):
    frame = Frame(root, height=15, width=60, bg="black")
    lb2 = Label(frame, text = "System Status",
                fg = "#3cecff", bg = "black", font = ("times",14,"bold"))
    lb2.pack(side="top")
    self.l = Listbox(frame, height=15, width=60,bg = "black",
                     fg="green", font=('times', 12))
    scroll = Scrollbar(frame, command=self.l.yview)
    self.l.configure(yscrollcommand=scroll.set)
    self.l.pack(side=LEFT)
    scroll.pack(side=LEFT, fill=Y)
    frame.pack(expand=1, fill=X, pady=10, padx=5, side=location)

  # a function which allows program to display message for user
  def insertItem(self,message):
    self.l.insert(END, message)
    self.l.see(END)



'''
A class of objects which displays datum object created by user and current
weights of the class of each label
'''
class theDisplay:
  def __init__(self,container,name,location,width):
      
    frame = Frame(container, bd=0, relief=RAISED,  background ="black")
    frame.pack(expand=1, fill=X, pady=10, padx=5, side=location)
    self.label = Label(frame, text = name, fg = "#3cecff",
                       bg = "black", font = ("times",14,"bold"))
    self.label.pack(side="top")
    self.canvas = Canvas(frame, width=width, height=300,background="black")
    self.canvas.pack()


    
'''
Display the tile in GUI
'''
class theTitle:
  def __init__(self,container,location):
    frame = Frame(container, bd=0, relief=FLAT, background ="black")
    frame.pack(expand=1, fill=X, pady=10, padx=5,side=location)
    self.canvas = Canvas(frame, bg='white', width=700,
                     height=50,background="black")
    self.canvas.pack()
    self.sentence = ''
    self.modTitle('Perceptron Classifier')
    
  '''
  function that will modify displayed text in title
  '''
  def modTitle(self,item):
    if self.sentence != '':
      self.canvas.delete(self.sentence)   
    self.sentence = self.canvas.create_text(330, 25, text=str(item),
                                            fill="#3cecff",
                                            justify=CENTER,
                                            font=('Times', 20, 'bold'))



'''
An interface that demonstrates the use of perceptron AI technique
'''
class interface:
  def __init__(self, master):    
    frame = Frame(master, width=700, height=600, bd=1, background ="black")
    frame.pack()



    
    iFrame = Frame(frame, width=700, height=600, bd=1, background ="black")
    iFrame.pack(side=TOP)
    # Control panel
    temp.iControl = control.theControl(iFrame,LEFT)

    # System Output Frame
    temp.iOutput = theOutput(iFrame,LEFT)
    
    # User Input Image
    temp.usrInput = theDisplay(iFrame,"User Input Image",LEFT,235)
    
    # Add a log list
    temp.LOG_LIST = theLog(iFrame,RIGHT)
        
    # Create a new frame
    iFrame = Frame(frame, width=700, height=600, bd=1, background ="black")
    iFrame.pack(side=BOTTOM)

    # Input weight
    temp.inputWeight = theDisplay(iFrame,"",LEFT,470)
      
    # Current Weight
    temp.currentWeight = theDisplay(iFrame,"",LEFT,470)
    
    # Select classifier
    temp.iClassifier = perceptron.PerceptronClassifier()
   


        
        
    
root = Tk()
root.option_add('*font', ('verdana', 10, 'bold'))
interface = interface(root)
root.title('Perceptron Classifier')
root.mainloop()
