
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




  






def runClassifier():
  global TK_ROOT, SP_CANVAS, LOG_X, LOG_Y
 
  # Set up variables according to the command line inputs  
  featureFunction = basicFeatureExtractorDigit
  
  legalLabels = range(10)		# number of labels

  # Select classifier
  classifier = perceptron.PerceptronClassifier(legalLabels)
      
  # Load data  
  numTraining = 1

  loadImage()

  
  rawTrainingData = samples.loadDataFile("digitdata/trainingimages",
                                         numTraining,DIGIT_DATUM_WIDTH,
                                         DIGIT_DATUM_HEIGHT,'train',SP_CANVAS)

  trainingLabels = samples.loadLabelsFile("digitdata/traininglabels", numTraining)

  
  rawTestData = samples.loadDataFile("digitdata/testingimages",
                                     TEST_SET_SIZE,DIGIT_DATUM_WIDTH,
                                     DIGIT_DATUM_HEIGHT,'test', SP_CANVAS)
  testLabels = samples.loadLabelsFile("digitdata/testlabels", TEST_SET_SIZE)
  
  # Extract features

  print rawTestData
  trainingData = map(basicFeatureExtractorDigit, rawTrainingData)
  print "cp3"
  testData = map(basicFeatureExtractorDigit, rawTestData)

  
  # Conduct auto training
  SP_CANVAS.create_text(LOG_X,LOG_Y, text= "Auto Training...", anchor=NW, font=tkFont.Font(size=-14))
  LOG_Y += 15
  classifier.train(trainingData, trainingLabels,SP_CANVAS)

  # Auto Testing
 # print "Validating..."
#  guesses = classifier.classify(validationData)
#  correct = [guesses[i] == validationLabels[i] for i in range(len(validationLabels))].count(True)
# print str(correct), ("correct out of " + str(len(validationLabels)) + " (%.1f%%).") % (100.0 * correct / len(validationLabels))

  # User Input Testing
  SP_CANVAS.create_text(LOG_X,LOG_Y, text= "Recognizing...", anchor=NW, font=tkFont.Font(size=-14))
  LOG_Y += 15
  guesses = classifier.classify(testData,SP_CANVAS,"usr")
  
  # Completion Notify
  SP_CANVAS.create_text(LOG_X,LOG_Y+30, text= "Completed...", anchor=NW, font=tkFont.Font(size=-14))
  LOG_Y += 15

  

  
if __name__ == "__main__":
  runClassifier()

  
