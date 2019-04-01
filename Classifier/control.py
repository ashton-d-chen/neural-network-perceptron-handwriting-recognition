'''
File: Control.py
Author: Jann-Chyi Chen
Version: 1.0
Date: 2008-03-19
Description: Control.py create a control panel for the user. User can use the
  created control panel to create a datum object from a input image. In addition,
  user can assign a label for a class of prototype weights. User can train the
  perceptron classifier and command it to identify a given image.
'''



from Tkinter import *
import samples        # open a datum file 
import temp           # stores a set of global variables
import perceptron     
import convert        # convert input image to a datum object and save it
import util           
TEMP = 0              # temporary stores an entry value  



'''
A class of objects which creates a pop-up window asking user for an entry value.
'''
class theDialog:
  def __init__(self, container):

    # create a pop-up window
    self.top = Toplevel(container,bg="black")
    Label(self.top, text="Please enter new a value", bg="black", fg="#3cecff").pack()

    # create an entry
    self.iEntry = Entry(self.top, bg="#035e89", fg="#3cecff")
    self.iEntry.pack(padx=5)

    # create an "Enter" button
    b = Button(self.top, text="Enter", bg="black", fg="green", command=self.callUpdate)
    b.pack(pady=5)

  # save entry variable to a global variable
  def callUpdate(self):
    global TEMP 
    TEMP = self.iEntry.get()
    self.top.destroy()
    

