from Tkinter import *
from PIL import Image
import perceptron
import samples
import sys
import util
import time
import tkFont

STATUS_X = 80
STATUS_Y = 40
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
c7 = 0
myList = 0
text = []
TRAIN_NUM = 100
legalLabels = range(10)		# number of labels
TEST_SET_SIZE = 100
DIGIT_DATUM_WIDTH=28
DIGIT_DATUM_HEIGHT=28
iClassifier = []
pCorrect = 0
c5Temp = 0
c4Temp = 0



class MyDialog:
    def __init__(self, parent):

        top = self.top = Toplevel(parent)

        Label(top, text="Value").pack()

        self.e = Entry(top)
        self.e.pack(padx=5)

        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):

        print "value is", self.e.get()

        self.top.destroy()
        
def basicFeatureExtractorDigit(datum):
  """
  Returns a set of pixel features indicating whether
  each pixel in the provided datum is black, gray, or white.
  """
  a = datum.getPixels()

  features = util.Counter()
  for x in range(DIGIT_DATUM_WIDTH):
    for y in range(DIGIT_DATUM_HEIGHT):
      if datum.getPixel(x, y) > 0:
        features[(x,y)] = 1
      else:
        features[(x,y)] = 0
  return features

def loadImage():
  global text, myList
  WIDTH = 28
  HEIGHT = 28
  try:
      temp = Image.open("digitdata/input.bmp")
      myList.insertItem("Open file...")
  except:
      myList.insertItem("Can't open file.")
      return
  im = temp.resize((WIDTH,HEIGHT))
  temp = []
  for i in range(len(im.getdata())):
    temp.append(im.getdata()[i])
  im = temp[:]
  result = []

  for i in range(0,28):
    test = ''
    result.append([])
    for j in range(0,28):
      if im[i*28+j] == (255,255,255):
        result[i].append(' ')
      elif im[i*28+j] == (0,0,0):
        result[i].append('#')
      test += result[i][j]


  text_file = open("digitdata/testingimages", "w")
  count = 20
  tempText = []
  for i in range(0,28):
    temp = ''
    for j in range(0,28):
      if result[i][j] == ' ':
        if i < 27 and result[i+1][j] == '#':
          result[i][j] = '+'
        elif i > 0 and result[i-1][j] == '#':
          result[i][j] = '+'
        elif j < 27 and result[i][j+1]== '#':
          result[i][j] = '+'
        elif j > 0 and result[i][j-1] == '#':
          result[i][j] = '+'
      temp += result[i][j]
      text_file.write(result[i][j])
    if len(text) != 0:
        c3.delete(text[i])
    tempText.append(c3.create_text(120, count, text=temp, fill="#3cecff", justify=CENTER, font=('courier', 10)))
    count += 10
    if i < 27:
      text_file.write("\n")
    if i == 27:
      text_file.write(" ")
  text = tempText[:]
  text_file.close()
  myList.insertItem("Loading completed.")
  myList.insertItem("==================")



class theList:
  def __init__(self,root):
    frame = Frame(root, height=15, width=18, bg="black")
      

    self.l = Listbox(frame, height=15, width=18,bg = "black", fg="green", font=('times', 12))
    scroll = Scrollbar(frame, command=self.l.yview)

    self.l.configure(yscrollcommand=scroll.set)
    self.l.pack(side=LEFT)
    scroll.pack(side=LEFT, fill=Y)
    #frame.pack(expand=1, fill=X,pady=10,padx=5,sid="top")
    frame.pack(side="left")

  def insertItem(self,message):
    self.l.insert(END, message)
    self.l.see(END)


