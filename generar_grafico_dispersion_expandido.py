import pandas as pd
import matplotlib.pyplot as plt
from numpy import polyfit

# Cargar el archivo CSV
file_path = 'rendientoXhoras_reports/horas_rendimiento_1004.csv' # Cambia esto por la ruta de tu archivo
data = pd.read_csv(file_path)

# Definir la posición de la línea vertical ajustable
linea_horas_minimas = 20  # Puedes cambiar este valor para ajustar la línea vertical

# Convertir las columnas necesarias a formatos numéricos, asegurándose de tratar tanto las horas como el rendimiento con decimales
data['Horas'] = data['Horas'].apply(lambda x: float(str(x).replace(',', '.')))  # Reemplazar coma por punto y convertir a float
data['Rendimiento'] = data['Rendimiento'].apply(lambda x: float(str(x).replace(',', '.')))  # Reemplazar coma por punto y convertir a float

# Calcular los coeficientes de la regresión lineal (ajuste lineal)
coeficientes = polyfit(data['Horas'], data['Rendimiento'], 1)  # Ajuste lineal de primer grado
pendiente, interseccion = coeficientes  # Pendiente (m) e intersección (b) de la recta

# Crear el gráfico de dispersión
plt.figure(figsize=(8, 6))

# Eliminar bordes de la figura
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)

# Crear el gráfico de dispersión con color personalizado
plt.scatter(data['Horas'], data['Rendimiento'], color='#42b5fc', alpha=0.7)  # Cambié el color a #42b5fc

# Establecer los límites de los ejes
plt.xlim(0, data['Horas'].max() * 1.1)  # 10% adicional para dar un pequeño margen
plt.ylim(0, data['Rendimiento'].max() * 1.1)  # 10% adicional para dar un pequeño margen

# Colorear los cuadrantes con transparencia del 20%
plt.fill_betweenx([0, 5], 0, linea_horas_minimas, color='#f0684d', alpha=0.2)  # Cuadrante inferior izquierdo
plt.fill_betweenx([5, data['Rendimiento'].max() * 1.1], 0, linea_horas_minimas, color='#5C5C5C', alpha=0.2)  # Cuadrante superior izquierdo
plt.fill_betweenx([0, 5], linea_horas_minimas, data['Horas'].max() * 1.1, color='#5C5C5C', alpha=0.2)  # Cuadrante inferior derecho
plt.fill_betweenx([5, data['Rendimiento'].max() * 1.1], linea_horas_minimas, data['Horas'].max() * 1.1, color='#42b5fc', alpha=0.2)  # Cuadrante superior derecho

# Dibujar la línea vertical en la posición ajustable de las horas
plt.axvline(x=linea_horas_minimas, color='r', linestyle='--', linewidth=1)  # Línea vertical ajustable

# Dibujar la línea horizontal en 5 de rendimiento
plt.axhline(y=5, color='g', linestyle='--', linewidth=1)  # Línea horizontal en 5 rendimiento

# Dibujar la línea de tendencia calculada (valor esperado entre horas y rendimiento)
x_line = [0, data['Horas'].max() * 1.1]  # Rango de x para la línea
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
