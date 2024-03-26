# PRUEBAS DE LOS NÚMEROS PSEUDOALEATORIOS

A continuación, encontrarás un conjunto de pruebas diseñadas para implementar secuencias de validación de números pseudoaleatorios. Estas pruebas incluirán gráficos que permitirán visualizar la uniformidad o distribución de los datos. Para realizar la prueba, deberás seleccionar un archivo CSV o Excel que contenga el conjunto de datos a evaluar.

## Prueba de Medias 

Esta prueba se basa en la hipótesis de que los números generados siguen una distribución uniforme entre 0 y 1. A continuacion podra evidenciar los pasos para realizar la prueba de medias:

1. Obtener la media. La media (o promedio) de los números se calcula sumando todos los números y dividiendo por la cantidad total de números. En notación matemática, esto se expresa como:


   ![image](https://github.com/Danna-Sanabria/Pseudorandom_Test/assets/83075069/9bd5608f-f91e-40a8-a944-7235ed264277)


    donde n es la cantidad total de números y ri​ es el i-ésimo número.

3. Obtener los límites inferior y superior. Estos límites se calculan utilizando la distribución normal estándar y un nivel de confianza predefinido (usualmente 95%). Los límites se calculan como:

    ![image](https://github.com/Danna-Sanabria/Pseudorandom_Test/assets/83075069/2c790b56-0a97-4d47-87d4-43921ea7ec0d)

    donde zα/2​ es el valor crítico de la distribución normal estándar para un nivel de confianza de α.

4. Comprobar si la media se encuentra entre los límites inferior y superior. Si la media calculada en el paso 1 se encuentra dentro de los límites calculados en el paso 2, entonces se puede concluir que los números pasan la prueba de medias.

##  Prueba de Varianza

La prueba de varianza es una prueba estadística que se utiliza para verificar la calidad de una secuencia de números pseudoaleatorios. Esta prueba se basa en la hipótesis de que los números generados siguen una distribución uniforme entre 0 y 1. Aquí están los pasos para realizar la prueba de varianza:

1. Obtener la varianza. La varianza se calcula con la siguiente fórmula:

    ![alt text](resouce\image-3.png)

    donde n es la cantidad total de números, ri​ es el i-ésimo número y rˉ es la media de los números.

2. Obtener los límites inferior y superior. Estos límites se calculan utilizando la distribución chi-cuadrada y un nivel de confianza predefinido (usualmente 95%). Los límites se calculan como:
    
    ![alt text](resouce\image-4.png)

    donde 

    ![alt text](resouce\image.png) 
    ![alt text](resouce\image-1.png) 
    
    son los valores críticos de la distribución chi-cuadrada para un nivel de confianza de α y n−1 grados de libertad.

3. Comprobar si la varianza se encuentra entre los límites inferior y superior. Si la varianza calculada en el paso 1 se encuentra dentro de los límites calculados en el paso 2, entonces se puede concluir que los números pasan la prueba de varianza. 

## Prueba Kolmogórov-Smirnov

Esta prueba consiste en comparar la distribución empírica de los datos con la distribución teórica. Se realiza de la sigiente manera:

1. Ordenar los datos en intervalos, para este caso 10, respectivamnte de de menor a mayor.
2. Calcular la probabilidad obtenida de un dato. Se calcula respecto a la frecuencia obtenida de cada intervalo, dividido en la cantidad de datos.
3. Calcular la probabilidad esperada de un dato. Se calcula respecto a la frecuencia esperada acumulada de cada intervalo, dividido en la cantidad de datos.
4. Calcular la diferencia máxima. Se calcula la diferencia entre las probabilidades anteriormente calculadas y se toma la máxima de estas diferencias.
5. Comparar la diferencia máxima con el valor crítico. El valor crítico se obtiene de la tabla de Kolmogorov-Smirnov para un nivel de significancia predefinido. Si la diferencia máxima es menor que el valor crítico, entonces se puede concluir que los datos siguen la distribución teórica1.

## Prueba Chi2  

La prueba de Chi cuadrado, permite evaluar si existe una diferencia significativa entre los resultados esperados y los observados, esto de la siguiente manera:

1. Calcular las frecuencias esperadas. 
2. Calcular las frecuencias observadas. 
3. Calcular el estadístico de Chi cuadrado. El estadístico de Chi cuadrado se calcula como la suma de las diferencias al cuadrado entre las frecuencias observadas y las esperadas, divididas por las frecuencias esperadas. En notación matemática, esto se expresa como:

    ![alt text](resouce\image-2.png)


    donde Oi​ son las frecuencias observadas y Ei​ son las frecuencias esperadas.

4. Comparar el estadístico de Chi cuadrado con el valor crítico. El valor crítico se obtiene de la tabla de Chi cuadrado para un nivel de significancia predefinido. Si el estadístico de Chi cuadrado es mayor que el valor crítico, entonces no pasa la prueba el conjunto de números.

## Prueba de Póker

Examina en forma individual los dígitos del número pseudoaleatorio generado. Aquí están los pasos para realizar la prueba de póker:

1. Tomar los dígitos. Se toman 5 dígitos a la vez de cada número pseudoaleatorio generado.
2. Clasificar los dígitos. Se clasifican los dígitos en las siguientes categorías: Par, dos pares, tercia, póker, quintilla, full y todos diferentes.
3. Calcular las frecuencias observadas. Se cuenta el número de veces que cada categoría aparece en los datos.
4. Calcular las frecuencias esperadas. Se calculan las frecuencias esperadas para cada categoría utilizando las probabilidades teóricas de cada mano de póker, que son las siguientes:
    Todos diferentes = 0.3024
    Un par = 0.504
    Dos pares = 0.108
    Tercia = 0.072
    Full = 0.009
    Quintilla = 0.0001
5. Se calcula el estadístico de Chi cuadrado como la suma de las diferencias al cuadrado entre las frecuencias observadas y las esperadas, divididas por las frecuencias esperadas.
6. Comparar el estadístico de Chi cuadrado con el valor crítico. Si el estadístico de Chi cuadrado es menor que el valor crítico para un nivel de significancia predefinido, entonces se puede concluir que los números pasan la prueba de póker.

