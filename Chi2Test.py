import numpy as np
from scipy.stats import chi2

class Chi2Test:
    def __init__(self, acceptance_lvl=0.05):
        self.acceptance_lvl = acceptance_lvl
        #Chi2 propability Table
        self.chi2table = np.array([
            [0.995, 0.99, 0.975, 0.95, 0.90, 0.10, 0.05, 0.025, 0.01, 0.005],
            [0000, 0000,  0.001, 0.004, 0.016, 2.706, 3.841, 5.024, 6.635, 7.879],   
            [0.010, 0.020, 0.051, 0.103, 0.211, 4.605, 5.991, 7.378, 9.210, 10.597],
            [0.072, 0.115, 0.216, 0.352, 0.584, 6.251, 7.815, 9.348, 11.345, 12.838],
            [0.207, 0.297, 0.484, 0.711, 1.064, 7.779, 9.488, 11.143, 13.277, 14.860],
            [0.412, 0.554, 0.831, 1.145, 1.610, 9.236, 11.070, 12.833, 15.086, 16.750],
            [0.676, 0.872, 1.237, 1.635, 2.204, 10.645, 12.592, 14.449, 16.812, 18.548],
            [0.989, 1.239, 1.690, 2.167, 2.833, 12.017, 14.067, 16.013, 18.475, 20.278],
            [1.344, 1.646, 2.180, 2.733, 3.490, 13.362, 15.507, 17.535, 20.090, 21.955],
            [1.735, 2.088, 2.700, 3.325, 4.168, 14.684, 16.919, 19.023, 21.666, 23.589],
            [2.156, 2.558, 3.247, 3.940, 4.865, 15.987, 18.307, 20.483, 23.209, 25.188],
            [2.603, 3.053, 3.816, 4.575, 5.578, 17.275, 19.675, 21.920, 24.725, 26.757],
            [3.074, 3.571, 4.404, 5.226, 6.304, 18.549, 21.026, 23.337, 26.217, 28.300],
            [3.565, 4.107, 5.009, 5.892, 7.042, 19.812, 22.362, 24.736, 27.688, 29.819],
            [4.075, 4.660, 5.629, 6.571, 7.790, 21.064, 23.685, 26.119, 29.141, 31.319],
            [4.601, 5.229, 6.262, 7.261, 8.547, 22.307, 24.996, 27.488, 30.578, 32.801],
            [5.142, 5.812, 6.908, 7.962, 9.312, 23.542, 26.296, 28.845, 32.000, 34.267],
            [5.697, 6.408, 7.564, 8.672, 10.085, 24.769, 27.587, 30.191, 33.409, 35.718],
            [6.265, 7.015, 8.231, 9.390, 10.865, 25.989, 28.869, 31.526, 34.805, 37.156],
            [6.844, 7.633, 8.907, 10.117, 11.651, 27.204, 30.144, 32.852, 36.191, 38.582],
            [7.434, 8.260, 9.591, 10.851, 12.443, 28.412, 31.410, 34.170, 37.566, 39.997],
            [8.034, 8.897, 10.283, 11.591, 13.240, 29.615, 32.671, 35.479, 38.932, 41.401],
            [8.643, 9.542, 10.982, 12.338, 14.041, 30.813, 33.924, 36.781, 40.289, 42.796],
            [9.260, 10.196, 11.689, 13.091, 14.848, 32.007, 35.172, 38.076, 41.638, 44.181],
            [9.886, 10.856, 12.401, 13.848, 15.659, 33.196, 36.415, 39.364, 42.980, 45.559],
            [10.520, 11.524, 13.120, 14.611, 16.473, 34.382, 37.652, 40.646, 44.314, 46.928],
            [11.160, 12.198, 13.844, 15.379, 17.292, 35.563, 38.885, 41.923, 45.642, 48.290],
            [11.808, 12.879, 14.573, 16.151, 18.114, 36.741, 40.113, 43.195, 46.963, 49.645],
            [12.461, 13.565, 15.308, 16.928, 18.939, 37.916, 41.337, 44.461, 48.278, 50.993],
            [13.121, 14.256, 16.047, 17.708, 19.768, 39.087, 42.557, 45.722, 49.588, 52.336],
            [13.787, 14.953, 16.791, 18.493, 20.599, 40.256, 43.773, 46.979, 50.892, 53.672],
            [20.707, 22.164, 24.433, 26.509, 29.051, 51.805, 55.758, 59.342, 63.691, 66.766],
            [27.991, 29.707, 32.357, 34.764, 37.689, 63.167, 67.505, 71.420, 76.154, 79.490],
            [35.534, 37.485, 40.482, 43.188, 46.459, 74.397, 79.082, 83.298, 88.379, 91.952],
            [43.275, 45.442, 48.758, 51.739, 55.329, 85.527, 90.531, 95.023, 100.425, 104.215],
            [51.172, 53.540, 57.153, 60.391, 64.278, 96.578, 101.879, 106.629, 112.329, 116.321],
            [59.196, 61.754, 65.647, 69.126, 73.291, 107.565, 113.145, 118.136, 124.116, 128.299],
            [67.328, 70.065, 74.222, 77.929, 82.358, 118.498, 124.342, 129.561, 135.807, 140.169]])
        
    """"Main method to make test"""
    def evaluate(self, data):
        n=len(data)
        bins=int(1+np.log2(n))
        hist, bin_edges = np.histogram(data, bins=bins)
        observed_freq = hist
        expected_freq = n/bins * np.ones(bins) #Calculates the expected frequency based on n samples and intervals
        chi2_statistic = sum((observed_freq - expected_freq)**2 / expected_freq) #To calculate the statistic
        chi2_critical_value = self.findKSValue(data)
        status_hypo=""
        if chi2_statistic > chi2_critical_value:
            status_hypo="Reject null hypothesis"
        else:
            status_hypo="Cannot reject null hypothesis"
        return chi2_statistic, chi2_critical_value, observed_freq, expected_freq, bin_edges, status_hypo,n
    
    """"Method to find the Chi2 value associated to the df and acceptance_lvl"""
    def findKSValue(self,data):
        n=len(data) #gets the number of samples
        bins=int(1+np.log2(n)) #gets the number of intervals
        return self.chi2table[bins-1,6] #looks for the value in the table
    
    """Gets Mean and Std values of the samples in the data"""
    def getMeanAndStd(self,data):
        return np.mean(data),np.std(data)

    def chi_cuadrado_test(self, data):
        # Número de intervalos
        k = 8

        # Calculamos la longitud de la secuencia
        n = len(data)

        # Creamos los intervalos
        intervalos = np.linspace(0, 1, k+1)

        # Contamos las frecuencias observadas en cada intervalo
        frec_observada, _ = np.histogram(data, bins=intervalos)

        # Calculamos la frecuencia esperada para cada intervalo
        frec_esperada = np.ones(k) * n / k

        # Calculamos el estadístico chi-cuadrado para cada intervalo
        chi2_intervalos = ((frec_observada - frec_esperada) ** 2) / frec_esperada

        # Sumamos los chi-cuadrado de todos los intervalos
        chi2_total = np.sum(chi2_intervalos)

        # Calculamos el valor crítico de chi-cuadrado con 7 grados de libertad
        valor_critico = chi2.ppf(0.95, k-1)

        print("intervalos: ", intervalos)
        print("F espe:" , frec_esperada)
        print("F Obser: ", frec_observada)
        print("Chi-cuadrado de cada intervalo:")
        print(chi2_intervalos)
        print("Chi-cuadrado total:", chi2_total)
        print("Valor crítico:", valor_critico)

        # Comparamos el chi-cuadrado total con el valor crítico
        if chi2_total <= valor_critico:
            print("La secuencia pasa la prueba de uniformidad.")
        else:
            print("La secuencia no pasa la prueba de uniformidad.")