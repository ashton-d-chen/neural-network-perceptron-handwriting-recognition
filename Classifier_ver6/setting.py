from Tkinter import *
import util
import variable
import os
#from Interface import TRAIN_NUM
temp = 0

variable.TRAIN_NUM = 100
variable.AUTO_ITERATIONS=5
variable.USER_LABEL = '0'
variable.USER_ITERATIONS=5
variable.POS_WEIGHT = 1
variable.NEG_WEIGHT = 1
class theDialog:
  def __init__(self, container):

    self.top = Toplevel(container,bg="black")
    Label(self.top, text="Please enter new a value", bg="black", fg="#3cecff").pack()

    self.iEntry = Entry(self.top, bg="#035e89", fg="#3cecff")
    self.iEntry.pack(padx=5)

    b = Button(self.top, text="Enter", bg="black", fg="green", command=self.callUpdate)
    b.pack(pady=5)

  def callUpdate(self):
    global temp 
    temp = self.iEntry.get()
    self.top.destroy()
    

class theSetting:
  def __init__(self, container):
    # Auto Training Settings
    self.container = container
    frame = Frame(container, bd=2, relief=FLAT, background ="black",
                  highlightcolor="red")
    frame.pack(expand=1, fill=X, pady=10, padx=5,side="left")
    lbl = Label(frame, text = "Auto Training Settings ", fg="#3cecff",
                bg="black",font=("times",14,"underline"))
    lbl.pack()
       
    self.b0 = Button(frame, text="Data Amount: " + str(variable.TRAIN_NUM),
                     fg="#3cecff", command=self.autoDataAmount, bg ="black",
                     relief=SOLID, font=(12))
    self.b0.pack(side=TOP)
    self.b1 = Button(frame, text="Iteration: " + str(variable.AUTO_ITERATIONS),
                     fg="#3cecff",command=self.autoDataIter, bg ="black", relief=SOLID,
                     font=("times",12))
    self.b1.pack(side=TOP)
 
   # c7.create_text(65, 30, text=str(TRAIN_NUM), fill="#3cecff", justify=CENTER, font=('times', 14, 'bold'))



    # User Training Settings
    frame = Frame(container, bd=2, relief=FLAT, background ="black",
                  highlightcolor="red")
    frame.pack(expand=1, fill=X, pady=10, padx=5,side="left")
    lbl = Label(frame, text = "User Training Settings ", fg="#3cecff",
                bg="black",font=("times",14, "underline"))
    lbl.pack()
    
    self.b2 = Button(frame, text="Inputed Label: " + str(variable.USER_LABEL), fg="#3cecff",
                        command=self.usrDataLabel, bg ="black", relief=SOLID, font=("times",12))
    self.b2.pack(side=TOP)
    self.b3 = Button(frame, text="Iteration: " + str(variable.USER_ITERATIONS), fg="#3cecff",
                        command=self.usrDataIter, bg ="black", relief=SOLID, font=("times",12))
    self.b3.pack(side=TOP)


    # Perceptron Settings
    frame = Frame(container, bd=2, relief=FLAT, background ="black",
                  highlightcolor="red")
    frame.pack(expand=1, fill=X, pady=10, padx=5,side="left")
    lbl = Label(frame, text = "Perceptron Settings ", fg="#3cecff", bg="black",
                font=("times",14,"underline"))
    lbl.pack()
    self.b4 = Button(frame, text="Positive Weight: " + str(variable.POS_WEIGHT),
                     fg="#3cecff", command=self.percepPos, bg ="black", relief=SOLID, font=("times",12))
    self.b4.pack(side=TOP)
    self.b5 = Button(frame, text="Negative Weight: " + str(variable.NEG_WEIGHT), fg="#3cecff",
                        command=self.percepNeg, bg ="black", relief=SOLID, font=("times",12))
    self.b5.pack(side=TOP)



  def autoDataAmount(self):
    global temp
    self.iDialog = theDialog(self.container)
    self.container.wait_window(self.iDialog.top)
    variable.TRAIN_NUM = int(temp)
    self.b0['text']="Data Amount: " + str(temp)
  def autoDataIter(self):
    global temp
    self.iDialog = theDialog(self.container)
    self.container.wait_window(self.iDialog.top)
    variable.AUTO_ITERATIONS = int(temp)
    self.b1['text']="Iteration: " + str(temp)
  def usrDataLabel(self):
    global temp
    self.iDialog = theDialog(self.container)
    self.container.wait_window(self.iDialog.top)
    variable.USER_LABEL = str(temp)
    if variable.USER_LABEL not in variable.LEGAL_LABELS:
      variable.LEGAL_LABELS.append(variable.USER_LABEL)
      variable.iClassifier.weights[variable.USER_LABEL] = util.Counter()
    self.b2['text']="Inputed Label: " + str(temp)
  def usrDataIter(self):
    global temp
    self.iDialog = theDialog(self.container)
    self.container.wait_window(self.iDialog.top)
    variable.USER_ITERATIONS = int(temp)
    print temp
    self.b3['text']="Iteration: " + str(temp)
  def percepPos(self):
    global temp
    self.iDialog = theDialog(self.container)
    self.container.wait_window(self.iDialog.top)
    variable.POS_WEIGHT = float(temp)
    self.b4['text']="Positive Weight: " + str(temp)
  def percepNeg(self):
    global temp
    self.iDialog = theDialog(self.container)
    self.container.wait_window(self.iDialog.top)
    variable.NEG_WEIGHT = float(temp)
    self.b5['text']="Negative Weight: " + str(temp)


if __name__ == "__main__":
  root = Tk()
  iSetting = theSetting(root)



    
