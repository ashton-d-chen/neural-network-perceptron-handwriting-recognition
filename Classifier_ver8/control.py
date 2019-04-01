from Tkinter import *
import samples
import temp
import log
import perceptron
import convert
import title
import setting
import display
import output
import util
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
    

class theControl:
  def __init__(self, container,location): # Import user input

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
    self.makeButton("Recognize User Input", self.recog)

    # Quit
    self.makeButton("Quit", self.goQuit)


    
    self.frame.pack(expand=1, fill=X, pady=10, padx=5, side=location)


  def makeButton(self, name, command):
    self.button[name]=Button(self.frame, text=name, fg="#3cecff",
                        command=command, bg ="black", relief=SOLID)
    self.button[name].pack(side=TOP)
    

    
  def loadImage(self):
    self.modBG(self.button["Load Input"])
    temp.LOG_LIST.insertItem("Loading user image...")
    convert.loadImage()

  def usrDataLabel(self):
    global TEMP
    self.modBG(self.button["Label Entered"])
    self.iDialog = theDialog(self.frame)
    self.frame.wait_window(self.iDialog.top)
    temp.USER_LABEL = str(TEMP)
    if temp.USER_LABEL not in temp.LEGAL_LABELS:
      temp.LEGAL_LABELS.append(temp.USER_LABEL)
      temp.iClassifier.weights[temp.USER_LABEL] = util.Counter()
    temp.iOutput.display(0,TEMP)
    for i in range(28):
      for j in range(28):
        temp.iClassifier.weights[TEMP][(i,j)] = 0
    print temp.LEGAL_LABELS

            
  def recog(self):
    global iClassifier
    global iClassifier, c4Temp

    self.modBG(self.button["Recognize User Input"])
    rawTestData = samples.loadDataFile("digitdata/testingimages",
                                     1, temp.DIGIT_DATUM_WIDTH,
                                     temp.DIGIT_DATUM_HEIGHT,temp.LOG_LIST)
    testData = map(samples.basicFeatureExtractorDigit, rawTestData)
    guess = temp.iClassifier.classify(testData,temp.LOG_LIST)
    guess = guess[0]
    temp.iOutput.display(1,guess)

    print "guess = ", guess
    # Display Weight of Guessed Label
    if guess != temp.USER_LABEL:
      temp.PRE_GUESS = guess
    if temp.PRE_GUESS != '':
      guess = temp.PRE_GUESS
      
    count = 20
    tempText = []
    for i in range(28):
      TEMP = ''
      for j in range(28):
        if temp.iClassifier.weights[guess][(j,i)] >= 0:
          TEMP += (' ' + str(temp.iClassifier.weights[guess][(j,i)]))
        else:
          TEMP += str(temp.iClassifier.weights[guess][(j,i)])
      if len(temp.curInputText) != 0:
          temp.currentWeight.canvas.delete(temp.curInputText[i])
      tempText.append(temp.currentWeight.canvas.create_text(235, count, text=TEMP, fill="#3cecff", justify=LEFT, font=('courier', 10)))
      count += 10
    temp.curInputText = tempText[:]
    temp.currentWeight.label["text"] = "Weight of Label " + guess
    
    
    # Display Result of Recognizing
    count = 20
    tempText = []
    for i in range(28):
      TEMP = ''
      for j in range(28):
        if temp.iClassifier.weights[temp.USER_LABEL][(j,i)] >= 0:
          TEMP += (' ' + str(temp.iClassifier.weights[temp.USER_LABEL][(j,i)]))
        else:
          TEMP += str(temp.iClassifier.weights[temp.USER_LABEL][(j,i)])
      if len(temp.usrInputText) != 0:
          temp.inputWeight.canvas.delete(temp.usrInputText[i])
      tempText.append(temp.inputWeight.canvas.create_text(235, count, text=TEMP, fill="#3cecff", justify=LEFT, font=('courier', 10)))
      count += 10
    temp.usrInputText = tempText[:]
    temp.inputWeight.label["text"] = "Weight of Label " + temp.USER_LABEL


  def cWeight(self):
    if len(temp.iClassifier.weights)>0:                
      keys = temp.iClassifier.weights.keys()
      keys.sort()
      
      for key in keys:
        print " "
        print "Label = ", key
        for i in range(28):
          line = ''
          for j in range(28):
            if temp.iClassifier.weights[key][(j,i)] >= 0:
              line += '+' + str(temp.iClassifier.weights[key][(j,i)])
            else:
              line += str(temp.iClassifier.weights[key][(j,i)])
          print line
          

  def usrTrain(self):
    
    self.modBG(self.button["Training"])
    # Load training images
    rawTrainingData = samples.loadDataFile("digitdata/testingimages",
                                         1,temp.DIGIT_DATUM_WIDTH,
                                         temp.DIGIT_DATUM_HEIGHT,temp.LOG_LIST)
    temp.LOG_LIST.insertItem("Training data imported.")
    
    trainingData = map(samples.basicFeatureExtractorDigit, rawTrainingData)
    # Load training Labels    
    #trainingLabels = samples.loadLabelsFile("digitdata/traininglabels", temp.TRAIN_NUM,temp.LOG_LIST)
    trainingLabels = []
    trainingLabels.append(temp.USER_LABEL)
    print temp.USER_LABEL
    print trainingLabels
    temp.LOG_LIST.insertItem("Training labels imported.")
    # Training
    temp.iClassifier.train(trainingData, trainingLabels,1,temp.LOG_LIST)
    temp.LOG_LIST.insertItem("Training Completed.")
    temp.LOG_LIST.insertItem("==================")
   

  def goQuit(self):
    self.modBG(self.button["Quit"])
    exit()





  def modBG(self,item):
    item["background"] = "blue"
    item["fg"] = "#FFF"
    for i in self.button:
      if self.button[i] != item:
          self.button[i]["background"] = "black"
          self.button[i]["fg"] = "#3cecff"    

# Test code    
if __name__ == "__main__":
  root = Tk()
  frame = Frame(root)
  temp.LOG_LIST = log.theLog(frame,TOP)
  iControl = theControl(root,TOP)

  
  temp.iClassifier = perceptron.PerceptronClassifier()
    
  temp.iTitle = title.theTitle(frame,TOP)

  # Add setting option
  #temp.iSetting = setting.theSetting(frame,TOP)

  # Add a log list
  temp.LOG_LIST = log.theLog(frame,TOP)

  # User Input Image
  temp.iDisplay = display.theDisplay(frame,"hi",TOP)

  # System Output Frame
  temp.iOutput = output.theOutput(frame,TOP)

  
  # Control pansel
  temp.iControl = theControl(frame,TOP)
  
  # Select classifier
  temp.iClassifier = perceptron.PerceptronClassifier()
