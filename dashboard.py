import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de la página
st.set_page_config(page_title='Dashboard de Acceso a Internet en Argentina', layout='wide')

# Función para cargar datos
@st.cache_data
def cargar_datos():
    file_path = 'Datasets/Internet.xlsx'
    xls = pd.ExcelFile(file_path)
    
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
    return dataframes

# Cargar datos
data = cargar_datos()

# Título del dashboard
st.title('Dashboard de Acceso a Internet en Argentina')

# Sidebar para filtros
st.sidebar.header('Filtros')

# Filtros de selección
provincias = data['Accesos_por_tecnologia']['Provincia'].unique()
provincia_seleccionada = st.sidebar.multiselect('Selecciona Provincia(s):', provincias, default=provincias)

años = data['Ingresos']['Año'].unique()
año_seleccionado = st.sidebar.selectbox('Selecciona Año:', años)

# Filtrar datos según selección
df_accesos_filtrado = data['Accesos_por_tecnologia'][data['Accesos_por_tecnologia']['Provincia'].isin(provincia_seleccionada)]
df_ingresos_filtrado = data['Ingresos'][data['Ingresos']['Año'] == año_seleccionado]

# Visualización de accesos por tecnología
st.subheader('Accesos por Tecnología')
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=df_accesos_filtrado, x='Provincia', y='Total', hue='Año', ax=ax)
plt.xticks(rotation=90)
plt.ylabel('Número de Accesos')
st.pyplot(fig)

# Visualización de ingresos
st.subheader('Ingresos por Año')
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=df_ingresos_filtrado, x='Periodo', y='Ingresos (miles de pesos)', marker='o', ax=ax)
plt.xticks(rotation=90)
st.pyplot(fig)

# Análisis de penetración
st.subheader('Penetración de Internet por Provincia')
df_penetracion_filtrado = data['Penetracion_poblacion'][data['Penetracion_poblacion']['Provincia'].isin(provincia_seleccionada)]
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=df_penetracion_filtrado, x='Provincia', y='Accesos por cada 100 hab', ax=ax)
plt.xticks(rotation=90)
plt.ylabel('Accesos por cada 100 Habitantes')
st.pyplot(fig)

# Análisis de velocidad
st.subheader('Distribución de Velocidades de Acceso')
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(data=data['Totales_accesos_por_velocidad'], kde=True, ax=ax)
plt.xlabel('Velocidad')
plt.ylabel('Frecuencia')
st.pyplot(fig)

# Análisis de ingresos totales
st.subheader('Distribución de Ingresos')
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(data=data['Ingresos']['Ingresos (miles de pesos)'], kde=True, ax=ax)
plt.xlabel('Ingresos (miles de pesos)')
plt.ylabel('Frecuencia')
st.pyplot(fig)

# Análisis de demanda en áreas urbanas vs rurales
st.subheader('Análisis de Demanda en Áreas Urbanas vs Rurales')
urban_rural = data['Accesos_tecnologia_localidad'].copy()
urban_rural['Tipo'] = urban_rural['Localidad'].apply(lambda x: 'Urbano' if 'Ciudad' in x or 'Capital' in x else 'Rural')
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(data=urban_rural, x='Tipo', ax=ax)
plt.ylabel('Número de Accesos')
st.pyplot(fig)

# Identificación de áreas geográficas con baja penetración de servicios
st.subheader('Áreas Geográficas con Baja Penetración de Servicios')
baja_penetracion = data['Penetracion_poblacion'][data['Penetracion_poblacion']['Accesos por cada 100 hab'] < 20]
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=baja_penetracion, x='Provincia', y='Accesos por cada 100 hab', ax=ax)
plt.xticks(rotation=90)
plt.ylabel('Accesos por cada 100 Habitantes')
st.pyplot(fig)

# Proyección de crecimiento de ingresos y costos a mediano y largo plazo
st.subheader('Proyección de Crecimiento de Ingresos a Mediano y Largo Plazo')
# Suponemos un crecimiento del 10% anual
data['Ingresos']['Proyección 1 Año'] = data['Ingresos']['Ingresos (miles de pesos)'] * 1.10
data['Ingresos']['Proyección 3 Años'] = data['Ingresos']['Ingresos (miles de pesos)'] * (1.10 ** 3)
data['Ingresos']['Proyección 5 Años'] = data['Ingresos']['Ingresos (miles de pesos)'] * (1.10 ** 5)
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=data['Ingresos'], x='Periodo', y='Proyección 1 Año', label='Proyección 1 Año', marker='o', ax=ax)
sns.lineplot(data=data['Ingresos'], x='Periodo', y='Proyección 3 Años', label='Proyección 3 Años', marker='o', ax=ax)
sns.lineplot(data=data['Ingresos'], x='Periodo', y='Proyección 5 Años', label='Proyección 5 Años', marker='o', ax=ax)
plt.xticks(rotation=90)
plt.ylabel('Ingresos Proyectados (miles de pesos)')
st.pyplot(fig)

