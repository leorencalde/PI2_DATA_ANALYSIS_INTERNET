import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de la página
st.set_page_config(page_title='Dashboard de Acceso a Internet en Argentina', layout='wide')

# Función para cargar datos
@st.cache_data
def cargar_datos():
    file_path = './Datasets/Internet.xlsx'
    file_path_map = './Datasets/mapa_conectividad.xlsx'
    xls = pd.ExcelFile(file_path)
    xls_map = pd.ExcelFile(file_path_map)

    mapa_conectividad = pd.read_excel(xls_map, sheet_name='Hoja3')
    mapa_conectividad['Longitud'] = pd.to_numeric(mapa_conectividad['Longitud'], errors='coerce')
    mapa_conectividad['Latitud'] = pd.to_numeric(mapa_conectividad['Latitud'], errors='coerce')
    mapa_conectividad.rename(columns={'Latitud': 'latitude', 'Longitud': 'longitude'}, inplace=True)
    mapa_conectividad.dropna(subset=['latitude', 'longitude'], inplace=True)
        
    dataframes = {
        'Acc_vel_loc_sinrangos': pd.read_excel(xls, sheet_name='Acc_vel_loc_sinrangos'),
        'Velocidad_sin_Rangos': pd.read_excel(xls, sheet_name='Velocidad_sin_Rangos'),
        'Velocidad_por_prov': pd.read_excel(xls, sheet_name='Velocidad % por prov'),
        'Totales_vmd': pd.read_excel(xls, sheet_name='Totales VMD'),
        'Accesos_tecnologia_localidad': pd.read_excel(xls, sheet_name='Accesos_tecnologia_localidad'),
        'Totales_accesos_por_tecnologia': pd.read_excel(xls, sheet_name='Totales Accesos Por Tecnología'),
        'Accesos_por_tecnologia': pd.read_excel(xls, sheet_name='Accesos Por Tecnología'),
        'Dial_baf': pd.read_excel(xls, sheet_name='Dial-BAf'),
        'Totales_dial_baf': pd.read_excel(xls, sheet_name='Totales Dial-BAf'),
        'Penetracion_poblacion': pd.read_excel(xls, sheet_name='Penetración-poblacion'),
        'Penetracion_hogares': pd.read_excel(xls, sheet_name='Penetracion-hogares'),
        'Penetracion_totales': pd.read_excel(xls, sheet_name='Penetracion-totales'),
        'Totales_accesos_por_velocidad': pd.read_excel(xls, sheet_name='Totales Accesos por velocidad'),
        'Accesos_por_velocidad': pd.read_excel(xls, sheet_name='Accesos por velocidad'),
        'Ingresos': pd.read_excel(xls, sheet_name='Ingresos')
    }
    
    return mapa_conectividad, dataframes

# Cargar datos
mapa_conectividad, dataframes = cargar_datos()

# Título del dashboard
st.title('Acceso a Internet en Argentina')
st.subheader('Por: Leonardo Renteria - Analista de Datos')

# Sidebar para filtros
st.sidebar.header('Filtros')

# Filtros de selección
provincias = dataframes['Accesos_por_tecnologia']['Provincia'].unique()
provincias = list(provincias)
provincias.insert(0, "Seleccionar todas")
provincia_seleccionada = st.sidebar.multiselect('Selecciona Provincia(s):', provincias, default="Seleccionar todas")
if "Seleccionar todas" in provincia_seleccionada:
    provincia_seleccionada = provincias[1:]  # Excluye la opción "Seleccionar todas"

años = list(dataframes['Accesos_por_tecnologia']['Año'].unique())
años.insert(0, "Todos")
año_seleccionado = st.sidebar.selectbox('Selecciona Año:', años)
if año_seleccionado == "Todos":
    años_filtrados = dataframes['Accesos_por_tecnologia']['Año'].unique()
else:
    años_filtrados = [año_seleccionado]

trimestres = dataframes['Accesos_por_tecnologia']['Trimestre'].unique()
trimestre_seleccionado = st.sidebar.selectbox('Selecciona Trimestre:', trimestres)

# Filtrar datos según selección
df_accesos_filtrado = dataframes['Accesos_por_tecnologia'][
    (dataframes['Accesos_por_tecnologia']['Provincia'].isin(provincia_seleccionada)) &
    (dataframes['Accesos_por_tecnologia']['Año'].isin(años_filtrados))
]
df_ingresos_filtrado = dataframes['Ingresos'][dataframes['Ingresos']['Año'].isin(años_filtrados)]

# Visualización de accesos
st.subheader('Total de Accesos a Internet por Provincia')
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=df_accesos_filtrado, x='Provincia', y='Total', hue='Año', ax=ax)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
plt.ylabel('Número de Accesos')
st.pyplot(fig)

# Visualización de Mapa Accesos a Internet por Provincia
st.subheader('Distribución Geográfica Acceso a Internet en Argentina')
fig, ax = plt.subplots(figsize=(10, 6))
st.map(mapa_conectividad[['latitude', 'longitude']])

# Visualización de ingresos
st.subheader('Ingresos generados por servicios de Internet')
fig, ax = plt.subplots(figsize=(10, 6))
df_ingresos_filtrado = df_ingresos_filtrado.iloc[::-1]
sns.lineplot(data=df_ingresos_filtrado, x='Periodo', y='Ingresos (miles de pesos)', marker='o', ax=ax)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
plt.ylabel('Ingresos (miles de pesos)')
plt.title('Ingresos Generados por Servicios de Internet')
plt.grid(True)
st.pyplot(fig)

# Métricas de KPI
st.subheader('Métricas Clave para Monitorear el Progreso (KPI)')
st.subheader('Objetivo: Aumentar en un 2% el acceso al servicio de internet para el próximo trimestre, cada 100 hogares, por provincia.')
kpi_data = dataframes['Penetracion_hogares'].copy()
kpi_data['Nuevo_acceso'] = kpi_data['Accesos por cada 100 hogares'] * 1.02
kpi_data['KPI'] = ((kpi_data['Nuevo_acceso'] - kpi_data['Accesos por cada 100 hogares']) / kpi_data['Accesos por cada 100 hogares']) * 100

col1, col2 = st.columns(2)
col1.metric(label="Aumento en el acceso a internet (%)", value=f"{kpi_data['KPI'].mean():.2f} %")

# Conclusiones
st.subheader('Conclusiones')
st.markdown("""
A partir del análisis de los datos de acceso a internet en Argentina, podemos extraer las siguientes conclusiones:

1. **Distribución Desigual:** Existe una distribución desigual de accesos a internet entre las diferentes provincias, con algunas provincias mostrando una mayor penetración y otras rezagadas.
2. **Áreas de Baja Penetración:** Identificamos áreas geográficas con baja penetración de servicios, que representan oportunidades para expandir la cobertura y mejorar la calidad del servicio.
3. **Nuevas Áreas para Expansión:** Las provincias con baja penetración actual son candidatas ideales para futuras expansiones de servicio.            
4. **Crecimiento Sostenido:** Los ingresos por servicios de internet han mostrado un crecimiento sostenido a lo largo de los años, indicando una mayor adopción y demanda de servicios de alta velocidad.


""")
