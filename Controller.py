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

        borde_color = "#00FF00" if is_true else "#FF0000"
        self.fr.meanTest_button.config(foreground =borde_color)  

        self.fr.generateLbl(f"Limite Superior: {ls}", 390, 471)
        self.fr.generateLbl(f"Media: {m}", 390, 509)
        self.fr.generateLbl(f"Limite Inferior: {li}", 390, 547)
        self.drawMeanFigure(li,ls,m,"Limite Superior", "Media", "Limite Inferior" ) 

    def varianceTest(self):
        data =self.read_data_from_file(self.fr.getFilePath())
        self.fr.destroyAlllbls() 
        li,ls,var = self.varTest.evaluate(data)

        if self.varTest.valid():
            is_true = True
        else:
            is_true = False
        borde_color = "#00FF00" if is_true else "#FF0000"
        self.fr.VarianceTest.config(foreground =borde_color) 

        self.fr.generateLbl(f"Limite Superior: {ls}", 390, 471)
        self.fr.generateLbl(f"Varianza de la Muestra: {var}", 390, 509)
        self.fr.generateLbl(f"Limite Inferior: {li}", 390, 547) 
        self.drawMeanFigure(li,ls,var,"Limite Superior","Varianza de la Muestra", "Limite Inferior") 

    def KSTest(self):
        data =self.read_data_from_file(self.fr.getFilePath())
        self.fr.destroyAlllbls() # Destroy previous labels
        
        dif, max_dif_per =self.ks.evaluarKS(data) # Evaluate
        
        self.fr.generateLbl(f"Diferencia Máxima: {dif:.5f}", 390, 471)
        self.fr.generateLbl(f"Diferencia Máxima Permitida: {max_dif_per}", 390, 509)

        if self.ks.validate():
            is_true = True
        else:
            is_true = False
        borde_color = "#00FF00" if is_true else "#FF0000"
        self.fr.KSTest.config(foreground =borde_color)

        self.drawKSFigure() #Finally paint the graphic
    
    def Chi2Test(self):
        data =self.read_data_from_file(self.fr.getFilePath())
        self.fr.destroyAlllbls() # Destroy previous labels
        chi2_total, valor_critico, intervalos, frec_observada, frec_esperada = self.chi2.chi_cuadrado_test(data)

        if self.chi2.validate():
            is_true = True
        else:
            is_true = False
        borde_color = "#00FF00" if is_true else "#FF0000"
        self.fr.Chi2Test.config(foreground =borde_color)

        self.fr.generateLbl(f"Chi2: {chi2_total}",290, 463)
        self.fr.generateLbl(f"Valor Crítico: {valor_critico}",290, 491)
        self.drawChi2Figure(data, intervalos, frec_observada, frec_esperada) #Finally paint the graphic

    def PokerTest(self):
        data =self.read_data_from_file(self.fr.getFilePath())
        self.fr.destroyAlllbls() # Destroy previous labels  
        statistics, counts, value,n, Oi,Ei = self.poker.evaluate(data)
        self.fr.generateLbl(f"Número de muestras: {n}", 290, 463)
        self.fr.generateLbl(f"Sumatoria: {value}", 290, 491)
        self.fr.generateLbl(f"Poker : {counts}", 290, 519)
        self.fr.generateLbl(f"Máximo Error Permitido: {statistics}", 290, 547)
        self.fr.generateLbl(f"D: Todos Diferentes", 811, 713)
        self.fr.generateLbl(f"O: Un par", 811, 733)
        self.fr.generateLbl(f"T: Dos pares", 811, 753)
        self.fr.generateLbl(f"K: Tercia ", 811, 773)
        self.fr.generateLbl(f"F: Tercia & par", 811, 793)
        self.fr.generateLbl(f"P: Cuatro cartas del mismo valor", 811, 813)
        self.fr.generateLbl(f"Q: Cinco cartas del mismo valor", 811, 833)

        if self.poker.validate():
            is_true = True
        else:
            is_true = False
        borde_color = "#00FF00" if is_true else "#FF0000"
        self.fr.PokerTest.config(foreground =borde_color)

        self.drawPokerFigure(data,Oi,Ei) #Finally paint the graphic

    def drawMeanFigure(self,li,ls,m, name1, name2, name3):
        self.fig = plt.figure(figsize=(7, 3), dpi=120)
        ax = self.fig.add_subplot(111)
        names = [name1, name2, name3]
        values = [ls, m, li]
        bars = ax.bar(names, values, alpha=0.3)
        for bar, value in zip(bars, values):
            ax.text(bar.get_x() + bar.get_width() / 2, 
                    value,
                    '%.5f' % value,
                    ha='center', va='bottom')

        ax.set_ylim(0, 1)  # Establece el rango del eje vertical
        ax.set_title("Resultado Prueba de Medias")
        ax.grid(True)  # Añade cuadrícula al gráfico
        colors = ['#1B9CFC', '#F97F51', '#82589F']
        for bar, color in zip(bars, colors):
            bar.set_color(color)
        
        self.canvas.get_tk_widget().pack_forget()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.fr.mywindow)
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM)
        self.canvas.draw()
        self.fr.mywindow.update()
    
    def drawKSFigure(self):
        self.fig.clear()
        self.fig = plt.figure(figsize=(7, 4), dpi=100)
        ax = self.fig.add_subplot(111)

        intervalos = [(i / 10, (i + 1) / 10) for i in range(10)]
        interval_labels = [f"{inicio:.1f}-{fin:.1f}" for inicio, fin in intervalos]

        bar_width = 0.35 
        index = np.arange(len(self.ks.calcular_probabilidad_esperada()))
        ax.bar(index - bar_width/2, self.ks.calcular_probabilidad_obtenida(), bar_width, alpha=0.5, color='#22a6b3', label='Frecuencia Observada')
        ax.bar(index + bar_width/2, self.ks.calcular_probabilidad_esperada(), bar_width, alpha=0.5, color='#be2edd', label='Frecuencia Esperada')
        
        ax.set_xlabel('Intervalo')
        ax.tick_params(axis='x', rotation=45)
        ax.set_ylabel('Probabilidades')
        ax.set_title('Probabilidad Esperada vs Probabilidad Observada por Intervalo')
        ax.set_xticks(index)
        ax.set_xticklabels(interval_labels)
        ax.legend()
        ax.grid(True)

        self.fig.subplots_adjust(bottom=0.39)
        self.canvas.get_tk_widget().pack_forget()
        self.canvas = FigureCanvasTkAgg(self.fig, master= self.fr.mywindow)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM)
        self.fr.mywindow.update()
    
    def drawChi2Figure(self,data, intervalos, frec_observada, frec_esperada):
        self.fig.clear()
        self.fig = plt.figure(figsize=(7, 4), dpi=100)
        ax = self.fig.add_subplot(111)
        k = len(intervalos) - 1
        interval_labels = [f"{intervalos[i]:.4g}-{intervalos[i+1]:.4g}" for i in range(k)]
        bar_width = 0.35 
        index = np.arange(k)
        ax.bar(index, frec_observada, bar_width, alpha=0.5, color='#009432', label='Frecuencia Observada')
        ax.bar(index + bar_width, frec_esperada, bar_width, alpha=0.5, color='#EE5A24', label='Frecuencia Esperada')
        ax.set_xlabel('Intervalo')
        ax.tick_params(axis='x', rotation=45)
        ax.set_ylabel('Frecuencia')
        ax.set_title('Frecuencia Esperada vs Frecuencia Observada por Intervalo')
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(interval_labels)
        ax.legend()
        ax.grid(True)
        self.fig.subplots_adjust(bottom=0.39)
        self.canvas.get_tk_widget().pack_forget()
        self.canvas = FigureCanvasTkAgg(self.fig, master= self.fr.mywindow)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM)
        self.fr.mywindow.update()

    def drawPokerFigure(self,data, Oi,Ei):
        self.fig.clear()
        self.fig = plt.figure(figsize=(5, 3), dpi=100)
        ax = self.fig.add_subplot(111)
        tags = ["D","0","T","K","F","P","Q"] # tags for every hand of poker
        ax.set_title("Poker Test")
        colores = ['#D980FA', '#12CBC4', '#F0C180', '#EEBCD3', '#A5E7EF', '#EFE7B1', '#BAEFCE']
        ax.bar(tags, Oi, label="Frecuencia observada", color=colores)
        ax.plot(tags, Ei, label="Frecuencia esperada")
        ax.set_xlabel('Categoria')
        ax.set_ylabel('Frecuencia')
        ax.set_title('Frecuencia por Categoria')
        self.fig.subplots_adjust(bottom=0.39)
        self.canvas.get_tk_widget().pack_forget()
        self.canvas = FigureCanvasTkAgg(self.fig, master= self.fr.mywindow)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM)
        self.fr.mywindow.update()

if __name__ == "__main__":
    control = Controller()