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

    # Add setting option
  #  temp.iSetting = setting.theSetting(frame,BOTTOM)




    iFrame = Frame(frame, width=700, height=600, bd=1, background ="black")
    iFrame.pack(side=TOP)

    # User Input Image
    temp.usrInput = display.theDisplay(iFrame,"User Input Image",LEFT)
    
    # Input and weight Overlap
    temp.inputWeight = display.theDisplay(iFrame,"Input and Weight Overlap",LEFT)
    
    # Current Weight
    temp.currentWeight = display.theDisplay(iFrame,"Current weight",LEFT)


    iFrame = Frame(frame, width=700, height=600, bd=1, background ="black")
    iFrame.pack(side=TOP)
    
    # Control panel
    temp.iControl = control.theControl(iFrame,LEFT)

    # Current Weight
    temp.weightChange = display.theDisplay(iFrame,"Weight Change",LEFT)

    # System Output Frame
    temp.iOutput = output.theOutput(iFrame,LEFT)

    # Add a log list
    temp.LOG_LIST = log.theLog(iFrame,BOTTOM)
    
    # Select classifier
    temp.iClassifier = perceptron.PerceptronClassifier()
   


        
        
    
root = Tk()
root.option_add('*font', ('verdana', 10, 'bold'))
interface = interface(root)
root.title('Tkinter Widgets')

root.mainloop()
