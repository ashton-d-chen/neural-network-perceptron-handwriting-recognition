from Tkinter import *
import perceptron
import samples
import sys
import util
import time
import tkFont
import setting
import temp
import control
import log
import convert
import title
import display
import output
          
class interface:
  def __init__(self, master):
    global c1, c2, c3, c4, c5, c6, c7, iClassifier
    global TRAIN_NUM, POS_WEIGHT, NEG_WEIGHT, Tkinter
    
    frame = Frame(master, width=700, height=600, bd=1, background ="black")
    frame.pack()

    # Add a title
    temp.iTitle = title.theTitle(frame,TOP)




    iFrame = Frame(frame, width=700, height=600, bd=1, background ="black")
    iFrame.pack(side=TOP)

    # Add a log list
    temp.LOG_LIST = log.theLog(iFrame,LEFT)
    
    # User Input Image
    temp.usrInput = display.theDisplay(iFrame,"User Input Image",LEFT,235)
    
    # Input and weight Overlap
    temp.inputWeight = display.theDisplay(iFrame,"Weight of ",LEFT,470)
    



    iFrame = Frame(frame, width=700, height=600, bd=1, background ="black")
    iFrame.pack(side=TOP)
    
    # Control panel
    temp.iControl = control.theControl(iFrame,LEFT)

    
    # System Output Frame
    temp.iOutput = output.theOutput(iFrame,LEFT)

    # Current Weight
    temp.currentWeight = display.theDisplay(iFrame,"Weight of ",LEFT,470)


    
    # Select classifier
    temp.iClassifier = perceptron.PerceptronClassifier()
   


        
        
    
root = Tk()
root.option_add('*font', ('verdana', 10, 'bold'))
interface = interface(root)
root.title('Tkinter Widgets')

root.mainloop()
