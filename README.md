# Dashboard de Análisis de Datos con Streamlit y Gitflow

## Descripción

Este proyecto presenta una aplicación web desarrollada con Streamlit para el análisis exploratorio del archivo `penguins.csv`.

La aplicación permite cargar datos, validar archivos CSV, visualizar métricas generales, generar gráficos interactivos y consultar registros en una tabla dinámica.

## Objetivo

Aplicar el flujo de trabajo Gitflow durante el desarrollo de una aplicación de análisis de datos, separando cada funcionalidad en ramas independientes y publicando una versión estable mediante una rama de release y un tag de versión.

## Funcionalidades principales

- Validación de archivos CSV.
- Carga del dataset `penguins.csv`.
- Visualización de métricas generales.
- Generación de gráficos interactivos.
- Visualización tabular de registros.
- Pruebas unitarias con pytest.

## Tecnologías utilizadas

- Python
- Streamlit
- Pandas
- Plotly
- Pytest
- Git
- GitHub
- Gitflow

## Estructura del proyecto

```txt
streamlit-gitflow-penguins/
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── penguins.csv
├── src/
│   ├── __init__.py
│   └── data_utils.py
├── tests/
│   └── test_data_utils.py
└── docs/
    └── informe.md
