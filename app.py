import streamlit as st
import plotly.express as px

from src.data_utils import (
    validar_extension_csv,
    cargar_csv,
    cargar_csv_local,
    obtener_columnas_numericas,
    obtener_columnas_categoricas,
    filtrar_registros,
)


st.set_page_config(
    page_title="Dashboard Penguins",
    page_icon="🐧",
    layout="wide"
)

st.title("Dashboard de Análisis de Datos - Penguins")

st.write(
    "Aplicación desarrollada con Streamlit para cargar, validar, analizar "
    "y visualizar información del dataset penguins.csv."
)

st.sidebar.header("Carga de datos")

opcion_carga = st.sidebar.radio(
    "Seleccione el origen de datos",
    ["Archivo local del proyecto", "Subir archivo CSV"]
)

try:
    if opcion_carga == "Archivo local del proyecto":
        df = cargar_csv_local("data/penguins.csv")
        st.sidebar.success("Archivo data/penguins.csv cargado correctamente.")
    else:
        archivo = st.sidebar.file_uploader(
            "Seleccione el archivo penguins.csv",
            type=["csv"]
        )

        if archivo is None:
            st.info("Por favor, cargue el archivo penguins.csv para iniciar.")
            st.stop()

        if not validar_extension_csv(archivo.name):
            st.error("El archivo debe tener extensión .csv.")
            st.stop()

        df = cargar_csv(archivo)
        st.sidebar.success("Archivo cargado correctamente.")

except Exception as error:
    st.error(f"No se pudo cargar el archivo: {error}")
    st.stop()


st.header("Resumen general del dataset")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Número de filas", df.shape[0])

with col2:
    st.metric("Número de columnas", df.shape[1])

with col3:
    st.metric("Datos nulos", int(df.isnull().sum().sum()))


st.subheader("Vista previa de datos")
st.dataframe(df.head(10), use_container_width=True)


columnas_numericas = obtener_columnas_numericas(df)
columnas_categoricas = obtener_columnas_categoricas(df)


st.divider()
st.header("Visualizaciones principales")

if columnas_categoricas:
    columna_categoria = st.selectbox(
        "Seleccione una columna categórica",
        columnas_categoricas
    )

    conteo = df[columna_categoria].value_counts().reset_index()
    conteo.columns = [columna_categoria, "cantidad"]

    fig_bar = px.bar(
        conteo,
        x=columna_categoria,
        y="cantidad",
        title=f"Distribución por {columna_categoria}"
    )

    st.plotly_chart(fig_bar, use_container_width=True)


if len(columnas_numericas) >= 2:
    eje_x = st.selectbox("Seleccione el eje X", columnas_numericas)
    eje_y = st.selectbox("Seleccione el eje Y", columnas_numericas)

    color = columnas_categoricas[0] if columnas_categoricas else None

    fig_scatter = px.scatter(
        df,
        x=eje_x,
        y=eje_y,
        color=color,
        title=f"Relación entre {eje_x} y {eje_y}"
    )

    st.plotly_chart(fig_scatter, use_container_width=True)
else:
    st.warning("No existen suficientes columnas numéricas para generar gráficos.")


st.divider()
st.header("Visualización tabular de datos")

cantidad = st.number_input(
    "Seleccione la cantidad de registros a visualizar",
    min_value=1,
    max_value=len(df),
    value=min(10, len(df))
)

posicion = st.radio(
    "Seleccione desde dónde desea visualizar los datos",
    ["Inicio", "Final"],
    horizontal=True
)

try:
    df_filtrado = filtrar_registros(df, cantidad, posicion)
    st.dataframe(df_filtrado, use_container_width=True)
except ValueError as error:
    st.error(str(error))
