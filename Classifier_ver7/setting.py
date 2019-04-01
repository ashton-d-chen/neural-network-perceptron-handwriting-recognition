from Tkinter import *
import util
import temp
import os
#from Interface import TRAIN_NUM
TEMP = 0


class theDialog:
  def __init__(self, container):

    self.top = Toplevel(container,bg="black")
    Label(self.top, text="Please enter new a value", bg="black", fg="#3cecff").pack()

    self.iEntry = Entry(self.top, bg="#035e89", fg="#3cecff")
    self.iEntry.pack(padx=5)

    b = Button(self.top, text="Enter", bg="black", fg="green", command=self.callUpdate)
    b.pack(pady=5)

  def callUpdate(self):
    global TEMP 
    TEMP = self.iEntry.get()
    self.top.destroy()
    

class theSetting:
  def __init__(self, container,location):
    # Auto Training Settings
    self.container = container
    frame = Toplevel(container, bd=2, relief=FLAT, background ="black",
                  highlightcolor="red")
    self.frame = frame

    '''
    subFrame = Frame(frame, bd=2, relief=FLAT, background ="black",
                  highlightcolor="red")
    subFrame.pack(side=LEFT)
    
    lbl = Label(subFrame, text = "Auto Training Settings ", fg="#3cecff",
                bg="black",font=("times",14,"underline"))
    lbl.pack()
       
    self.b0 = Button(subFrame, text="Data Amount: " + str(temp.TRAIN_NUM),
                     fg="#3cecff", command=self.autoDataAmount, bg ="black",
                     relief=SOLID, font=(12))
    self.b0.pack(side=TOP)
    self.b1 = Button(subFrame, text="Iteration: " + str(temp.AUTO_ITERATIONS),
                     fg="#3cecff",command=self.autoDataIter, bg ="black", relief=SOLID,
                     font=("times",12))
    self.b1.pack(side=TOP)
    '''


    subFrame = Frame(frame, bd=2, relief=FLAT, background ="black",
                  highlightcolor="red")
    subFrame.pack(side=RIGHT)
    
    # User Training Settings
    lbl = Label(subFrame, text = "User Training Settings ", fg="#3cecff",
                bg="black",font=("times",14, "underline"))
    lbl.pack()
    
    self.b2 = Button(subFrame, text="Inputed Label: " + str(temp.USER_LABEL), fg="#3cecff",
                        command=self.usrDataLabel, bg ="black", relief=SOLID, font=("times",12))
    self.b2.pack(side=TOP)
    self.b3 = Button(subFrame, text="Iteration: " + str(temp.USER_ITERATIONS), fg="#3cecff",
                        command=self.usrDataIter, bg ="black", relief=SOLID, font=("times",12))
    self.b3.pack(side=TOP)


    self.b6 = Button(subFrame, text="OK", fg="#3cecff",
                        command=self.close, bg ="black", relief=SOLID, font=("times",12))
    self.b6.pack(side=RIGHT)
    '''
    # Perceptron Settings
    subFrame = Frame(frame, bd=2, relief=FLAT, background ="black",
                  highlightcolor="red")
    subFrame.pack(side=LEFT)
    
    lbl = Label(subFrame, text = "Perceptron Settings ", fg="#3cecff", bg="black",
                font=("times",14,"underline"))
    lbl.pack()
    self.b4 = Button(subFrame, text="Positive Weight: " + str(temp.POS_WEIGHT),
                     fg="#3cecff", command=self.percepPos, bg ="black", relief=SOLID, font=("times",12))
    self.b4.pack(side=TOP)
    
    self.b5 = Button(subFrame, text="Negative Weight: " + str(temp.NEG_WEIGHT), fg="#3cecff",
                        command=self.percepNeg, bg ="black", relief=SOLID, font=("times",12))
    self.b5.pack(side=TOP)
    '''
 #   frame.pack(expand=1, fill=X, pady=10, padx=5,side=location)

  def autoDataAmount(self):
    global TEMP
    self.iDialog = theDialog(self.container)
    self.container.wait_window(self.iDialog.top)
    temp.TRAIN_NUM = int(TEMP)
    self.b0['text']="Data Amount: " + str(TEMP)
  def autoDataIter(self):
    global TEMP
    self.iDialog = theDialog(self.container)
    self.container.wait_window(self.iDialog.top)
    temp.AUTO_ITERATIONS = int(TEMP)
    self.b1['text']="Iteration: " + str(TEMP)
  def usrDataLabel(self):
    global TEMP
    self.iDialog = theDialog(self.container)
    self.container.wait_window(self.iDialog.top)
    temp.USER_LABEL = str(TEMP)
#    if temp.USER_LABEL not in temp.LEGAL_LABELS:
#      print "CP1"
#      temp.LEGAL_LABELS.append(temp.USER_LABEL)
#      temp.iClassifier.weights[temp.USER_LABEL] = util.Counter()
#      print "weights = ", temp.iClassifier.weights
    temp.iOutput.display(0,TEMP)
    self.b2['text']="Inputed Label: " + str(TEMP)
    print "Legal Labels = ",temp.LEGAL_LABELS
  def usrDataIter(self):
    global TEMP
    self.iDialog = theDialog(self.container)
    self.container.wait_window(self.iDialog.top)
    temp.USER_ITERATIONS = int(TEMP)
    self.b3['text']="Iteration: " + str(TEMP)
  def percepPos(self):
    global TEMP
    self.iDialog = theDialog(self.container)
    self.container.wait_window(self.iDialog.top)
    temp.POS_WEIGHT = float(TEMP)
    self.b4['text']="Positive Weight: " + str(TEMP)
  def percepNeg(self):
    global TEMP
    self.iDialog = theDialog(self.container)
    self.container.wait_window(self.iDialog.top)
    temp.NEG_WEIGHT = float(TEMP)
    self.b5['text']="Negative Weight: " + str(TEMP)
  def close(self):
    self.frame.destroy()

if __name__ == "__main__":
  root = Tk()
  iSetting = theSetting(root,TOP)



    
