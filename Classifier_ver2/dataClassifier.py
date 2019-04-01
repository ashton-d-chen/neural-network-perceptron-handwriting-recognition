import perceptron
import samples
import sys
import util

TEST_SET_SIZE = 100
DIGIT_DATUM_WIDTH=28
DIGIT_DATUM_HEIGHT=28
FACE_DATUM_WIDTH=60
FACE_DATUM_HEIGHT=70

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
  



def runClassifier():
  
  # Set up variables according to the command line inputs  
  featureFunction = basicFeatureExtractorDigit
  
  legalLabels = range(10)		# number of labels

  # Select classifier
  classifier = perceptron.PerceptronClassifier(legalLabels)
      
  # Load data  
  numTraining = 100


  rawTrainingData = samples.loadDataFile("digitdata/trainingimages", numTraining,DIGIT_DATUM_WIDTH,DIGIT_DATUM_HEIGHT)
  trainingLabels = samples.loadLabelsFile("digitdata/traininglabels", numTraining)
  rawValidationData = samples.loadDataFile("digitdata/validationimages", TEST_SET_SIZE,DIGIT_DATUM_WIDTH,DIGIT_DATUM_HEIGHT)
  validationLabels = samples.loadLabelsFile("digitdata/validationlabels", TEST_SET_SIZE)
  rawTestData = samples.loadDataFile("digitdata/testimages", TEST_SET_SIZE,DIGIT_DATUM_WIDTH,DIGIT_DATUM_HEIGHT)
  testLabels = samples.loadLabelsFile("digitdata/testlabels", TEST_SET_SIZE)
    
  
  # Extract features
  trainingData = map(basicFeatureExtractorDigit, rawTrainingData)
  validationData = map(basicFeatureExtractorDigit, rawValidationData)
  testData = map(basicFeatureExtractorDigit, rawTestData)
  
  # Conduct training and testing
  print "Training..."
  classifier.train(trainingData, trainingLabels, validationData, validationLabels)
 # print "Validating..."
#  guesses = classifier.classify(validationData)
#  correct = [guesses[i] == validationLabels[i] for i in range(len(validationLabels))].count(True)
# print str(correct), ("correct out of " + str(len(validationLabels)) + " (%.1f%%).") % (100.0 * correct / len(validationLabels))

  print "Testing..."
  guesses = classifier.classify(testData)
  correct = [guesses[i] == testLabels[i] for i in range(len(testLabels))].count(True)
  print str(correct), ("correct out of " + str(len(testLabels)) + " (%.1f%%).") % (100.0 * correct / len(testLabels))
  util.pause()
  analysis(classifier, guesses, testLabels, rawTestData)  

if __name__ == "__main__":
  runClassifier()
