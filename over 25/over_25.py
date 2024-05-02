import pandas as pd
import datetime

def over_25_years():
    # Creamos una lista que contiene los valores de la fecha actual con el siguiente formato: ["año", "mes", "día"]
    today = str(datetime.date.today()).split("-")
    
    # Convertimos los valores de la fecha actual en enteros
    for i, element in enumerate(today):
        today[i] = int(element)

    # Cargamos el archivo de edades
    ages = pd.read_csv('edades.csv', encoding="utf-8", header=None)
    
    # Formateamos el archivo de edades para obtener cada fecha con el siguiente formato: ["día", "mes", "año"]
    formated_ages = []
    for _index, age in ages[1:].iterrows():
        formated_ages.append(age[0].split("/"))
    
    # Creamos una lista que contiene todas las fechas de aquellas que nacieron del 1998 para atras, todos estos ya tienen 25 años o más
    over_25 = [a for a in formated_ages if int(a[2]) < today[0] - 25]
    # Para los que nacieron en el año 1999, se compara el mes y el dia para saber si ya han cumplido 25 años
    for age in [a for a in formated_ages if int(a[2]) == today[0] - 25]:
        # Si el mes es menor que el actual, automaticamente se agrega a la lista
        if (int(age[1]) < today[1]):
            over_25.append(age)
        # Si el mes es igual al actual y el dia es igual o menor, se agrega a la lista también
        elif (int(age[1]) == today[1] and int(age[0]) <= today[2]):
            over_25.append(age)
    
    # Convertimos las listas de las fechas en listas de enteros 
    for i, element in enumerate(over_25):
        over_25[i] = [int(element[0]), int(element[1]), int(element[2])]
    
    # Calculamos las edades
    calculated_ages = []
    for age in over_25:
        # Si el mes es menor que el actual, automaticamente se agrega a la lista
        if (age[1] < today[1]):
            calculated_ages.append(today[0] - age[2])
        # Si el mes es igual al actual y el dia es igual o menor, se agrega a la lista también
        elif (age[1] == today[1] and age[0] <= today[2]):
            calculated_ages.append(today[0] - age[2])
        # Calculamos las edades del resto y les restamos 1, esto por que todavía no han cumplido 25 años
        else:
            calculated_ages.append(today[0] - age[2] - 1)
    
    # Ordenamos las edades de manera ascendente
    calculated_ages.sort()

    # Creamos un diccionario con las edades y sus frecuencias
    fi = {}
    for i in calculated_ages:
        if i in fi:
            fi[i] += 1
        else:
            fi[i] = 1

    # Creamos un dataframe con las edades y sus frecuencias    
    df = pd.DataFrame({'Age':fi.keys(), 'Frequency':fi.values()})

    return df