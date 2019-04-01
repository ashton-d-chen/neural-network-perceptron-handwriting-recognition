import util
from Tkinter import *
import tkFont
import variable

class PerceptronClassifier:
  """
  Perceptron classifier.
  """
  def __init__( self):
    self.type = "perceptron"
    self.weights = {}
    for label in variable.LEGAL_LABELS:
      self.weights[label] = util.Counter()
      
  def train( self, trainingData, trainingLabels, myList):
    """
    The training loop for the perceptron passes through the training data several
    times and updates the weight vector for each label based on classification errors.
    See the project description for details.
    """

      
    for iteration in range(variable.AUTO_ITERATIONS):
      print "iteration = ", iteration
      myList.insertItem("Training iteration " + str(iteration) + ".")
    #  print ("Training iteration " + str(iteration) + ".")

      guess = []
      for i in range(len(trainingData)): # there are 100 data in each training set
        vectors = util.Counter()
        for l in variable.LEGAL_LABELS: # test with 10 legal labels
          #print l
          #print self.weights[l]
          vectors[l] = self.weights[l] * trainingData[i]
          
        if vectors.argMax() != trainingLabels[i]:

          posTrainData = trainingData[i]
          negTrainData = trainingData[i]

          for j in trainingData[i]:
            if trainingData[i][j] > 0:
              posTrainData[j] = (variable.POS_WEIGHT)*trainingData[i][j]
              negTrainData[j] = (variable.NEG_WEIGHT)*trainingData[i][j]

          self.weights[vectors.argMax()] -= negTrainData
          self.weights[trainingLabels[i]] += posTrainData
          #print "leagal labels", self.variable.LEGAL_LABELS

  def classify(self, data, tye):
    """
    Classifies each datum as the label that most closely matches the prototype vector
    for that label.  See the project description for details.
    """
    guesses = []
    for datum in data:
      vectors = util.Counter()
      for l in variable.LEGAL_LABELS:
        vectors[l] = self.weights[l] * datum
      guesses.append(vectors.argMax())
           
    return guesses
