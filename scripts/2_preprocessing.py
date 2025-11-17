"""Rotinas de preparação de dados para o dataset de obesidade."""

from __future__ import annotations

from pathlib import Path
from typing import List

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import (
    LabelEncoder,
    OneHotEncoder,
    OrdinalEncoder,
    StandardScaler,
)

# Definições alinhadas com a etapa de EDA
TARGET_COLUMN = "Obesity"
NUMERIC_FEATURES: List[str] = [
    "Age",
    "Height",
    "Weight",
    "FCVC",
    "NCP",
    "CH2O",
    "FAF",
    "TUE",
]
CATEGORICAL_FEATURES: List[str] = [
    "Gender",
    "family_history",
    "FAVC",
    "SMOKE",
    "SCC",
    "MTRANS",
]
ORDINAL_FEATURES: List[str] = ["CAEC", "CALC"]
ORDINAL_ORDER = ["no", "Sometimes", "Frequently", "Always"]
BMI_COLUMN = "BMI"


def carregar_dados(caminho: Path) -> pd.DataFrame:
    """Carrega o dataset, remove duplicatas e retorna um DataFrame.

    Args:
        caminho: Caminho completo para o arquivo CSV.

    Returns:
        DataFrame com o conteúdo do CSV e duplicatas removidas.

    Raises:
        FileNotFoundError: Caso o caminho informado não exista.
    """
    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    df = pd.read_csv(caminho)
    df.drop_duplicates(inplace=True)
    return df


def criar_bmi(df: pd.DataFrame) -> pd.DataFrame:
    """Cria a coluna de IMC (BMI) a partir de peso e altura.

    Args:
        df: DataFrame original.

    Returns:
        Novo DataFrame contendo a coluna BMI.
    """
    resultado = df.copy()
    altura = resultado["Height"].replace({0: np.nan})
    resultado[BMI_COLUMN] = resultado["Weight"] / (altura**2)
    return resultado


def obter_preprocessor() -> ColumnTransformer:
    """Instancia o pré-processador de features em um ColumnTransformer.

    Returns:
        ColumnTransformer com pipelines para variáveis numéricas,
        categóricas nominais e categóricas ordinais.
    """
    numeric_pipeline = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
        ]
    )

    ordinal_pipeline = Pipeline(
        steps=[
            (
                "ordinal_encoder",
                OrdinalEncoder(
                    categories=[ORDINAL_ORDER, ORDINAL_ORDER],
                    handle_unknown="use_encoded_value",
                    unknown_value=-1,
                ),
            )
        ]
    )

    categorical_pipeline = Pipeline(
        steps=[
            (
                "onehot",
                OneHotEncoder(
                    drop="first",
                    handle_unknown="ignore",
                    sparse_output=False,
                ),
            )
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "numeric",
                numeric_pipeline,
                NUMERIC_FEATURES + [BMI_COLUMN],
            ),
            (
                "ordinal",
                ordinal_pipeline,
                ORDINAL_FEATURES,
            ),
            (
                "categorical",
                categorical_pipeline,
                CATEGORICAL_FEATURES,
            ),
        ],
        remainder="drop",
    )
    return preprocessor


def obter_target_encoder() -> LabelEncoder:
    """Retorna o codificador para a variável alvo.

    Returns:
        Instância de LabelEncoder.
    """
    return LabelEncoder()


__all__ = [
    "TARGET_COLUMN",
    "NUMERIC_FEATURES",
    "CATEGORICAL_FEATURES",
    "ORDINAL_FEATURES",
    "carregar_dados",
    "criar_bmi",
    "obter_preprocessor",
    "obter_target_encoder",
]

