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


class theControl:
  def __init__(self, container,location): # Import user input

    self.frame = Frame(container, bd=0, relief=RAISED,  background ="black")
    self.button = {}

    # Load User Input
    self.makeButton("Load User Input", self.loadImage)

    # Display Current Weight
    self.makeButton("Current Weight", self.cWeight)
    # Settings
    self.makeButton("Settings", self.settings)
    # User Train
    self.makeButton("User Train",  self.usrTrain)

    # Recognize User Input
    self.makeButton("Recognize User Input", self.recog)
    # Reset
    self.makeButton("Reset", self.reset)
    # Quit
    self.makeButton("Quit", self.goQuit)

    #Auto Training from give set
    self.makeButton("Auto Training", self.autoTrain)

    # Validate Training
    self.makeButton("Validate Training", self.valid)
      
    
    self.frame.pack(expand=1, fill=X, pady=10, padx=5, side=location)

  def makeButton(self, name, command):
    self.button[name]=Button(self.frame, text=name, fg="#3cecff",
                        command=command, bg ="black", relief=SOLID)
    self.button[name].pack(side=TOP)
    
  def autoTrain(self):
  
    self.modBG(self.button["Auto Training"])
    # Load training images
    rawTrainingData = samples.loadDataFile("digitdata/trainingimages",
                                         temp.TRAIN_NUM,temp.DIGIT_DATUM_WIDTH,
                                         temp.DIGIT_DATUM_HEIGHT,temp.LOG_LIST)
    temp.LOG_LIST.insertItem("Training data imported.")
    
    trainingData = map(samples.basicFeatureExtractorDigit, rawTrainingData)
    # Load training Labels    
    trainingLabels = samples.loadLabelsFile("digitdata/traininglabels", temp.TRAIN_NUM,temp.LOG_LIST)
    print trainingLabels
    temp.LOG_LIST.insertItem("Training labels imported.")
    # Training
    temp.iClassifier.train(trainingData, trainingLabels,temp.AUTO_ITERATIONS,temp.LOG_LIST)
    temp.LOG_LIST.insertItem("Training Completed.")
    temp.LOG_LIST.insertItem("==================")
    

    
  def valid(self):
    global iClassifier
    global pCorrect, c5, c5Temp
    self.modBG(self.button["Validate Training"])

    rawValidationData = samples.loadDataFile("digitdata/validationimages",
                                             temp.TEST_SET_SIZE,temp.DIGIT_DATUM_WIDTH,
                                             temp.DIGIT_DATUM_HEIGHT,temp.LOG_LIST)
    temp.LOG_LIST.insertItem("Testing data imported.")
    validationLabels = samples.loadLabelsFile("digitdata/validationlabels",
                                              temp.TEST_SET_SIZE,temp.LOG_LIST)
    temp.LOG_LIST.insertItem("Testing labels imported.")
    validationData = map(samples.basicFeatureExtractorDigit, rawValidationData)
    

    guesses = temp.iClassifier.classify(validationData,temp.LOG_LIST)
    correct = [guesses[i] == validationLabels[i] for i in range(len(validationLabels))].count(True)
    temp.LOG_LIST.insertItem(str(correct) + (" correct out of " + str(len(validationLabels))))
    temp.LOG_LIST.insertItem("=========================")
    temp.iOutput.display(1,str(100.0 * correct / len(validationLabels))+"%")
    
    
  def loadImage(self):
    self.modBG(self.button["Load User Input"])
    temp.LOG_LIST.insertItem("Loading user image...")
    convert.loadImage()

            
  def recog(self):
    global iClassifier
    global iClassifier, c4Temp

    self.modBG(self.button["Recognize User Input"])
    rawTestData = samples.loadDataFile("digitdata/testingimages",
                                     1, temp.DIGIT_DATUM_WIDTH,
                                     temp.DIGIT_DATUM_HEIGHT,temp.LOG_LIST)
    testData = map(samples.basicFeatureExtractorDigit, rawTestData)
    guess = temp.iClassifier.classify(testData,temp.LOG_LIST)
    temp.iOutput.display(1,guess[0])


  def cWeight(self):
    print "weighs = ",temp.iClassifier.weights
    if len(temp.iClassifier.weights)>0:                
      print temp.iClassifier.weights
      for k in temp.iClassifier.weights:
        print " " 
        for i in range(28):
          line = ''
          for j in range(28):
            line += str(temp.iClassifier.weights[k][(i,j)])
          print line  
                           
  def usrTrain(self):
    
    self.modBG(self.button["Auto Training"])
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
   
    '''
    global root
    self.modBG(self.button["User Train"])


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
    temp.LOG_LIST.insertItem("Training labels imported.")
    # Training
    #print temp.USER_ITERATIONS
    temp.iClassifier.train(trainingData, trainingLabels,temp.USER_ITERATIONS,temp.LOG_LIST)
    temp.LOG_LIST.insertItem("Training Completed.")
    temp.LOG_LIST.insertItem("==================")
    '''

  def settings(self):
    self.modBG(self.button["Settings"])
    iSetting = setting.theSetting(self.frame,TOP)
    
  def reset(self):
    self.modBG(self.button["Reset"])
            
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