class myButton:
  def __init__(self, frame): # Import user input
    self.b = []
    # Auto Training from given set
    self.b0 = Button(frame, text="Auto Training", fg="#3cecff",
                        command=self.autoTrain, bg ="black", relief=SOLID)
    self.b0.pack(side=TOP)

    # Validate Training
    self.b1 = Button(frame, text="Validate", fg="#3cecff",
                        command=self.valid, bg ="black", relief=SOLID)
    self.b1.pack(side=TOP)

    # Load User Input
    self.b2 = Button(frame, text="Load\nUser Input", fg="#3cecff",
                       command=self.loadImage, bg ="black", relief=SOLID)
    self.b2.pack(side=TOP)

    # Recognize user input
    self.b3 = Button(frame, text="Recognize\nUser Input", fg="#3cecff",
                        command=self.recog, bg ="black", relief=SOLID)
    self.b3.pack(side=TOP)
    
    # User input Training
    self.b4 = Button(frame, text="User Input\nTraining", fg="#3cecff",
                        command=self.usrTrain, bg ="black", relief=SOLID)
    self.b4.pack(side=TOP)
    
    # Reset
    self.b5 = Button(frame, text="Reset", fg="#3cecff",
                        command=self.reset, bg ="black", relief=SOLID)
    self.b5.pack(side=TOP)

    # Quit
    self.b6 = Button(frame, text="QUIT", fg="#3cecff",
                         command=self.goQuit, bg="black", relief=SOLID)
    self.b6.pack(side=BOTTOM)

    self.s = [self.b0, self.b1, self.b2, self.b3, self.b4, self.b5, self.b6]

  def autoTrain(self):
    global TRAIN_NUM, iClassifier, DIGIT_DATUM_HEIGHT, DIGIT_DATUM_WIDTH,myList
    self.b0["background"] = "blue"
    self.b0["fg"] = "#FFF"
    for i in self.s:
        if i != self.b0:
            i["background"] = "black"
            i["fg"] = "#3cecff"
    
    # Load training images
    rawTrainingData = samples.loadDataFile("digitdata/trainingimages",
                                         TRAIN_NUM,DIGIT_DATUM_WIDTH,
                                         DIGIT_DATUM_HEIGHT,myList)
    myList.insertItem("Training data imported.")
    
    trainingData = map(basicFeatureExtractorDigit, rawTrainingData)
    # Load training Labels    
    trainingLabels = samples.loadLabelsFile("digitdata/traininglabels", TRAIN_NUM,myList)
    myList.insertItem("Training labels imported.")
    # Training
    iClassifier.train(trainingData, trainingLabels,myList)
    myList.insertItem("Training Completed.")
    myList.insertItem("==================")
    

    
  def valid(self):
    global TRAIN_NUM, iClassifier, DIGIT_DATUM_HEIGHT
    global DIGIT_DATUM_WIDTH,myList,pCorrect, c5, c5Temp
    for i in self.s:
        if i != self.b1:
            i["background"] = "black"
            i["fg"] = "#3cecff"

    self.b1["background"] = "blue"
    self.b1["fg"] = "#FFF"

    rawValidationData = samples.loadDataFile("digitdata/validationimages",
                                             TEST_SET_SIZE,DIGIT_DATUM_WIDTH,
                                             DIGIT_DATUM_HEIGHT,myList)
    myList.insertItem("Testing data imported.")
    validationLabels = samples.loadLabelsFile("digitdata/validationlabels",
                                              TEST_SET_SIZE,myList)
    myList.insertItem("Testing labels imported.")
    validationData = map(basicFeatureExtractorDigit, rawValidationData)
    

    guesses = iClassifier.classify(validationData,myList)
    correct = [guesses[i] == validationLabels[i] for i in range(len(validationLabels))].count(True)
    myList.insertItem(str(correct) + (" correct out of " + str(len(validationLabels)))) 
    if c5Temp != 0:
      c5.delete(c5Temp) 
    c5Temp = c5.create_text(65, 30, text=str(100.0 * correct / len(validationLabels))+"%", fill="#3cecff", justify=CENTER, font=('times', 24, 'bold'))
    myList.insertItem("=========================")

    
  def loadImage(self):
    global c2, STATUS_Y, myList

    self.b2["background"] = "blue"
    self.b2["fg"] = "#FFF"
    myList.insertItem("Loading user image...")
    loadImage()
    for i in self.s:
        if i != self.b2:
            i["background"] = "black"
            i["fg"] = "#3cecff"
            
  def recog(self):
    global TRAIN_NUM, iClassifier, DIGIT_DATUM_HEIGHT
    global DIGIT_DATUM_WIDTH,myList, iClassifier, c4Temp

    self.b3["background"] = "blue"
    self.b3["fg"] = "#FFF"
    for i in self.s:
        if i != self.b3:
            i["background"] = "black"
            i["fg"] = "#3cecff"
    rawTestData = samples.loadDataFile("digitdata/testingimages",
                                     1, DIGIT_DATUM_WIDTH,
                                     DIGIT_DATUM_HEIGHT,myList)
    testLabels = samples.loadLabelsFile("digitdata/testlabels", TEST_SET_SIZE,myList)
    testData = map(basicFeatureExtractorDigit, rawTestData)
    guess = iClassifier.classify(testData,myList)
    if c4Temp != 0:
      c4.delete(c4Temp) 
    c4Temp = c4.create_text(65, 30, text=guess[0], fill="#3cecff", justify=CENTER, font=('times', 24, 'bold'))


  def usrTrain(self):
    global TRAIN_NUM, iClassifier, DIGIT_DATUM_HEIGHT
    global root, DIGIT_DATUM_WIDTH,myList

    self.b4["background"] = "blue"
    self.b4["fg"] = "#FFF"  
    for i in self.s:
        if i != self.b4:
            i["background"] = "black"
            i["fg"] = "#3cecff"
    d = MyDialog(root)
    root.wait_window(d.top)

    # Load training images
    rawTrainingData = samples.loadDataFile("digitdata/testingimages",
                                         TRAIN_NUM,DIGIT_DATUM_WIDTH,
                                         DIGIT_DATUM_HEIGHT,myList)
    myList.insertItem("Training data imported.")
    
    trainingData = map(basicFeatureExtractorDigit, rawTrainingData)
    # Load training Labels    
    trainingLabels = samples.loadLabelsFile("digitdata/traininglabels", TRAIN_NUM,myList)
    myList.insertItem("Training labels imported.")
    # Training
    iClassifier.train(trainingData, trainingLabels,myList)
    myList.insertItem("Training Completed.")
    myList.insertItem("==================")
    

  def reset(self):
    self.b5["background"] = "blue"
    self.b5["fg"] = "#FFF"
    for i in self.s:
        if i != self.b5:
            i["background"] = "black"
            i["fg"] = "#3cecff"
            
  def goQuit(self):
    global root
    self.b6["background"] = "blue"
    self.b6["fg"] = "#FFF"
    for i in self.s:
        if i != self.b6:
            i["background"] = "black"
            i["fg"] = "#3cecff"
    exit()
          
