import numpy as np
from scipy.stats import norm
class MeanTest:
    def __init__(self, acceptance_lvl=0.05):
        self.acceptance_lvl = acceptance_lvl

    def calculateMedia(self, data):
        self.suma = sum(data)
        self.promedio = self.suma / len(data)
        return self.promedio 
    
    """"Main method to make test"""
    def evaluate(self, data):
        self.n = len(data) # number of samples
        self.m = np.mean(data)  #get mean of data
        self.v = np.std(data) #get standard
        pb_acum = 1-(self.acceptance_lvl/2)
        z = norm.ppf(pb_acum)
        self.li = (1/2) - z * (1/ np.sqrt(12 * self.n)) #Lower bound calculation
        self.ls = (1/2) + z * (1/ np.sqrt(12 * self.n)) #Higher bound calculation
        return self.li, self.ls, self.m
    
    def defineResult(self, li, ls, m):
        if self.m <= ls and self.m >= li:
            return True
