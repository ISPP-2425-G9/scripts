import pandas as pd
import matplotlib.pyplot as plt
from numpy import polyfit

# Cargar el archivo CSV
file_path = 'rendientoXhoras_reports/horas_rendimiento_1004.csv' # Cambia esto por la ruta de tu archivo
data = pd.read_csv(file_path)

# Definir la posición de la línea vertical ajustable
linea_horas_minimas = 10  # Puedes cambiar este valor para ajustar la línea vertical

# Convertir las columnas necesarias a formatos numéricos, asegurándose de tratar tanto las horas como el rendimiento con decimales
data['Horas'] = data['Horas'].apply(lambda x: float(str(x).replace(',', '.')))  # Reemplazar coma por punto y convertir a float
data['Rendimiento'] = data['Rendimiento'].apply(lambda x: float(str(x).replace(',', '.')))  # Reemplazar coma por punto y convertir a float

# Calcular los coeficientes de la regresión lineal (ajuste lineal)
coeficientes = polyfit(data['Horas'], data['Rendimiento'], 1)  # Ajuste lineal de primer grado
pendiente, interseccion = coeficientes  # Pendiente (m) e intersección (b) de la recta

# Crear el gráfico de dispersión
plt.figure(figsize=(8, 6))

# Eliminar bordes superiores y derechos, pero agregar bordes más oscuros en la parte inferior y izquierda
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_color('gray')  # Borde izquierdo más oscuro
plt.gca().spines['left'].set_linewidth(1.5)  # Grosor del borde izquierdo
plt.gca().spines['bottom'].set_color('gray')  # Borde inferior más oscuro
plt.gca().spines['bottom'].set_linewidth(1.5)  # Grosor del borde inferior

# Crear el gráfico de dispersión con puntos más grandes
plt.scatter(data['Horas'], data['Rendimiento'], color='#42b5fc', alpha=0.7, s=100)  # Aumenté el tamaño de los puntos con `s=100`

# Establecer los límites de los ejes basados en el valor mínimo y máximo de las columnas
x_min = data['Horas'].min()
x_max = data['Horas'].max()
y_min = data['Rendimiento'].min()
y_max = data['Rendimiento'].max()

# Añadir un pequeño margen para evitar que los puntos queden pegados a los bordes
margen_x = (x_max - x_min) * 0.05  # 5% de margen en el eje X
margen_y = (y_max - y_min) * 0.05  # 5% de margen en el eje Y

# Establecer los límites de los ejes con el margen adicional
plt.xlim(x_min - margen_x, x_max + margen_x)
plt.ylim(y_min - margen_y, y_max + margen_y)

# Dibujar la línea vertical en la posición ajustable de las horas
plt.axvline(x=linea_horas_minimas, color='r', linestyle='--', linewidth=1)  # Línea vertical ajustable

# Dibujar la línea horizontal en 5 de rendimiento
plt.axhline(y=5, color='g', linestyle='--', linewidth=1)  # Línea horizontal en 5 rendimiento

# Dibujar la línea de tendencia calculada (valor esperado entre horas y rendimiento)
x_line = [x_min - margen_x, x_max + margen_x]  # Rango de x para la línea
y_line = [pendiente * x + interseccion for x in x_line]  # Ecuación de la recta

# Dibujar la línea de valor esperado en color f0684d
plt.plot(x_line, y_line, color='#f0684d', linestyle='-', linewidth=2)  # Línea de valor esperado

# Etiquetas y título
plt.title('Mapa de Puntos: Horas vs Rendimiento')
plt.xlabel('Horas')
plt.ylabel('Rendimiento')

# Hacer las líneas de la cuadrícula más claras
plt.grid(True, linestyle='-', color='gray', alpha=0.3)

# Mostrar el gráfico sin la leyenda de las líneas
plt.show()
