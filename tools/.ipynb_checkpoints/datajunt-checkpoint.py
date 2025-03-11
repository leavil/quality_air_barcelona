import pandas as pd
import os
import csv

# Definir el rango de fechas
start_year = 2019
start_month = 4  # Abril
end_year = 2025
end_month = 1    # Enero

# Lista para almacenar los DataFrames
dataframes = []

# Función para obtener el nombre del mes en catalán
def get_month_name_catalan(month):
    months_catalan = {
        1: "Gener", 2: "Febrer", 3: "Març", 4: "Abril", 5: "Maig", 6: "Juny",
        7: "Juliol", 8: "Agost", 9: "Setembre", 10: "Octubre", 11: "Novembre", 12: "Desembre"
    }
    return months_catalan.get(month, "")

# Función para detectar el delimitador de un archivo CSV
def detect_delimiter(file_path):
    with open(file_path, 'r') as file:
        first_line = file.readline()
    # Delimitadores comunes: coma (,), punto y coma (;), tabulación (\t)
    delimiters = [',', ';', '\t']
    delimiter = csv.Sniffer().sniff(first_line).delimiter
    return delimiter

# Iterar sobre el rango de fechas
for year in range(start_year, end_year + 1):
    for month in range(1, 13):
        # Saltar los meses antes de abril de 2019
        if year == start_year and month < start_month:
            continue
        # Saltar los meses después de enero de 2025
        if year == end_year and month > end_month:
            continue

        # Obtener el nombre del mes en catalán
        month_name = get_month_name_catalan(month)

        # Generar el nombre del archivo
        file_name = f"/content/{year}_{month:02d}_{month_name}_qualitat_aire_BCN.csv"

        # Verificar si el archivo existe
        if os.path.exists(file_name):
            # Detectar el delimitador del archivo
            delimiter = detect_delimiter(file_name)
            print(f"Archivo: {file_name}, Delimitador detectado: '{delimiter}'")

            # Leer el archivo con el delimitador correcto
            df = pd.read_csv(file_name, delimiter=delimiter)
            dataframes.append(df)
        else:
            print(f"Archivo no encontrado: {file_name}")

# Concatenar todos los DataFrames en uno solo
if dataframes:
    final_df = pd.concat(dataframes, ignore_index=True)

    # Eliminar filas duplicadas (por si acaso)
    final_df = final_df.drop_duplicates()

    print("Proceso completado. DataFrame final creado.")
    print(f"Número de filas en el DataFrame final: {len(final_df)}")
else:
    print("No se encontraron archivos en el rango especificado.")
