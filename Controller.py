from Frame import Frame
from KSTest import KSTest
from MeanTest import MeanTest
from VarianceTest import VarianceTest
from Chi2Test import Chi2Test
from PokerTest import PokerTest
import pandas as pd
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from scipy.stats import *
from statsmodels.distributions.empirical_distribution import ECDF
import tkinter as tk

class Controller:
    def __init__(self):
        self.fr = Frame(self)
        self.meanTest = MeanTest()
        self.varTest = VarianceTest()
        self.chi2 = Chi2Test()
        self.ks = KSTest()
        self.poker = PokerTest()
        self.fig = plt.figure(figsize=(5, 5),dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master= self.fr.mywindow)
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM)
        self.fr.mywindow.mainloop()

    """It grabs the data from the given file path""" 
    def read_data_from_file(self, filename):
        if filename.endswith('.csv'):
            df = pd.read_csv(filename, header=None, decimal=',', delimiter=';')
        elif filename.endswith('.xlsx') or filename.endswith('.xls'):
            df = pd.read_excel(filename, header=None, decimal=',')
        else:
            raise ValueError("Formato de archivo no compatible. Proporcione un archivo CSV o Excel.")

        data = df.values.flatten().tolist()
        return data

    def meanTest(self):
        data = self.read_data_from_file(self.fr.getFilePath())
        self.fr.destroyAlllbls() 

        li,ls,m = self.meanTest.evaluate(data)

        if self.meanTest.defineResult(li, ls, m):
            is_true = True
        else:
            is_true = False

        test = tk.Label(text="TEST", font=("Georgia", 12))
        test.place(x=484, y=431)

        self.changeLabelColor(test, is_true)

        self.fr.generateLbl(f"Limite Superior: {ls}", 390, 471)
        self.fr.generateLbl(f"Media: {m}", 390, 509)
        self.fr.generateLbl(f"Limite Inferior: {li}", 390, 547)

        self.drawMeanFigure(li,ls,m,"Limite Superior", "Media", "Limite Inferior" ) 
    
    def changeLabelColor(self, label, is_true):
        if is_true:
            color = "#00FF00"  
        else:
            color = "#FF0000"  
        label.config(bg=color)

    def varianceTest(self):
        data =self.read_data_from_file(self.fr.getFilePath())
        self.fr.destroyAlllbls() 
        li,ls,var = self.varTest.evaluate(data)
        self.fr.generateLbl(f"Limite Superior: {ls}", 390, 471)
        self.fr.generateLbl(f"Varianza de la Muestra: {var}", 390, 509)
        self.fr.generateLbl(f"Limite Inferior: {li}", 390, 547) 
        self.drawMeanFigure(li,ls,var,"Limite Superior","Varianza de la Muestra", "Limite Inferior") 

    def KSTest(self):
        data =self.read_data_from_file(self.fr.getFilePath())
        self.fr.destroyAlllbls() # Destroy previous labels
        # self.fr.generateLbl("KS TEST")
        #Make the test
        # dif, ksvalue=self.ks.evaluate(data) # Evaluate
        results = KSTest.calculate_differences(self, data)
        print( results['max_diff_normal'])
        print( results['diff_normal'])
        print( results['max_diff_poisson'])
        #Shows information
        # self.fr.generateLbl(f"Number of samples: {n}")
        # self.fr.generateLbl(f"Passed test: {valid}")
        # self.fr.generateLbl("Max Difference: %.5f %%" % dif, 390, 471)
        # self.fr.generateLbl(f"KSValue associated: {ksvalue}", 390, 509)

        # self.drawKSFigure(data) #Finally paint the graphic
    
    def Chi2Test(self):
        data =self.read_data_from_file(self.fr.getFilePath())
        self.fr.destroyAlllbls() # Destroy previous labels
        # self.fr.generateLbl("CHI2 TEST")
        #Make the test
        statistic, chi_value, obs_freq, expect_freq, bin_edges, status_hypo,n =self.chi2.evaluate(data)
        #Shows information
        # self.fr.generateLbl(f"Number of samples: {n}")
        # self.fr.generateLbl(f"Status: {status_hypo}")
        # self.fr.generateLbl(f"Observed frequency: {obs_freq}")
        # self.fr.generateLbl(f"Expected frequency: {expect_freq}")
        # self.fr.generateLbl(f"Obtained Value: {statistic}")
        # self.fr.generateLbl(f"Chi2Value Associated: {chi_value}")
        self.drawChi2Figure(data) #Finally paint the graphic

    def PokerTest(self):
        data =self.read_data_from_file(self.fr.getFilePath())
        self.fr.destroyAlllbls() # Destroy previous labels
        # self.fr.generateLbl("POKER TEST")
        #Make the test
        statistics, counts, value,n, Oi,Ei=self.poker.evaluate(data)
        #Shows information
        # self.fr.generateLbl(f"Number of samples: {n}")
        # self.fr.generateLbl(f"Obtained Value: {value}")
        # self.fr.generateLbl(f"Poker counts: {counts}")
        # self.fr.generateLbl(f"PokerValue Associated: {statistics}")
        self.drawPokerFigure(data,Oi,Ei) #Finally paint the graphic

    def drawMeanFigure(self,li,ls,m, name1, name2, name3):
        self.fig = plt.figure(figsize=(7, 3), dpi=120)
        ax = self.fig.add_subplot(111)
        
        # Define los nombres y valores para las barras
        names = [name1, name2, name3]
        values = [ls, m, li]

        # Crea las barras con los nombres y valores correspondientes
        bars = ax.bar(names, values, alpha=0.3)

        # Añade etiquetas debajo de cada barra
        for bar, value in zip(bars, values):
            ax.text(bar.get_x() + bar.get_width() / 2, 
                    value,
                    '%.5f' % value,
                    ha='center', va='bottom')

        ax.set_ylim(0, 1)  # Establece el rango del eje vertical
        ax.set_title("Resultado Prueba de Medias")
        ax.grid(True)  # Añade cuadrícula al gráfico

        # Asigna un color diferente a cada barra
        colors = ['blue', 'green', 'red']
        for bar, color in zip(bars, colors):
            bar.set_color(color)
        
        # Actualiza el canvas
        self.canvas.get_tk_widget().pack_forget()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.fr.mywindow)
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM)
        self.canvas.draw()
        # Actualiza la ventana con la nueva figura
        self.fr.mywindow.update()
    
    def drawKSFigure(self,data):
        self.fig.clear()
        self.fig = plt.figure(figsize=(7, 4))
        ax = self.fig.add_subplot(111)
        mu, sigma= self.ks.getMeanAndStd(data)
        x = np.linspace(norm.ppf(0.01), norm.ppf(0.99), 100)
        # pdf = norm.pdf(x, mu, sigma)
        cdf = norm.cdf(x, mu, sigma)
        e_cdf = ECDF(data)
        ax.set_title("KS Test")
        ax.plot(e_cdf.x, e_cdf.y, label='Empirical CDF')
        ax.plot(x, cdf, label='Theoretical CDF')

        self.canvas.get_tk_widget().pack_forget()
        self.canvas = FigureCanvasTkAgg(self.fig, master= self.fr.mywindow)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM)
        # Update the window with the new figure
        self.fr.mywindow.update()
    
    def drawChi2Figure(self,data):
        self.fig.clear()
        self.fig = plt.figure(figsize=(5, 3), dpi=100)
        ax = self.fig.add_subplot(111)
        mu, sigma = self.chi2.getMeanAndStd(data)
        n_bins = int(1 + np.log2(len(data)))
        bins = np.histogram_bin_edges(data, bins=n_bins)
        # Calculate the observed frequencies
        observed, _ = np.histogram(data, bins=bins)

        # Calculate the expected frequencies using the normal distribution
        expected = len(data) * np.diff(norm.cdf(bins, mu, sigma))

        # Plot the histogram and compare the observed and expected frequencies
        ax.set_title("Chi2 Test")
        ax.hist(data, bins=bins, alpha=0.5, label='Observed') 
        ax.plot(bins[1:], expected, label='Expected')
        self.canvas.get_tk_widget().pack_forget()
        self.canvas = FigureCanvasTkAgg(self.fig, master= self.fr.mywindow)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM)
        # Update the window with the new figure
        self.fr.mywindow.update()

    def drawPokerFigure(self,data, Oi,Ei):
        self.fig.clear()
        self.fig = plt.figure(figsize=(5, 3), dpi=100)
        ax = self.fig.add_subplot(111)
        tags = ["D","0","T","K","F","P","Q"] # tags for every hand of poker
        ax.set_title("Poker Test")
        ax.bar(tags, Oi, label="Frecuencia observada")
        ax.plot(tags, Ei, label="Frecuencia esperada")
        self.canvas.get_tk_widget().pack_forget()
        self.canvas = FigureCanvasTkAgg(self.fig, master= self.fr.mywindow)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.RIGHT)
        # Update the window with the new figure
        self.fr.mywindow.update()

if __name__ == "__main__":
    control = Controller()