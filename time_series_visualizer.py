import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Importar datos (No cambiar la fecha de análisis ni el índice)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Limpiar los datos filtrando los días en el 2.5% superior e inferior del conjunto de datos
df = df[
    (df['value'] >= df['value'].quantile(0.025)) & 
    (df['value'] <= df['value'].quantile(0.975))
]

def draw_line_plot():
    # Dibujar gráfico de líneas
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df.index, df['value'], color='red', linewidth=1)
    
    ax.setTitle('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Guardar imagen y retornar figura (No modificar)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copiar y preparar datos para el gráfico de barras agrupado por mes y año
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    
    # Agrupar por año y mes calculando el promedio
    df_bar_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    
    # Ordenar los meses correctamente
    months_order = [
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    df_bar_grouped = df_bar_grouped.reindex(columns=months_order)

    # Dibujar gráfico de barras
    fig = df_bar_grouped.plot(kind='bar', figsize=(15, 10), xlabel='Years', ylabel='Average Page Views').figure
    plt.legend(title='Months', labels=months_order)
    plt.xticks(rotation=0)

    # Guardar imagen y retornar figura (No modificar)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Preparar datos para los diagramas de caja (Box Plots)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')
    
    # Ordenar meses abreviados para la estacionalidad
    months_order_short = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Configurar los subplots de Matplotlib
    fig, axes = plt.subplots(1, 2, figsize=(20, 6))

    # Primer diagrama de caja: Year-wise Box Plot (Trend)
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].setTitle('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Segundo diagrama de caja: Month-wise Box Plot (Seasonality)
    sns.boxplot(x='month', y='value', data=df_box, order=months_order_short, ax=axes[1])
    axes[1].setTitle('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Guardar imagen y retornar figura (No modificar)
    fig.savefig('box_plot.png')
    return fig