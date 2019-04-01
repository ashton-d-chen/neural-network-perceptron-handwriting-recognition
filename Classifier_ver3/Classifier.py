
TEST_SET_SIZE = 1
DIGIT_DATUM_WIDTH=28
DIGIT_DATUM_HEIGHT=28


TK_ROOT = None
SP_CANVAS = None
LOG_X = 30
LOG_Y = 30


import perceptron
import samples
import sys
import util
from Tkinter import *
import tkFont

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

def printImage(pixels,width,height):
  """
  Generates a Datum object that contains all pixels in the 
  provided list of pixels.  This will serve as a helper function
  to the analysis function you write.
  """
  image = samples.Datum(None,width,height)
  for x, y in pixels:
    image.pixels[x][y] = 2
  print image  
  
from PIL import Image


def loadImage():
  WIDTH = 28
  HEIGHT = 28
  temp = Image.open("input.bmp")
  im = temp.resize((WIDTH,HEIGHT))
  im = list(im.getdata())
  result = []

  for i in range(0,28):
    test = ''
    for j in range(0,28):
      if im[i*28+j] == (255,255,255):
        result.append(' ')
      elif im[i*28+j] == (0,0,0):
        result.append('#')
      test += result[i*28+j]
    print test

  text_file = open("digitdata/testingimages", "w")
  for i in range(0,27):
    test = ''
    for j in range(0,27):
      if result[i*28+j] == ' ':
        if result[(i+1)*28+j] == '#':
          result[i*28+j] = '+'
        elif result[(i-1)*28+j] == '#':
          result[i*28+j] = '+'
        elif result[i*28+j+1]== '#':
          result[i*28+j] = '+'
        elif result[i*28+j-1] == '#':
          result[i*28+j] = '+'
          
      text_file.write(result[i*28+j])
    text_file.write(" ")
    text_file.write("\n")
  text_file.write("                            ")
  text_file.write("\n")
  text_file.write("                            ")
  text_file.close()




  






def runClassifier():
  global TK_ROOT, SP_CANVAS, LOG_X, LOG_Y
  TK_ROOT = Tk(className="Classifier Interface") # Create window
  TK_ROOT.geometry("1024x768")
  TK_ROOT.grid_rowconfigure(0, weight=1)
  TK_ROOT.grid_columnconfigure(0, weight=1)
  SP_CANVAS = Canvas(TK_ROOT, xscrollcommand=None, scrollcommand=None)
  SP_CANVAS.grid(row=0,column=0,sticky='nesw')
  SP_CANVAS.create_rectangle(10, 10, 150, 500,fill="white")
  

  # Set up variables according to the command line inputs  
  featureFunction = basicFeatureExtractorDigit
  
  legalLabels = range(10)		# number of labels

  # Select classifier
  classifier = perceptron.PerceptronClassifier(legalLabels)
      
  # Load data  
  numTraining = 1


  rawTrainingData = samples.loadDataFile("digitdata/trainingimages",
                                         numTraining,DIGIT_DATUM_WIDTH,
                                         DIGIT_DATUM_HEIGHT,'train',SP_CANVAS)

  trainingLabels = samples.loadLabelsFile("digitdata/traininglabels", numTraining)

  loadImage()
  rawTestData = samples.loadDataFile("digitdata/testingimages",
                                     TEST_SET_SIZE,DIGIT_DATUM_WIDTH,
                                     DIGIT_DATUM_HEIGHT,'test', SP_CANVAS)
  testLabels = samples.loadLabelsFile("digitdata/testlabels", TEST_SET_SIZE)
  
  # Extract features

  print rawTestData
  trainingData = map(basicFeatureExtractorDigit, rawTrainingData)
  print "cp3"
  testData = map(basicFeatureExtractorDigit, rawTestData)

  
  # Conduct training and testing
  SP_CANVAS.create_text(LOG_X,LOG_Y, text= "Training...", anchor=NW, font=tkFont.Font(size=-14))
  LOG_Y += 15
  classifier.train(trainingData, trainingLabels,SP_CANVAS)
 # print "Validating..."
#  guesses = classifier.classify(validationData)
#  correct = [guesses[i] == validationLabels[i] for i in range(len(validationLabels))].count(True)
# print str(correct), ("correct out of " + str(len(validationLabels)) + " (%.1f%%).") % (100.0 * correct / len(validationLabels))

  SP_CANVAS.create_text(LOG_X,LOG_Y, text= "Testing...", anchor=NW, font=tkFont.Font(size=-14))
  LOG_Y += 15
  guesses = classifier.classify(testData,SP_CANVAS)
  correct = [guesses[i] == testLabels[i] for i in range(len(testLabels))].count(True)
  print str(correct), ("correct out of " + str(len(testLabels)) + " (%.1f%%).") % (100.0 * correct / len(testLabels))
  SP_CANVAS.create_text(LOG_X,LOG_Y+30, text= "Completed...", anchor=NW, font=tkFont.Font(size=-14))
  LOG_Y += 15
  SP_CANVAS.create_rectangle(200,300, 201, 301)
  
  the_input = raw_input('TYPE HERE:>> ')
  if match('bye',the_input):
    return
  
if __name__ == "__main__":
  runClassifier()

  
