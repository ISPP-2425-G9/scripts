import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

csv_path = "clockify_reports/clockify_report_sprint3_final_1004.csv"
csv_path_comparativo = "clockify_reports/clockify_report_2703.csv"

def generar_grafica(csv_path, csv_path_comparativo):
    # Cargar los dos archivos CSV
    df1 = pd.read_csv(csv_path)
    df2 = pd.read_csv(csv_path_comparativo)

    # Agrupar y sumar por usuario
    horas1 = df1.groupby("User")["Time (decimal)"].sum().round()
    horas2 = df2.groupby("User")["Time (decimal)"].sum().round()

    # Asegurar que ambos DataFrames tengan los mismos usuarios
    all_users = sorted(set(horas1.index).union(set(horas2.index)))
    horas1 = horas1.reindex(all_users, fill_value=0)
    horas2 = horas2.reindex(all_users, fill_value=0)

    # Ordenar por horas del reporte actual (horas1)
    horas1 = horas1.sort_values(ascending=False)
    horas2 = horas2.reindex(horas1.index)

    # Posición de las barras
    indices = np.arange(len(horas1))
    bar_width = 0.4

    # Crear gradiente azul
    azul_cmap = plt.cm.colors.LinearSegmentedColormap.from_list(
        "azul", [(66/255, 181/255, 252/255, 1), (66/255, 181/255, 252/255, 0.5)]
    )
    azul_gradient = azul_cmap(np.linspace(0, 1, len(horas1)))

    # Crear gradiente gris
    gris_cmap = plt.cm.colors.LinearSegmentedColormap.from_list(
        "gris", [(67/255, 67/255, 67/255, 1), (67/255, 67/255, 67/255, 0.7)]
    )
    gris_gradient = gris_cmap(np.linspace(0, 1, len(horas1)))

    # Crear la gráfica
    plt.figure(figsize=(12, 8))
    bars1 = plt.barh(indices - bar_width/2, horas1.values, height=bar_width, color=azul_gradient)
    bars2 = plt.barh(indices + bar_width/2, horas2.values, height=bar_width, color=gris_gradient)

    # Etiquetas
    plt.xlabel("Horas", fontsize=14, family="sans-serif")
    plt.title("Comparación de horas trabajadas por usuario", fontsize=16, family="sans-serif")
    plt.yticks(indices, horas1.index, fontsize=12, family="sans-serif")
    plt.gca().invert_yaxis()

    # Añadir etiquetas a las barras
    for bar1, bar2 in zip(bars1, bars2):
        if bar1.get_width() > 0:
            plt.text(bar1.get_width() + 0.5, bar1.get_y() + bar1.get_height()/2,
                     f"{bar1.get_width():.0f} h", va='center', fontsize=10, fontweight='bold', family="sans-serif")
        if bar2.get_width() > 0:
            plt.text(bar2.get_width() + 0.5, bar2.get_y() + bar2.get_height()/2,
                     f"{bar2.get_width():.0f} h", va='center', fontsize=10, color="#434343", family="sans-serif")

    # Estética
    plt.legend(fontsize=12)
    for spine in ['top', 'right', 'left', 'bottom']:
        plt.gca().spines[spine].set_visible(False)
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

generar_grafica(csv_path, csv_path_comparativo)
