import util
from Tkinter import *
import tkFont
import temp

class PerceptronClassifier:
  """
  Perceptron classifier.
  """
  def __init__( self):
    self.type = "perceptron"
    self.weights = {}
    for label in temp.LEGAL_LABELS:
      self.weights[label] = util.Counter()

      # initialize weights
      for i in range(28):
        for j in range(28):
          self.weights[label][(i,j)] = 0
    
      
  def train( self, trainingData, trainingLabels, n, myList):
    """
    The training loop for the perceptron passes through the training data several
    times and updates the weight vector for each label based on classification errors.
    See the project description for details.
    """

      
    for iteration in range(n):
      myList.insertItem("Training iteration " + str(iteration) + ".")
      guess = []
      for i in range(len(trainingData)): # there are 100 data in each training set
        test = 0
        vectors = util.Counter()
        for l in temp.LEGAL_LABELS: # test with 10 legal labels
          vectors[l] = self.weights[l] * trainingData[i]
          if len(self.weights[l]) == 0:
            test = 0
          else:
            test = 1
          
        if test == 0 or vectors.argMax() != trainingLabels[i]:
          posTrainData = trainingData[i]
          negTrainData = trainingData[i]

          for j in trainingData[i]:
            if trainingData[i][j] > 0:
              posTrainData[j] = (temp.POS_WEIGHT)*trainingData[i][j]
              negTrainData[j] = (temp.NEG_WEIGHT)*trainingData[i][j]
          self.weights[vectors.argMax()] -= negTrainData
          self.weights[trainingLabels[i]] += posTrainData

  def classify(self, data, tye):
    """
    Classifies each datum as the label that most closely matches the prototype vector
    for that label.  See the project description for details.
    """
    guesses = []
    for datum in data:
      vectors = util.Counter()
      for l in temp.LEGAL_LABELS:
        vectors[l] = self.weights[l] * datum
      guesses.append(vectors.argMax())
           
    return guesses
