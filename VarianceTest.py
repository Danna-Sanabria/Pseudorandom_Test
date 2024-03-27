import numpy as np
from scipy.stats import chi2

class VarianceTest:
    def __init__(self, acceptance_lvl=0.05):
        """Initialize the VarianceTest object.

        Args:
            acceptance_lvl (float, optional): Acceptance level for the test. Defaults to 0.05.
        """
        self.acceptance_lvl = acceptance_lvl


    def evaluate(self, data):
        """Evaluate the variance test on the given data.

        Args:
            data (array-like): Sequence of data points.

        Returns:
            tuple: A tuple containing the lower bound, upper bound, and variance.
        """
        numberSample = len(data) # number of samples
        r = np.mean(data) # get mean of data
        self.var = np.var(data) # σ^2 -> Calculate the variance of the data
        p1 = self.acceptance_lvl/2 #( α /2 )
        p2 = 1-(self.acceptance_lvl/2) #1 - ( α /2 )
        self.x1 =chi2.isf(p1,numberSample-1) #𝑿_(𝜶/𝟐)^𝟐
        self.x2 = chi2.isf(p2, numberSample-1) #𝑿_(𝟏−(𝜶/𝟐))^𝟐
        self.li = self.x1/(12*(numberSample-1)) #Lower bound
        self.ls = self.x2/(12*(numberSample-1)) #Higher bound
        return self.li,self.ls, self.var
    
    
    """Evaluate if variance of data is between li and ls, if it is, it passes the test"""
    def valid(self):
        return self.ls<self.var<self.li
    
    
