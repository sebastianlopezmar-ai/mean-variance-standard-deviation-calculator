import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Importar los datos
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Crear el diagrama de dispersión
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', alpha=0.7)

    # 3. Crear la primera línea de mejor encaje (desde 1880 hasta el 2050)
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series([i for i in range(df['Year'].min(), 2051)])
    y_pred = res.slope * x_pred + res.intercept
    ax.plot(x_pred, y_pred, color='red', label='Best Fit Line (1880-2050)')

    # 4. Crear la segunda línea de mejor encaje (desde el año 2000 hasta el 2050)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred_recent = pd.Series([i for i in range(2000, 2051)])
    y_pred_recent = res_recent.slope * x_pred_recent + res_recent.intercept
    ax.plot(x_pred_recent, y_pred_recent, color='green', label='Best Fit Line (2000-2050)')

    # 5. Añadir etiquetas y título
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Guardar y retornar la figura (No modificar)
    fig.savefig('sea_level_plot.png')
    return fig