class AllTkinterWidgets:
  def __init__(self, master):
    global c1, c2, c3, c4, c5, myList, legalLabels, iClassifier
    frame = Frame(master, width=700, height=600, bd=1, background ="black")
    frame.pack()
   
    iframe5 = Frame(frame, bd=0, relief=FLAT, background ="black")
    iframe5.pack(expand=1, fill=X, pady=10, padx=5,side="top")
    c1 = Canvas(iframe5, bg='white', width=700, height=50,background="black")
    c1.pack()

    iframe5 = Frame(frame, bd=0, relief=RAISED, background ="black", highlightcolor="red")
    iframe5.pack(expand=1, fill=X, pady=10, padx=5,side="bottom") 

    iframe7 = Frame(iframe5, bd=0, relief=RAISED, background ="black", highlightcolor="red")
    iframe7.pack(expand=1, fill=X, pady=10, padx=5,side="left")
    lbl = Label(iframe7, text = "Auto Training Settings ", fg="#3cecff", bg="black",font=("times",14,"bold"))
    lbl.pack()
    c7 = Canvas(iframe7, width=70, height=50,background="black")
    c7.pack()

    iframe7 = Frame(iframe5, bd=0, relief=RAISED, background ="black", highlightcolor="red")
    iframe7.pack(expand=1, fill=X, pady=10, padx=5,side="left")
    lbl = Label(iframe7, text = "Validation Settings", fg="#3cecff", bg="black",font=("times",14,"bold"))
    lbl.pack()
    c7 = Canvas(iframe7, width=70, height=50,background="black")
    c7.pack()

    iframe7 = Frame(iframe5, bd=0, relief=RAISED, background ="black", highlightcolor="red")
    iframe7.pack(expand=1, fill=X, pady=10, padx=5,side="left")
    lbl = Label(iframe7, text = "User Training Settings ", fg="#3cecff", bg="black",font=("times",14,"bold"))
    lbl.pack()
    c4 = Canvas(iframe7, width=70, height=50,background="black")
    c4.pack()
 
    iframe7 = Frame(iframe5, bd=0, relief=RAISED, background ="black", highlightcolor="red")
    iframe7.pack(expand=1, fill=X, pady=10, padx=5,side="right")
    lbl = Label(iframe7, text = "Perceptron Settings", fg="#3cecff", bg="black",font=("times",14,"bold"))
    lbl.pack()
    c7 = Canvas(iframe7, width=70, height=50,background="black")
    c7.pack()
    
    # Status Frame
    iframe5 = Frame(frame, bd=0, relief=RAISED,  background ="black")
    iframe5.pack(expand=1, fill=X, pady=10, padx=5, side="left")
    lbl = Label(iframe5, text = "System Status", fg="#3cecff", bg="black",font=("times",14,"bold"))
    lbl.pack()
 #   c2 = Canvas(iframe5, bg='white', width=175, height=400,background="black")
    #c2.pack()

    # Add a log list
    myList = theList(iframe5)


    # User Input Frame 
    iframe5 = Frame(frame, bd=0, relief=RAISED,  background ="black")
    iframe5.pack(expand=1, fill=X, pady=10, padx=5, side="left")
    lb2 = Label(iframe5, text = "User Input", fg = "#3cecff", bg = "black", font = ("times",14,"bold"))
    lb2.pack(side="top")
    c3 = Canvas(iframe5, width=235, height=300,background="black")
    c3.pack()   

    iframe5 = Frame(frame, bd=0, relief=RAISED,  background ="black")        
    iframe5.pack(expand=1, fill=X, pady=10, padx=5, side="right")
    myButton(iframe5)        
    # System Output Frame
    
    iframe5 = Frame(frame, bd=0, relief=RAISED,  background ="black")
    iframe5.pack(expand=1, fill=X, pady=10, padx=5, side="top")
    lb2 = Label(iframe5, text = "Guess Digit", fg = "#3cecff", bg = "black", font = ("times",14,"bold"))
    lb2.pack(side="top")
    c4 = Canvas(iframe5, bg='white', width=130, height=60, background="black")
    c4.pack()

    
    iframe5 = Frame(frame, bd=0, relief=RAISED,  background ="black")
    iframe5.pack(expand=1, fill=X, pady=10, padx=5, side="top")
    lb2 = Label(iframe5, text = "Predicted Correct", fg = "#3cecff", bg = "black", font = ("times",14,"bold"))
    lb2.pack(side="top")
    c5 = Canvas(iframe5, bg='white', width=130, height=60, background="black")
    c5.pack()
    
    iframe5 = Frame(frame, bd=0, relief=RAISED,  background ="black")
    iframe5.pack(expand=1, fill=X, pady=10, padx=5, side="top")
    lb2 = Label(iframe5, text = "User Input\nCorrectness Statistics", fg = "#3cecff", bg = "black", font = ("times",14,"bold"))
    lb2.pack(side="top")
    c6 = Canvas(iframe5, bg='white', width=130, height=60, background="black")
    c6.pack()    

    

    c5.create_text(80, 280, text='Correctness', fill="#3cecff", justify=CENTER, font=('times', 14, 'bold'))
    
    c1.create_text(330, 25, text='Perceptron Handwriting Recognition', fill="#3cecff", justify=CENTER,font=('Times', 20, 'bold'))
   # c3.create_text(130, 20, text='User Input', fill="#3cecff", justify=CENTER, font=('times', 14, 'bold'))
  #  c3.create_text(130, 320, text='Predicted Correctness', fill="#3cecff", justify=CENTER, font=('times', 14, 'bold'))
    

    
    c5.create_text(80, 280, text='Correctness', fill="#3cecff", justify=CENTER, font=('times', 14, 'bold'))
    c5.create_text(80, 296, text='Statistics', fill="#3cecff", justify=CENTER, font=('times', 14, 'bold'))
    c6.create_text(80, 20, text='Statistics', fill="#3cecff", justify=CENTER, font=('times', 14, 'bold'))


    
    iClassifier = perceptron.PerceptronClassifier(legalLabels)
    # Select classifier



        
        
    
root = Tk()
root.option_add('*font', ('verdana', 10, 'bold'))
interface = AllTkinterWidgets(root)
root.title('Tkinter Widgets')

root.mainloop()
