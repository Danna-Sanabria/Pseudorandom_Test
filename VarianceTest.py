import numpy as np
from scipy.stats import chi2

class VarianceTest:
    def __init__(self, acceptance_lvl=0.05):
        self.acceptance_lvl = acceptance_lvl

    """"Main method to make test"""
    def evaluate(self, data):
        numberSample = len(data) # number of samples
        r = np.mean(data) # get mean of data
        self.var = np.var(data) # σ^2 -> get variance of data
        p1 = self.acceptance_lvl/2 #( α /2 )
        p2 = 1-(self.acceptance_lvl/2) #1 - ( α /2 )
        self.x1 =chi2.isf(p1,numberSample-1) #𝑿_(𝜶/𝟐)^𝟐
        self.x2 = chi2.isf(p2, numberSample-1) #𝑿_(𝟏−(𝜶/𝟐))^𝟐
        self.li = self.x1/(12*(numberSample-1)) #lower bounumberSampled
        self.ls = self.x2/(12*(numberSample-1)) #Higher bounumberSampled
        return self.li,self.ls, self.var
    
    
    """Evaluate if variance of data is between li and ls, if it is, it passes the test"""
    def valid(self):
        return self.ls<self.var<self.li
    
    
