import pandas as pd
import pytest

from src.data_utils import (
    validar_extension_csv,
    obtener_columnas_numericas,
    obtener_columnas_categoricas,
    filtrar_registros,
)


@pytest.fixture
def penguins_df():
    return pd.DataFrame({
        "species": ["Adelie", "Adelie", "Gentoo", "Chinstrap", "Gentoo"],
        "island": ["Torgersen", "Torgersen", "Biscoe", "Dream", "Biscoe"],
        "bill_length_mm": [39.1, 39.5, 46.1, 50.0, 45.2],
        "bill_depth_mm": [18.7, 17.4, 13.2, 19.5, 14.8],
        "flipper_length_mm": [181, 186, 211, 196, 212],
        "body_mass_g": [3750, 3800, 4500, 3900, 5200],
        "sex": ["male", "female", "female", "male", "female"],
        "year": [2007, 2007, 2008, 2009, 2009],
    })


def test_validar_extension_csv_correcta():
    assert validar_extension_csv("penguins.csv") is True


def test_validar_extension_csv_mayuscula():
    assert validar_extension_csv("penguins.CSV") is True


def test_validar_extension_csv_incorrecta():
    assert validar_extension_csv("penguins.xlsx") is False


def test_columnas_numericas_penguins(penguins_df):
    columnas = obtener_columnas_numericas(penguins_df)

    assert "bill_length_mm" in columnas
    assert "bill_depth_mm" in columnas
    assert "flipper_length_mm" in columnas
    assert "body_mass_g" in columnas
    assert "year" in columnas
    assert "species" not in columnas


def test_columnas_categoricas_penguins(penguins_df):
    columnas = obtener_columnas_categoricas(penguins_df)

    assert "species" in columnas
    assert "island" in columnas
    assert "sex" in columnas
    assert "body_mass_g" not in columnas


def test_filtrar_registros_inicio_penguins(penguins_df):
    resultado = filtrar_registros(penguins_df, 2, "Inicio")

    assert len(resultado) == 2
    assert resultado.iloc[0]["species"] == "Adelie"


def test_filtrar_registros_final_penguins(penguins_df):
    resultado = filtrar_registros(penguins_df, 2, "Final")

    assert len(resultado) == 2
    assert resultado.iloc[0]["species"] == "Chinstrap"
    assert resultado.iloc[1]["species"] == "Gentoo"


def test_filtrar_registros_cantidad_invalida(penguins_df):
    with pytest.raises(ValueError):
        filtrar_registros(penguins_df, 0, "Inicio")


def test_filtrar_registros_posicion_invalida(penguins_df):
    with pytest.raises(ValueError):
        filtrar_registros(penguins_df, 3, "Centro")
