import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

csv_path = "example_reports/clockify_report.csv"
csv_path_comparativo = "example_reports/clockify_report.csv"

def generar_grafica(csv_path, csv_path_comparativo):
    # Cargar los CSV
    df1 = pd.read_csv(csv_path)
    df2 = pd.read_csv(csv_path_comparativo)

    # Agrupar y redondear
    horas1 = df1.groupby("User")["Time (decimal)"].sum().round()
    horas2 = df2.groupby("User")["Time (decimal)"].sum().round()

    # Unificar usuarios
    all_users = sorted(set(horas1.index).union(set(horas2.index)))
    horas1 = horas1.reindex(all_users, fill_value=0)
    horas2 = horas2.reindex(all_users, fill_value=0)

    # Ordenar por horas actuales
    horas1 = horas1.sort_values(ascending=False)
    horas2 = horas2.reindex(horas1.index)

    # Preparar valores
    indices = np.arange(len(horas1))
    bar_height = 0.8  # Aumentar el tamaño de las barras
    n = len(horas1)

    # Transparencias graduales (de 1.0 a 0.6)
    transparencias = np.linspace(1.0, 0.6, n)

    # Inicializar gráfica
    plt.figure(figsize=(12, 8))

    for i, (user, alpha) in enumerate(zip(horas1.index, transparencias)):
        h1 = horas1[user]
        h2 = horas2[user]
        base = min(h1, h2)
        diff = abs(h1 - h2)

        # Colores con transparencia
        gris = (67/255, 67/255, 67/255, alpha)
        verde = (66/255, 181/255, 252/255, alpha)
        rojo = (222/255, 57/255, 43/255, alpha)

        # Parte base gris
        plt.barh(i, base, height=bar_height, color=gris)

        # Parte de diferencia
        if h1 > h2:
            plt.barh(i, diff, left=base, height=bar_height, color=verde)
        elif h2 > h1:
            plt.barh(i, diff, left=base, height=bar_height, color=rojo)

        # Elegir color de texto según si el anterior es mayor
        text_color = "white" if h2 > h1 else "black"

        # Etiqueta de horas actuales
        plt.text(h1 + 0.5, i, f"{h1:.0f} h", va='center', fontsize=10, fontweight='bold',
                 color=text_color, family="sans-serif")

    # Ejes y etiquetas
    plt.yticks(indices, horas1.index, fontsize=12, family="sans-serif")
    plt.xlabel("Horas", fontsize=14, family="sans-serif")
    plt.title("Diferencia de horas trabajadas por usuario", fontsize=16, family="sans-serif")
    plt.gca().invert_yaxis()

    # Eliminar la leyenda
    # handles, labels = plt.gca().get_legend_handles_labels()
    # by_label = dict(zip(labels, handles))
    # plt.legend(by_label.values(), by_label.keys(), fontsize=12)

    # Estilo gráfico
    for spine in ['top', 'right', 'left', 'bottom']:
        plt.gca().spines[spine].set_visible(False)
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

generar_grafica(csv_path, csv_path_comparativo)
