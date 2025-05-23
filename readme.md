# Análisis de la Calidad del Aire en Barcelona

Este proyecto realiza un análisis exploratorio de los niveles de contaminación atmosférica en distintas estaciones de la ciudad de Barcelona. Utiliza técnicas estadísticas y de visualización para estudiar la evolución de contaminantes como el ozono (O₃), NO₂ y PM₁₀, entre otros.

## Autores

- **Arnau González Almirall**
- **Germán Bueno Lozano**

## Descripción del Proyecto

Este proyecto tiene como objetivo realizar un análisis exploratorio de datos (EDA) sobre la calidad del aire en Barcelona, considerando los datos meteorológicos de lluvia y temperatura. El análisis incluye la exploración de correlaciones, eventos extremos, tendencias temporales y visualizaciones de datos para identificar patrones y relaciones entre los contaminantes y las variables meteorológicas.

## Estructura de Carpetas

```
tu_proyecto/
├── .ipynb_checkpoints/
├── data/
├── docs/
├── notebooks/
├── reports/
│   ├── correlaciones/
│   ├── eventos/
│   ├── exploración/
│   ├── temporal/
│   ├── visualizaciones/
│   └── ....
├── src/
├── tools/
├── .gitattributes
├── .gitignore
├── descomprimir_datos.py
├── link
├── README.md
└── requirements.txt

```

En la carpeta `reports`, se encuentran varias subcarpetas que contienen visualizaciones y análisis específicos:

- **Correlaciones**:
  - ![Gráfico de pares de estaciones](reports\correlaciones\pairplot_estaciones.png)
  - ![Matriz de correlación entre variables](reports\correlaciones\matriz_correlacion.png)

- **Eventos**:
  - ![Relación entre gases y variables meteorológicas](reports\eventos\relaciones_gases_meteo.png)

- **Exploración**:
  - ![Mapa de calor de estaciones](reports\exploracion\heatmap_estaciones.png)
  - ![Histogramas de contaminantes](reports\exploracion\histogramas_contaminantes.png)

- **Temporal**:
  - ![Evolución mensual de contaminantes](reports\temporal\evolucion_mensual.png)

- **Visualizaciones**:
  - ![Cargas factoriales del Análisis de Componentes Principales (PCA)](reports\visualizaciones\pca_cargas_factoriales.png)

- **Estacionalidad**:
  - ![Gráficos de estacionalidad para cada contaminante](reports\estacionalidad\estacionalidad_contaminantes.png)


## Requisitos

### Instalación completa

Para instalar todos los paquetes necesarios, incluyendo soporte geoespacial:

```bash
pip install -r requirements.txt
```

### Instalación mínima (sin geoespacial)

Para ejecutar el análisis sin funcionalidades geoespaciales:

```bash
pip install pandas numpy matplotlib seaborn plotly scikit-learn jupyter py7zr
```

## Descompresión de los datos

Debido al tamaño de los archivos, estos se proporcionan comprimidos en formato `.7z`.

### Requisitos previos

Instala el paquete necesario para la descompresión:

```bash
pip install py7zr
```

### Estructura de carpetas esperada

```
tu_proyecto/
├── notebooks/
│   └── quality_air_bcn_final.7z
├── descomprimir_datos.py
└── ...
```

### Ejecución del script de descompresión

```bash
python descomprimir_datos.py
```

### Características del script `descomprimir_datos.py`

- Verifica que los archivos existan antes de intentar descomprimirlos.
- Crea automáticamente la carpeta `notebooks/datos_descomprimidos/`.
- Maneja errores durante la descompresión de forma segura.
- Proporciona mensajes claros sobre el estado del proceso.

## Objetivo del Trabajo

Realizar un análisis exploratorio de datos (EDA) sobre la calidad del aire en Barcelona, considerando los datos meteorológicos de lluvia y temperatura.

## Datos a Utilizar

- Datos de calidad del aire (por ejemplo, niveles de PM2.5, PM10, NO2, O3, SO2, CO).
- Datos meteorológicos (lluvia y temperatura).

## Pasos a Seguir

1. **Carga y Limpieza de Datos**:
   - Cargar los datasets de calidad del aire y meteorológicos.
   - Realizar una limpieza inicial de los datos: manejo de valores faltantes, eliminación de duplicados, corrección de formatos, etc.

2. **Exploración Inicial**:
   - Realizar un resumen estadístico de los datos (media, mediana, desviación estándar, valores mínimos y máximos).
   - Visualizar la distribución de las variables principales (histogramas, boxplots).

3. **Análisis de Correlación**:
   - Calcular y visualizar la matriz de correlación entre las variables de calidad del aire y las variables meteorológicas.
   - Identificar posibles relaciones entre la lluvia, la temperatura y los contaminantes del aire.

4. **Análisis Temporal**:
   - Analizar las tendencias temporales de los contaminantes y las variables meteorológicas (gráficos de series temporales).
   - Identificar patrones estacionales o diarios en los datos.

5. **Análisis de Eventos Extremos**:
   - Identificar días con niveles extremos de contaminación o condiciones meteorológicas inusuales.
   - Analizar cómo estos eventos extremos afectan la calidad del aire.

6. **Visualización de Datos**:
   - Crear visualizaciones que muestren la relación entre la lluvia, la temperatura y la calidad del aire (gráficos de dispersión, mapas de calor).
   - Utilizar mapas para visualizar la distribución espacial de los contaminantes en Barcelona.

7. **Análisis de Componentes Principales (PCA)**:
   - Aplicar PCA para reducir la dimensionalidad de los datos y identificar los componentes principales que explican la variabilidad en los datos.

8. **Conclusiones y Recomendaciones**:
   - Resumir los hallazgos principales del análisis.
   - Proponer recomendaciones basadas en los resultados del EDA.

## Herramientas y Librerías a Utilizar

- Python con librerías como Pandas, NumPy, Matplotlib, Seaborn, Plotly, y Scikit-learn.
- Jupyter Notebook para la documentación y visualización del análisis.