'''
A class of objects which creates a control panel for user to control the
program execution
'''
class theControl:
  def __init__(self, container,location): 

    # create a frame
    self.frame = Frame(container, bd=0, relief=RAISED,  background ="black")
    self.button = {}

    # Load User Input
    self.makeButton("Load Input", self.loadImage)

    # Enter User Input Label
    self.makeButton("Label Entered", self.usrDataLabel)

    # Display Current Weight
    self.makeButton("Current Weight", self.cWeight)
    
    # Train
    self.makeButton("Training",  self.usrTrain)

    # Recognize User Input
    self.makeButton("Recognize", self.recog)

    # toggle
    self.makeButton("Toggle", self.toggle)
    
    # Quit
    self.makeButton("Quit", self.goQuit)
    
    self.frame.pack(expand=1, fill=X, pady=10, padx=5, side=location)



  # a method which create a button with specific style
  def makeButton(self, name, command):
    self.button[name]=Button(self.frame, text=name, fg="#3cecff",
                        command=command, bg ="black", relief=SOLID)
    self.button[name].pack(side=TOP)


    
  # command the program to convert an input image to a datum object and save it
  def loadImage(self):
    self.modBG(self.button["Load Input"])
    temp.LOG_LIST.insertItem("Loading image...")
    convert.loadImage()
    temp.LOG_LIST.insertItem("Datum object created successfully")



  # open a pop-up window which ask user for the label of input datum object
  def usrDataLabel(self):
    global TEMP
    self.modBG(self.button["Label Entered"])
    self.iDialog = theDialog(self.frame)    # creates a pop-up window
    self.frame.wait_window(self.iDialog.top)
    temp.USER_LABEL = str(TEMP)
    temp.LOG_LIST.insertItem("User-defined label " + str(TEMP) + " entered")

    # if entered label is not currently within program record,
    # create a new entry and a class of weights for that label
    if temp.USER_LABEL not in temp.LEGAL_LABELS:
      temp.LOG_LIST.insertItem("Entered label is not in data base, create\
                               a new label class")
      
      # create a new entry
      temp.LEGAL_LABELS.append(temp.USER_LABEL)  

      # create a new class of weights of 0s 
      temp.iClassifier.weights[temp.USER_LABEL] = util.Counter()

      # initialize the weights under new class
      for i in range(28):
        for j in range(28):
          temp.iClassifier.weights[TEMP][(i,j)] = 0
      temp.LOG_LIST.insertItem("Weights of new label class initialized")

    # display entered label on the GUI
    temp.iOutput.display(0,TEMP)

    

  # commands the program to recognize or identify input datum object.   
  def recog(self):
    self.modBG(self.button["Recognize"])

    temp.LOG_LIST.insertItem("Start recognizing...")
    # read datum object
    testData = samples.loadDataFile("datum",
                                     1, temp.DIGIT_DATUM_WIDTH,
                                     temp.DIGIT_DATUM_HEIGHT,temp.LOG_LIST)


    # make a guess of input image using perceptron classifier
    guess = temp.iClassifier.classify(testData,temp.LOG_LIST)
    guess = guess[0]
    print guess
    temp.LOG_LIST.insertItem("Recognizing completed.")
    
    # display guess result
    temp.iOutput.display(1,guess)

    ### Display weights of guessed Label ###
    temp.LOG_LIST.insertItem("Display weights of relative label class")    
    if guess != temp.USER_LABEL or guess == '':
      temp.LOG_LIST.insertItem("Guessed label does not \
                                match the one entered by user")    
      temp.PRE_GUESS = guess
    else:
      guess = temp.PRE_GUESS

    count = 20
    tempText = []
    for i in range(28):
      TEMP = ''
      for j in range(28):
        if temp.iClassifier.weights[guess][(j,i)] > 0 or\
           (temp.iClassifier.weights[guess][(j,i)] == 0 and temp.mode == 0):
          TEMP += (' ' + str(temp.iClassifier.weights[guess][(j,i)]))
        elif temp.iClassifier.weights[guess][(j,i)] == 0:
          TEMP += '  '
        else:
          TEMP += str(temp.iClassifier.weights[guess][(j,i)])

      # erase previous item on canvas if there is any
      if len(temp.curInputText) != 0:
          temp.currentWeight.canvas.delete(temp.curInputText[i])

      # insert item onto canvas
      tempText.append(temp.currentWeight.canvas.create_text(235, count,
                                                            text=TEMP,
                                                            fill="#3cecff",
                                                            justify=LEFT,
                                                            font=('courier', 10)))
      count += 10


    temp.curInputText = tempText[:]      # save the canvas object

    # Change the title of the canvas
    temp.currentWeight.label["text"] = "Weights of Label " + guess

    
    
    ### Display weights of user-entered label ###
    count = 20
    tempText = []
    for i in range(28):
      TEMP = ''
      for j in range(28):
        if temp.iClassifier.weights[temp.USER_LABEL][(j,i)] > 0 or\
           (temp.iClassifier.weights[temp.USER_LABEL][(j,i)] == 0 and temp.mode == 0):
          TEMP += (' ' + str(temp.iClassifier.weights[temp.USER_LABEL][(j,i)]))
        elif temp.iClassifier.weights[guess][(j,i)] == 0:
          TEMP += '  '
        else:
          TEMP += str(temp.iClassifier.weights[temp.USER_LABEL][(j,i)])

      # erase previous item on the canvas if there is any
      if len(temp.usrInputText) != 0:
          temp.inputWeight.canvas.delete(temp.usrInputText[i])

      # append each line of pixel 
      tempText.append(temp.inputWeight.canvas.create_text(235,
                                                          count,
                                                          text=TEMP,
                                                          fill="#3cecff",
                                                          justify=LEFT,
                                                          font=('courier', 10)))
      count += 10
    temp.usrInputText = tempText[:]     # save the canvas object
    temp.inputWeight.label["text"] = "Weight of Label " + temp.USER_LABEL


  '''
  Displays all the classes of weights on terminal
  '''
  def cWeight(self):
    if len(temp.iClassifier.weights)>0: # if there is any clases in record

      # extract and sort keys from the dictionary
      keys = temp.iClassifier.weights.keys()
      keys.sort()

      # print weights of each class on terminal
      for key in keys:
        print " "
        print "Label = ", key
        for i in range(28):
          line = ""
          for j in range(28):
            if temp.iClassifier.weights[key][(j,i)] >= 0:
              line += "+" + str(temp.iClassifier.weights[key][(j,i)])
            else:
              line += str(temp.iClassifier.weights[key][(j,i)])
          print line
          
  '''
  Train the perceptron classifier
  '''
  def usrTrain(self):
    
    self.modBG(self.button["Training"])

    # Load input datum object
    trainingData = samples.loadDataFile("datum",
                                         1,temp.DIGIT_DATUM_WIDTH,
                                         temp.DIGIT_DATUM_HEIGHT,temp.LOG_LIST)
    temp.LOG_LIST.insertItem("Training data imported.")
    
    # convert each pixel of datum object to its corresponding value
    #trainingData = map(samples.basicFeatureExtractorDigit, rawTrainingData)
    trainingLabels = []
    trainingLabels.append(temp.USER_LABEL)
    
    # Training
    temp.iClassifier.train(trainingData, trainingLabels,1,temp.LOG_LIST)
    temp.LOG_LIST.insertItem("Training Completed.")
    temp.LOG_LIST.insertItem("==================")

  '''
  toggle view
  '''
  def toggle(self):
    if temp.mode == 0:   
      temp.mode = 1
    elif temp.mode == 1:
      temp.mode = 0
    self.recog()
  '''
  Exit the program
  '''
  def goQuit(self):
    self.modBG(self.button["Quit"])
    exit()

  '''
  Changes the color of a clicked button
  '''
  def modBG(self,item):
    item["background"] = "blue"
    item["fg"] = "#FFF"
    for i in self.button:
      if self.button[i] != item:
          self.button[i]["background"] = "black"
          self.button[i]["fg"] = "#3cecff"


