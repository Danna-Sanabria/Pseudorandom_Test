import numpy as np
from scipy.stats import norm

class MeanTest:
    def __init__(self, acceptance_lvl=0.05):
        """
        Constructor of the MeanTest class.

        Parameters:
        acceptance_lvl (float): Acceptance level for the hypothesis test. Default is 0.05.
        """
        self.acceptance_lvl = acceptance_lvl

    def calculateMedia(self, data):
        """
        Calculate the mean of the provided data.

        Parameters:
        data (list or array-like): Data for which mean is calculated.

        Returns:
        float: The mean of the data.
        """
        self.suma = sum(data)
        self.promedio = self.suma / len(data)
        return self.promedio 
    
    def evaluate(self, data):
        """
        Perform hypothesis testing for the population mean.

        Parameters:
        data (list or array-like): Sample data.

        Returns:
        tuple: A tuple with lower and upper confidence bounds, and the sample mean.
        """
        self.n = len(data) # number of samples
        self.m = np.mean(data)  # get the mean of data
        self.v = np.std(data) # get the standard deviation
        pb_acum = 1-(self.acceptance_lvl/2)
        z = norm.ppf(pb_acum)
        self.li = (1/2) - z * (1/ np.sqrt(12 * self.n)) # Lower bound calculation
        self.ls = (1/2) + z * (1/ np.sqrt(12 * self.n)) # Higher bound calculation
        return self.li, self.ls, self.m
    
    def defineResult(self, li, ls, m):
        """
        Define the result of the hypothesis test.

        Parameters:
        li (float): Lower bound.
        ls (float): Upper bound.
        m (float): Sample mean.

        Returns:
        bool: True if the sample mean is within the confidence bounds, False otherwise.
        """
        if self.m <= ls and self.m >= li:
            return True
        else:
            return False
