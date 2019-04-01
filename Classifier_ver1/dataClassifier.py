 # This file contains feature extraction methods and harness 
# code for data classification

import mostFrequent
import naiveBayes
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

def basicFeatureExtractorFace(datum):
  """
  Returns a set of pixel features indicating whether
  each pixel in the provided datum is black, gray, or white.
  """
  a = datum.getPixels()

  features = util.Counter()
  for x in range(FACE_DATUM_WIDTH):
    for y in range(FACE_DATUM_HEIGHT):
      if datum.getPixel(x, y) > 0:
        features[(x,y)] = 1
      else:
        features[(x,y)] = 0
  return features

def enhancedFeatureExtractorDigit(datum):
  """
  Your feature extraction playground.
  """
  return basicFeatureExtractorDigit(datum)

def enhancedFeatureExtractorFace(datum):
  """
  Your feature extraction playground.
  """
  return basicFeatureExtractorFace(datum)


def analysis(classifier, guesses, testLabels, testData):
  """
  An analysis function.
  """

def printImage(pixels,width,height):
  """
  Generates a Datum object that contains all pixels in the 
  provided list of pixels.  This will serve as a helper function
  to the analysis function you write.
  
  Pixels should take the form 
  [(2,2), (2, 3), ...] 
  where each double represents a pixel.
  """
  image = samples.Datum(None,width,height)
  for x, y in pixels:
    image.pixels[x][y] = 2
  print image  
  
# Main harness code

