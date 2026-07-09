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

## 5. Procedimiento realizado
## 5.1 Creación del repositorio

Se creó un repositorio en GitHub para alojar el código fuente del proyecto. Posteriormente, se configuraron las ramas main y develop como base del flujo Gitflow.

## 5.2 Implementación de funciones de validación

Se creó la rama feature/validaciones, donde se implementaron funciones para validar archivos CSV, cargar datos, obtener columnas numéricas, obtener columnas categóricas y filtrar registros.

## 5.3 Desarrollo de la aplicación principal

Se creó la rama feature/app-principal, donde se implementó la aplicación principal con Streamlit. Esta sección permite cargar el dataset, mostrar métricas generales y generar gráficos interactivos.

## 5.4 Visualización tabular de datos

Se incorporó una sección que permite consultar registros desde el inicio o desde el final del dataset, indicando la cantidad de filas que se desea visualizar.

## 5.5 Pruebas con pytest

Se creó la rama feature/pruebas-pytest, donde se implementaron pruebas unitarias para validar el funcionamiento de las funciones auxiliares.

## 5.6 Release de la aplicación

Se creó la rama release/v1.0.0 desde develop. Luego, esta versión fue integrada en main y etiquetada con el tag v1.0.0.

## 6. Ramas utilizadas
main
develop
feature/validaciones
feature/app-principal
feature/pruebas-pytest
release/v1.0.0

##7. Evidencia de ramas y tags

## 8. Conclusiones
 1.- Gitflow permitió separar el desarrollo por funcionalidades, reduciendo el riesgo de modificar directamente la versión estable del proyecto.
 2.- La rama develop sirvió como punto de integración para validar los cambios antes de enviarlos a main.
 3.- El uso de una rama release y un tag de versión permitió identificar de forma clara la versión final entregable de la aplicación.
