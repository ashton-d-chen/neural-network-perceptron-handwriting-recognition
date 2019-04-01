# Perceptron implementation
import util
MAX_ITERATIONS=5

class PerceptronClassifier:
  """
  Perceptron classifier.
  """
  def __init__( self, legalLabels):
    self.legalLabels = legalLabels
    self.type = "perceptron"
    self.weights = {}
    for label in legalLabels:
      self.weights[label] = util.Counter()
      
  def train( self, trainingData, trainingLabels, validationData, validationLabels ):
    """
    The training loop for the perceptron passes through the training data several
    times and updates the weight vector for each label based on classification errors.
    See the project description for details.
    """
    for iteration in range(MAX_ITERATIONS):
      print "Starting iteration ", iteration, "..."
      for i in range(len(trainingData)):
        None # Your code here
    
  def classify(self, data ):
    """
    Classifies each datum as the label that most closely matches the prototype vector
    for that label.  See the project description for details.
    """
    guesses = []
    for datum in data:
      vectors = util.Counter()
      for l in self.legalLabels:
        vectors[l] = self.weights[l] * datum
      guesses.append(vectors.argMax())

    return guesses

  
  def findHighOddsFeatures(self, class1, class2):
    """
    Returns:
    features_class1 -- the 100 largest weight features 
    features_class2 -- the 100 largest weight features
    features_odds -- the 100 best features for difference in feature values
                     w_class1 - w_class2

    """

    features_class1 = util.Counter()
    features_class2 = util.Counter()
    features_odds = util.Counter()

    # Your code here

    return features_class1,features_class2,features_odds