def runClassifier():
  """
  Harness code for running different classifiers on the face or digit data.
  
  This is the main function for classification, and is designed
  to be invoked from the command line (outside the Python interpreter).
  
  Usage:
    > python dataClassifier.py 
    OR
    > python dataClassifier.py <data> <classifierName>
    OR
    > python dataClassifier.py <data> <classifierName> <featureFunction>
    OR
    > python dataClassifier.py <data> <classifierName> <featureFunction> <numTrainingExamples>
    OR
    > python dataClassifier.py <data> <classifierName> <featureFunction> <numTrainingExamples> <odds class1 class2>
    
  For example:
    > python dataClassifier.py digits naivebayes basic 1000
    
  would run the naive Bayes classifier on 1000 training examples using the
  basicFeatureExtractor function, and then test the classifier on the test data.
  """
  print "Doing classification"
  print "--------------------"
  # Assign default values for arguments if they are not provided.
  if(len(sys.argv) == 1):
    print "No data specified; using digits."
    sys.argv.append("digits")
  if(len(sys.argv) == 2):
    print "No classifier specified; using default."
    sys.argv.append("perceptron")
  if(len(sys.argv) == 3):
    print "No feature extraction function specified; using default."
    sys.argv.append("basic")
  if(len(sys.argv) == 4):
    print "No training set size specified; using default."
    sys.argv.append("100")
  if(len(sys.argv) == 5):
    print "Not doing odds ratio computation."
    sys.argv.append("noodds")
  
  # Set up variables according to the command line input.
  print "data:\t\t" + sys.argv[1]
  print "classifier:\t\t" + sys.argv[2]
  print "feature extractor:\t" + sys.argv[3]
  print "training set size:\t" + sys.argv[4]
  if((sys.argv[1]=="digits") & (sys.argv[3] == "basic")):
    featureFunction = basicFeatureExtractorDigit
  elif((sys.argv[1]=="faces") & (sys.argv[3] == "basic")):
    featureFunction = basicFeatureExtractorFace
  elif((sys.argv[1]=="digits") & (sys.argv[3] == "enhanced")):
    featureFunction = enhancedFeatureExtractorDigit
  elif((sys.argv[1]=="faces") & (sys.argv[3] == "enhanced")):
    featureFunction = enhancedFeatureExtractorFace
  else:
    print "Unknown feature function:", sys.argv[2]
    return

  if(sys.argv[1]=="digits"):	# if digits detect
    legalLabels = range(10)		# number of labels
  else:							# if face detect
    legalLabels = range(2)

  # Select classifier
  if(sys.argv[2] == "mostfrequent"):
    classifier = mostFrequent.MostFrequentClassifier(legalLabels)
  elif(sys.argv[2] == "naivebayes"):
    classifier = naiveBayes.NaiveBayesClassifier(legalLabels)
  elif(sys.argv[2] == "perceptron"):
    classifier = perceptron.PerceptronClassifier(legalLabels)
  else:
    print "Unknown classifier:", sys.argv[2]
    return
      
  # Load data  
  numTraining = int(sys.argv[4])

  if(sys.argv[1]=="faces"):
    rawTrainingData = samples.loadDataFile("facedata/facedatatrain", numTraining,FACE_DATUM_WIDTH,FACE_DATUM_HEIGHT)
    trainingLabels = samples.loadLabelsFile("facedata/facedatatrainlabels", numTraining)
    rawValidationData = samples.loadDataFile("facedata/facedatatrain", TEST_SET_SIZE,FACE_DATUM_WIDTH,FACE_DATUM_HEIGHT)
    validationLabels = samples.loadLabelsFile("facedata/facedatatrainlabels", TEST_SET_SIZE)
    rawTestData = samples.loadDataFile("facedata/facedatatest", TEST_SET_SIZE,FACE_DATUM_WIDTH,FACE_DATUM_HEIGHT)
    testLabels = samples.loadLabelsFile("facedata/facedatatestlabels", TEST_SET_SIZE)
  else:
    rawTrainingData = samples.loadDataFile("digitdata/trainingimages", numTraining,DIGIT_DATUM_WIDTH,DIGIT_DATUM_HEIGHT)
    trainingLabels = samples.loadLabelsFile("digitdata/traininglabels", numTraining)
    rawValidationData = samples.loadDataFile("digitdata/validationimages", TEST_SET_SIZE,DIGIT_DATUM_WIDTH,DIGIT_DATUM_HEIGHT)
    validationLabels = samples.loadLabelsFile("digitdata/validationlabels", TEST_SET_SIZE)
    rawTestData = samples.loadDataFile("digitdata/testimages", TEST_SET_SIZE,DIGIT_DATUM_WIDTH,DIGIT_DATUM_HEIGHT)
    testLabels = samples.loadLabelsFile("digitdata/testlabels", TEST_SET_SIZE)
    
  
  # Extract features
  print "Extracting features..."
  trainingData = map(featureFunction, rawTrainingData)
  validationData = map(featureFunction, rawValidationData)
  testData = map(featureFunction, rawTestData)
  
  # Conduct training and testing
  print "Training..."
  classifier.train(trainingData, trainingLabels, validationData, validationLabels)
  print "Validating..."
  guesses = classifier.classify(validationData)
  correct = [guesses[i] == validationLabels[i] for i in range(len(validationLabels))].count(True)
  print str(correct), ("correct out of " + str(len(validationLabels)) + " (%.1f%%).") % (100.0 * correct / len(validationLabels))

  print "Testing..."
  guesses = classifier.classify(testData)
  correct = [guesses[i] == testLabels[i] for i in range(len(testLabels))].count(True)
  print str(correct), ("correct out of " + str(len(testLabels)) + " (%.1f%%).") % (100.0 * correct / len(testLabels))
  util.pause()
  analysis(classifier, guesses, testLabels, rawTestData)
  
  # do odds ratio computation if specified at command line
  if((sys.argv[5] == "odds") & (len(sys.argv)==8)):
    features_class1,features_class2,features_odds = classifier.findHighOddsFeatures(int(sys.argv[6]),int(sys.argv[7]))
    if (sys.argv[1]=="faces"):
      printImage(features_class1,FACE_DATUM_WIDTH,FACE_DATUM_HEIGHT)
      printImage(features_class2,FACE_DATUM_WIDTH,FACE_DATUM_HEIGHT)
      printImage(features_odds,FACE_DATUM_WIDTH,FACE_DATUM_HEIGHT)
    else:
      printImage(features_class1,DIGIT_DATUM_WIDTH,DIGIT_DATUM_HEIGHT)
      printImage(features_class2,DIGIT_DATUM_WIDTH,DIGIT_DATUM_HEIGHT)
      printImage(features_odds,DIGIT_DATUM_WIDTH,DIGIT_DATUM_HEIGHT)

if __name__ == "__main__":
  runClassifier()
