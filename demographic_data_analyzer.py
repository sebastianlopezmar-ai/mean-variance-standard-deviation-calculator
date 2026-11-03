import pandas as pd


def calculate_demographic_data(print_data=True):
    # Leer el archivo de datos
    df = pd.read_csv('adult.data.csv')

    # 1. ¿Cuántas personas de cada raza están representadas en este conjunto de datos? 
    # (Esto debe ser una serie de Pandas con los nombres de las razas como índices).
    race_count = df['race'].value_counts()

    # 2. ¿Cuál es la edad promedio de los hombres?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. ¿Cuál es el porcentaje de personas que tienen un grado de licenciatura (Bachelors)?
    total_bachelors = df[df['education'] == 'Bachelors'].shape[0]
    total_people = df.shape[0]
    percentage_bachelors = round((total_bachelors / total_people) * 100, 1)

    # 4. ¿Qué porcentaje de personas con una educación avanzada (Bachelors, Masters, o Doctorate) generan más de 50k?
    # 5. ¿Qué porcentaje de personas sin una educación avanzada generan más de 50k?
    
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    # Porcentaje con educación avanzada que ganan >50K
    higher_education_rich = round(
        (df[higher_education & (df['salary'] == '>50K')].shape[0] / df[higher_education].shape[0]) * 100, 1
    )
    
    # Porcentaje sin educación avanzada que ganan >50K
    lower_education_rich = round(
        (df[lower_education & (df['salary'] == '>50K')].shape[0] / df[lower_education].shape[0]) * 100, 1
    )

    # 6. ¿Cuál es el mínimo número de horas que una persona trabaja por semana?
    min_work_hours = df['hours-per-week'].min()

    # 7. ¿Qué porcentaje de personas que trabajan el mínimo de horas por semana tienen un salario de más de 50k?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100, 1
    )

    # 8. ¿Qué país tiene el porcentaje más alto de personas que ganan >50K y cuál es ese porcentaje?
    country_earnings = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_total = df['native-country'].value_counts()
    highest_earning_country_percentage = (country_earnings / country_total * 100).dropna()
    
    highest_earning_country = highest_earning_country_percentage.idxmax()
    highest_earning_country_percentage = round(highest_earning_country_percentage.max(), 1)

    # 9. Identifica la ocupación más popular para quienes ganan >50K en India.
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    # NO MODIFICAR DE AQUÍ EN ADELANTE (impresión de resultados si print_data es True)
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }