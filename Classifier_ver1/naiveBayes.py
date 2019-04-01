import util
import classificationMethod
import math

class NaiveBayesClassifier(classificationMethod.ClassificationMethod):
  """
  The naive Bayes classifier is described in the textbook on page
  ...
  """
  def __init__(self, legalLabels):
    self.legalLabels = legalLabels
    self.type = "naivebayes"

  def train(self, trainingData, trainingLabels, validationData, validationLabels):
    """
    Train the classifier by collecting counts over the training data and using
    the validation data for smoothing.  See the project description for details.
    """
    # Your code here

    
  def classify(self, testData):
    """
    Classify the data based on the posterior distribution over labels.
    """
    guesses = []
    self.posteriors = [] # Posteriors are stored for later data analysis.
    for datum in testData:
      posterior = self.calculatePosteriorProbabilities(datum)
      guesses.append(posterior.argMax())
      self.posteriors.append(posterior)
    return guesses
      
  def calculatePosteriorProbabilities(self, datum):
    """
    Returns the posterior distribution over legal labels given the datum.
    Each probability should be stored in the posterior counter, e.g.
    
    posterior['spam'] = <Estimate of P(Label = 'spam' | datum)>
    """
    posterior = util.Counter()
    posterior["SomeLabel"] = -1e309 
    # Your code here
    return posterior
  
  def findHighOddsFeatures(self, class1, class2):
    """
    Returns: 
    features_class1 -- the 100 best features for P(feature=on|class1)
    features_class2 -- the 100 best features for P(feature=on|class2)
    features_odds -- the 100 best features for the odds ratio 
                     P(feature=on|class1)/P(feature=on|class2) 
    """

    featuresClass1 = util.Counter()
    featuresClass2 = util.Counter()
    featuresOdds = util.Counter()
    
    # Your code here

    return featuresClass1,featuresClass2,featuresOdds
    

    
      
