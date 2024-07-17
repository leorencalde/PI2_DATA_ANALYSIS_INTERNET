# Análisis de Servicios de Telecomunicaciones 💻📞📡

## Descripción del Proyecto

Este proyecto se centra en el análisis detallado de los servicios de telecomunicaciones en Argentina, con un énfasis particular en el acceso a internet. Utilizando una variedad de técnicas de análisis de datos y visualización, el objetivo es identificar patrones y tendencias que puedan ayudar a la empresa prestadora de servicios a mejorar su oferta y a identificar oportunidades de expansión y mejora.

## Estructura del Repositorio

- `EDA.ipynb`: Notebook de Jupyter con el Análisis Exploratorio de Datos (EDA) completo, incluyendo la identificación de valores atípicos, análisis geoespacial y visualizaciones detalladas.
- `dashboard.py`: Archivo de Streamlit para generar un dashboard interactivo que permite explorar los datos detalladamente con varios filtros.
- `datasets/`: Carpeta que contiene los archivos de datos utilizados en el análisis.
  - `internet.xlsx`: Archivo de Excel con los datos sobre acceso a internet por provincia y tecnología.
  - `mapa_conectividad.xlsx`: Archivo de Excel con los datos geoespaciales para el mapa de conectividad.
- `run_streamlit.py`: Script para ejecutar el dashboard de Streamlit.
- `requirements.txt`: Lista de dependencias necesarias para ejecutar el proyecto.

## Ejecutar el Dashboard de Streamlit

El Dashboard ha sido desplegado utilizando Streamlit Cloud. Puedes acceder en el siguiente enlace:

https://mlops-movies-leonardorenteria.onrender.com/docs

## Descripción del Dashboard

El dashboard permite a los usuarios explorar los datos de acceso a internet por provincia y tecnología a través de gráficos interactivos. Las principales funcionalidades incluyen:

- Filtros por año, trimestre y tecnología.
- Análisis de demanda en áreas urbanas vs. rurales.
- Identificación de áreas geográficas con baja penetración de servicios.
- Proyección de crecimiento de ingresos y costos.
- Identificación de nuevas áreas geográficas para expandir los servicios.
- Establecimiento de métricas clave para monitorear el progreso y el impacto de las mejoras implementadas.

### KPIs Propuestos

KPI 1: Aumento en el Acceso a Internet
Fórmula:
KPI = ((Nuevo acceso - Acceso actual) / Acceso actual) * 100
Objetivo: Aumentar en un 2% el acceso al servicio de internet para el próximo trimestre, cada 100 hogares, por provincia.

KPI 2: Crecimiento de Ingresos
Fórmula:
KPI = (Ingresos actuales - Ingresos del periodo anterior) / Ingresos del periodo anterior * 100
Objetivo: Medir el crecimiento de ingresos generado por los servicios de internet.

KPI 3: Penetración del Servicio
Fórmula: 
KPI = (Accesos totales / Población total) * 100
Objetivo: Medir la penetración del servicio de internet en relación a la población total.

## Análisis y Conclusiones

### Análisis Exploratorio de Datos

Se identificaron valores atípicos en varias categorías de datos, lo que indica variabilidad en el acceso a internet en diferentes provincias y tecnologías. Esto es crucial para focalizar recursos y esfuerzos en las áreas que más lo necesitan.

### Análisis Geoespacial

El análisis geoespacial mostró una distribución desigual del acceso a internet en las provincias de Argentina. Las provincias del norte y algunas del sur tienen una menor penetración de servicios de internet, lo que representa una oportunidad de expansión para la empresa.

### Proyección de Ingresos

El análisis de ingresos mostró una tendencia creciente en los ingresos generados por servicios de internet, lo que sugiere un mercado en expansión y la necesidad de mejorar la infraestructura para mantener y potenciar este crecimiento.

## Cómo Ejecutar el Proyecto

### Prerrequisitos

1. Python 3.x
2. Jupyter Notebook
3. Streamlit
4. Bibliotecas listadas en `requirements.txt`

### Instalación

1. Clonar este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio

2. Crear un entorno virtual y activarlo:
   ```bash
   python -m venv venv
   source venv/bin/activate   # En Windows, usar: venv\Scripts\activate

3. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
