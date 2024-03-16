import numpy as np
from scipy.stats import chi2

class PokerTest:
    def __init__(self, acceptance_lvl=0.05):
        self.acceptance_lvl = acceptance_lvl
        self.Oi = [0, 0, 0, 0, 0, 0, 0]  # Observed freq
        self.prob = [0.30240, 0.50400, 0.10800, 0.07200, 0.00900, 0.00450, 0.00010]  # Theoretical prob for every hand

    """Main method to make test"""
    def evaluate(self, data):
        n = len(data)  # Number of samples
        for i in data:
            num = float("{:.5f}".format(i))  # Truncate and convert to float
            num_str = str(num).replace('0.', '')  # Remove leading 0 and dot
            self.tipo(num_str)  # Classify every number of data

        Ei = [prob * n for prob in self.prob]  # Expected frequencies

        
        finals = [((h - o) ** 2) / h for h, o in zip(Ei, self.Oi)]  # Calculate chi-square statistic
        counts = f"D: {self.Oi[0]}  O: {self.Oi[1]}  T: {self.Oi[2]}  K: {self.Oi[3]}  F: {self.Oi[4]}  P: {self.Oi[5]}  Q: {self.Oi[6]}"
        self.statistics = chi2.isf(0.05, 6)
        self.sumatoria = np.sum(finals)
        return self.statistics, counts, self.sumatoria, n, self.Oi, Ei
    
    def validate(self):
        return self.sumatoria <= self.statistics

    """Evaluate if the number has 5 same digits"""
    @staticmethod
    def flushQ(number):
        return len(set(number)) == 1

    """Evaluate if the number has 3 same digits and one pair same"""
    @staticmethod
    def fullHouseF(number):
        counts = {digit: number.count(digit) for digit in number}
        return 2 in counts.values() and 3 in counts.values()

    """Evaluate if the number has 4 same digits"""
    @staticmethod
    def pokerP(number):
        counts = {digit: number.count(digit) for digit in number}
        return any(count >= 4 for count in counts.values())

    """Evaluate if the number has 3 same digits"""
    @staticmethod
    def kindK(number):
        counts = {digit: number.count(digit) for digit in number}
        return any(count >= 3 for count in counts.values())

    """Evaluate if the number has 1 pair of same digits"""
    @staticmethod
    def onePairO(number):
        counts = {digit: number.count(digit) for digit in number}
        return any(count >= 2 for count in counts.values())

    """Evaluate if the number has 2 pair of same digits"""
    @staticmethod
    def twoPairsT(number):
        counts = {digit: number.count(digit) for digit in number}
        pair_count = 0
        for count in counts.values():
            if count >= 2:
                pair_count += 1
        return pair_count >= 2

    """Evaluate if all the digits are different"""
    @staticmethod
    def td(number):
        return len(number) == len(set(number))

    """Evaluate the number to count poker hands and save the amount result for every hand"""
    def tipo(self, number):
        if self.flushQ(number):
            self.Oi[6] += 1
        elif self.pokerP(number):
            self.Oi[5] += 1
        elif self.fullHouseF(number):
            self.Oi[4] += 1
        elif self.kindK(number):
            self.Oi[3] += 1
        elif self.twoPairsT(number):
            self.Oi[2] += 1
        elif self.onePairO(number):
            self.Oi[1] += 1
        else:
            self.Oi[0] += 1