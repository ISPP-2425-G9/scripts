import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

csv_path = "clockify_reports/clockify_report_sprint3_final_1004.csv"

def generar_grafica(csv_path):
    # Cargar el archivo CSV
    df = pd.read_csv(csv_path)

    # Agrupar por usuario y sumar el tiempo decimal
    df_grouped = df.groupby("User")["Time (decimal)"].sum().sort_values(ascending=False)
    print(df_grouped)
    # Redondear las horas para que no haya decimales
    df_grouped = df_grouped.round()

    # Crear el gradiente de color azul con transparencia
    colors = [(66/255, 181/255, 252/255, 1), (66/255, 181/255, 252/255, 0.5)]  # Azul con transparencia
    cmap = plt.cm.colors.LinearSegmentedColormap.from_list("blue_gradient", colors)

    # Crear la gráfica horizontal de barras con gradiente
    plt.figure(figsize=(12, 8))
    bars = plt.barh(df_grouped.index, df_grouped.values, color=cmap(np.linspace(0, 1, len(df_grouped))))

    # Ajustar el tamaño de los nombres y cambiar la fuente
    plt.xlabel("Horas", fontsize=14, family="sans-serif")
    plt.title("Resumen de horas trabajadas por usuario", fontsize=16, family="sans-serif")
    plt.gca().invert_yaxis()  # Para que el usuario con más horas aparezca arriba

    # Añadir etiquetas con el número de horas a cada barra
    for bar in bars:
        width = bar.get_width()
        plt.text(width + 0.5, bar.get_y() + bar.get_height()/2,
                 f"{width:.0f} h", va='center', fontsize=12, fontweight='bold', family="sans-serif")

    # Cambiar el tamaño de los nombres de los usuarios y la fuente
    plt.yticks(fontsize=12, family="sans-serif")

    # Eliminar el borde negro
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)

    # Mostrar la gráfica sin el borde
    plt.tight_layout()
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.show()

generar_grafica(csv_path)