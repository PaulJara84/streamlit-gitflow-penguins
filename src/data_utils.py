import pandas as pd


def validar_extension_csv(nombre_archivo: str) -> bool:
    if not nombre_archivo:
        return False

    return nombre_archivo.lower().endswith(".csv")


def cargar_csv(archivo):
    codificaciones = ["utf-8", "utf-8-sig", "latin1", "cp1252"]

    for encoding in codificaciones:
        try:
            df = pd.read_csv(archivo, encoding=encoding)

            if df.empty:
                raise ValueError("El archivo CSV está vacío.")

            return df

        except UnicodeDecodeError:
            archivo.seek(0)
            continue

        except pd.errors.EmptyDataError:
            raise ValueError("El archivo CSV no contiene datos.")

        except pd.errors.ParserError:
            raise ValueError("El archivo CSV tiene un formato inválido.")

    raise ValueError("No se pudo leer el archivo CSV.")


def cargar_csv_local(ruta: str):
    df = pd.read_csv(ruta)

    if df.empty:
        raise ValueError("El archivo CSV está vacío.")

    return df


def obtener_columnas_numericas(df: pd.DataFrame):
    return df.select_dtypes(include=["number"]).columns.tolist()


def obtener_columnas_categoricas(df: pd.DataFrame):
    return df.select_dtypes(include=["object", "category"]).columns.tolist()


def filtrar_registros(df: pd.DataFrame, cantidad: int, posicion: str):
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor que cero.")

    if posicion == "Inicio":
        return df.head(cantidad)

    if posicion == "Final":
        return df.tail(cantidad)

    raise ValueError("La posición seleccionada no es válida.")
