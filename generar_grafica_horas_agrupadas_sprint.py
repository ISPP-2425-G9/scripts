import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

def grafica_barras_apiladas_por_proyecto(csv_path):
    # Cargar el archivo CSV
    df = pd.read_csv(csv_path)

    # Agrupar por Usuario y Proyecto, sumando las horas decimales
    df_grouped = df.groupby(['User', 'Project'])['Time (decimal)'].sum().reset_index()

    # Obtener lista de usuarios únicos
    usuarios = df_grouped['User'].unique()

    # Calcular las horas totales por usuario
    horas_totales_usuario = df_grouped.groupby('User')['Time (decimal)'].sum().reset_index()
    
    # Ordenar los usuarios por horas totales, de menor a mayor
    horas_totales_usuario = horas_totales_usuario.sort_values(by='Time (decimal)', ascending=True)
    usuarios_ordenados = horas_totales_usuario['User'].values

    # Definir un orden específico para los proyectos
    proyectos_ordenados = ["Devising a Project", "Sprint 1", "Sprint 2", "Sprint 3", "Preparing Project Launch"]

    # Crear un diccionario con colores personalizados para los proyectos
    colores_proyectos = {
        proyectos_ordenados[i]: color
        for i, color in enumerate(['#434343', '#de392b', '#2da44e' , '#fbbc04', '#42b5fc'])
    }

    # Crear figura
    plt.figure(figsize=(14, 8))

    # Posiciones verticales para cada usuario
    y_positions = np.arange(len(usuarios_ordenados))

    for i, usuario in enumerate(usuarios_ordenados):
        usuario_data = df_grouped[df_grouped['User'] == usuario]
        
        # Reordenar los proyectos según el orden que hemos definido
        usuario_data['Project'] = pd.Categorical(usuario_data['Project'], categories=proyectos_ordenados, ordered=True)
        usuario_data = usuario_data.sort_values(by='Project')  # Ahora se ordenan por el orden predeterminado de los proyectos
        
        left = 0  # punto inicial de la barra
        total_horas = usuario_data['Time (decimal)'].sum()  # Total de horas de cada usuario

        for _, row in usuario_data.iterrows():
            horas = row['Time (decimal)']
            proyecto = row['Project']
            color = colores_proyectos.get(proyecto, '#42b5fc')  # Color por defecto si no está en el diccionario
            plt.barh(i, horas, left=left, height=0.8, color=color, edgecolor='white')  # Aumento de grosor de las barras (height=0.8)
            left += horas
        
        # Redondear las horas totales y añadir "h" al final en negrita
        total_horas_redondeadas = round(total_horas)
        plt.text(left, i, f'{total_horas_redondeadas}h', va='center', ha='left', fontsize=12, color='black', fontweight='bold')

    # Etiquetas de usuario en el eje Y
    plt.yticks(y_positions, usuarios_ordenados, fontsize=12)
    plt.xlabel('Horas trabajadas (decimales)', fontsize=14)
    plt.title('Distribución de horas por usuario', fontsize=16)

    # Limpiar estilo
    for spine in ['top', 'right', 'left', 'bottom']:
        plt.gca().spines[spine].set_visible(False)

    plt.tight_layout()
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.show()

# 👉 USO:
# Reemplaza con tu ruta
ruta_csv = "clockify_sprint_report2504.csv"
grafica_barras_apiladas_por_proyecto(ruta_csv)
