# Informe de Desarrollo - Aplicación Streamlit con Gitflow

## 1. Integrantes

- Giovanni Baño
- Paul Jara

## 2. Descripción del proyecto

El proyecto consiste en una aplicación web desarrollada con Streamlit para analizar el dataset `penguins.csv`. La aplicación permite cargar datos, validar archivos CSV, visualizar métricas generales, generar gráficos interactivos y mostrar registros en una tabla.

## 3. Objetivo

Aplicar Gitflow como estrategia de control de versiones durante el desarrollo de una aplicación Streamlit, separando el trabajo por funcionalidades, integrando los cambios en `develop` y publicando una versión estable en `main`.

## 4. Estructura del proyecto

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
    ├── informe.md
    └── img/