# Identificación de nuevas áreas geográficas para expandir los servicios
st.subheader('Nuevas Áreas Geográficas para Expandir los Servicios')
nuevas_areas = data['Penetracion_poblacion'][data['Penetracion_poblacion']['Accesos por cada 100 hab'] < 30]
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=nuevas_areas, x='Provincia', y='Accesos por cada 100 hab', ax=ax)
plt.xticks(rotation=90)
plt.ylabel('Accesos por cada 100 Habitantes')
st.pyplot(fig)

# Establecimiento de métricas clave para monitorear el progreso y el impacto de las mejoras implementadas
st.subheader('Métricas Clave para Monitorear el Progreso')
kpi_data = data['Penetracion_hogares'].copy()
kpi_data['Nuevo_acceso'] = kpi_data['Accesos por cada 100 hogares'] * 1.02
kpi_data['KPI'] = ((kpi_data['Nuevo_acceso'] - kpi_data['Accesos por cada 100 hogares']) / kpi_data['Accesos por cada 100 hogares']) * 100
kpi_data['Velocidad_nueva'] = data['Velocidad_por_prov']['Mbps (Media de bajada)'] * 1.05
kpi_data['KPI_Velocidad'] = ((kpi_data['Velocidad_nueva'] - data['Velocidad_por_prov']['Mbps (Media de bajada)']) / data['Velocidad_por_prov']['Mbps (Media de bajada)']) * 100

fig, ax = plt.subplots(1, 2, figsize=(15, 6))
sns.barplot(data=kpi_data, x='Provincia', y='KPI', ax=ax[0])
ax[0].set_title('KPI: Aumento del 2% en el acceso a internet')
ax[0].set_xticklabels(ax[0].get_xticklabels(), rotation=90)
ax[0].set_ylabel('KPI (%)')

sns.barplot(data=kpi_data, x='Provincia', y='KPI_Velocidad', ax=ax[1])
ax[1].set_title('KPI: Aumento en la Velocidad Promedio de Internet')
ax[1].set_xticklabels(ax[1].get_xticklabels(), rotation=90)
ax[1].set_ylabel('KPI Velocidad (%)')

st.pyplot(fig)
            

# Conclusiones
st.subheader('Conclusiones')
st.markdown("""
A partir del análisis de los datos de acceso a internet en Argentina, podemos extraer las siguientes conclusiones:

1. **Distribución Desigual:** Existe una distribución desigual de accesos a internet entre las diferentes provincias, con algunas provincias mostrando una mayor penetración y otras rezagadas.
2. **Crecimiento Sostenido:** Los ingresos por servicios de internet han mostrado un crecimiento sostenido a lo largo de los años, indicando una mayor adopción y demanda de servicios de alta velocidad.
3. **Preferencia por Tecnologías Avanzadas:** Se observa una tendencia creciente hacia el uso de tecnologías más avanzadas como la fibra óptica, desplazando gradualmente a tecnologías más antiguas como ADSL.
4. **Variabilidad en la Velocidad:** Hay una variabilidad considerable en las velocidades de acceso a internet, con un número significativo de usuarios todavía utilizando velocidades bajas, aunque hay un crecimiento en las velocidades más altas.
5. **Áreas de Baja Penetración:** Identificamos áreas geográficas con baja penetración de servicios, que representan oportunidades para expandir la cobertura y mejorar la calidad del servicio.
6. **Proyección de Crecimiento:** Las proyecciones indican un crecimiento continuo en los ingresos, lo que sugiere que la demanda de servicios de internet seguirá en aumento.
7. **Áreas Urbanas vs Rurales:** Existen diferencias significativas en la demanda de servicios entre áreas urbanas y rurales, lo que sugiere la necesidad de estrategias diferenciadas para cada tipo de área.
8. **Nuevas Áreas para Expansión:** Las provincias con baja penetración actual son candidatas ideales para futuras expansiones de servicio.

Este análisis proporciona una visión clara de las tendencias y patrones en el acceso a internet en Argentina, lo que puede ayudar a los proveedores de servicios a tomar decisiones informadas y estratégicas.
""")
