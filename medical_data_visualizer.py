import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Importa los datos de medical_examination.csv y asígnalos a la variable df.
df = pd.read_csv('medical_examination.csv')

# 2. Agrega una columna overweight (sobrepeso) a los datos.
# IMC = peso (kg) / (altura en metros)^2. La altura en el dataset está en cm, por eso se divide entre 100.
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2)).apply(lambda x: 1 if x > 25 else 0)

# 3. Normaliza los datos haciendo que 0 siempre sea bueno y 1 siempre sea malo.
# Si el valor de cholesterol o gluc es 1, cámbialo a 0. Si es mayor que 1, cámbialo a 1.
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# 4. Dibuja el gráfico categórico en la función draw_cat_plot.
def draw_cat_plot():
    # 5. Crea un DataFrame para el gráfico categórico usando pd.melt
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # 6. Agrupa y reformatea los datos en df_cat para dividirlos por cardio y mostrar los conteos.
    df_cat = pd.DataFrame(df_cat.groupby(['cardio', 'variable', 'value'])['value'].count()).rename(columns={'value': 'total'}).reset_index()

    # 7. Convierte los datos y crea un gráfico que muestre los conteos usando sns.catplot()
    fig = sns.catplot(
        x='variable', 
        y='total', 
        hue='value', 
        col='cardio', 
        data=df_cat, 
        kind='bar'
    ).fig

    # 8. Obtén la figura para la salida y guárdala en la variable fig.
    # (Ya se asignó arriba con .fig)

    # 9. No modifiques las siguientes dos líneas.
    fig.savefig('catplot.png')
    return fig


# 10. Dibuja el mapa de calor en la función draw_heat_map.
def draw_heat_map():
    # 11. Limpia los datos en la variable df_heat filtrando los segmentos incorrectos
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12. Calcula la matriz de correlación y guárdala en la variable corr.
    corr = df_heat.corr()

    # 13. Genera una máscara para el triángulo superior y guárdala en la variable mask.
    mask = np.triu(corr)

    # 14. Configura la figura de matplotlib.
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15. Grafica la matriz de correlación usando el método de seaborn: sns.heatmap().
    sns.heatmap(
        corr, 
        mask=mask, 
        annot=True, 
        fmt='.1f', 
        square=True, 
        linewidths=0.5, 
        cbar_kws={'shrink': 0.5}, 
        center=0, 
        vmin=-0.1, 
        vmax=0.25
    )

    # 16. No modifiques las siguientes dos líneas.
    fig.savefig('heatmap.png')
    return fig