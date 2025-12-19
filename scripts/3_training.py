"""Pipeline de treinamento do modelo de classificação de obesidade.

Este script implementa o treinamento completo do modelo preditivo,
incluindo validação cruzada, métricas de performance e serialização
dos artefatos para deploy.

FASE 3 do Tech Challenge 4 - FIAP/POSTECH Data Analytics
"""

from __future__ import annotations

import pickle
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split

# Adiciona o diretório raiz ao path para importar o módulo de preprocessing
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))


# Renomeia módulo para importação (Python não permite imports com números no início)
import importlib.util
spec = importlib.util.spec_from_file_location("preprocessing", PROJECT_ROOT / "scripts" / "2_preprocessing.py")
preprocessing_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(preprocessing_module)

TARGET_COLUMN = preprocessing_module.TARGET_COLUMN
carregar_dados = preprocessing_module.carregar_dados
criar_bmi = preprocessing_module.criar_bmi
obter_preprocessor = preprocessing_module.obter_preprocessor
obter_target_encoder = preprocessing_module.obter_target_encoder

# Configurações
DATA_PATH = PROJECT_ROOT / "data" / "Obesity.csv"
MODEL_PATH = PROJECT_ROOT / "modelo.pkl"
ENCODER_PATH = PROJECT_ROOT / "label_encoder.pkl"
RANDOM_STATE = 42
TEST_SIZE = 0.2
N_FOLDS = 5


def preparar_dados() -> tuple[pd.DataFrame, pd.Series]:
    """Carrega e prepara os dados para treinamento.

    Returns:
        Tupla com DataFrame de features e Series do target.
    """
    print("=" * 60)
    print("FASE 3: TREINAMENTO DO MODELO DE CLASSIFICAÇÃO DE OBESIDADE")
    print("=" * 60)
    print("\n[1/5] Carregando dados...")

    df = carregar_dados(DATA_PATH)
    print(f"     - Registros carregados: {len(df)}")

    df = criar_bmi(df)
    print("     - Feature BMI criada")

    X = df.drop(columns=[TARGET_COLUMN])
    y = df[TARGET_COLUMN]
    print(f"     - Features: {X.shape[1]} | Target: {TARGET_COLUMN}")

    return X, y


def treinar_modelo(
    X: pd.DataFrame, y: pd.Series
) -> tuple[RandomForestClassifier, object, object]:
    """Treina o modelo com validação cruzada.

    Args:
        X: DataFrame com features.
        y: Series com target.

    Returns:
        Tupla com modelo treinado, preprocessor e label_encoder.
    """
    print("\n[2/5] Preparando pipeline de pré-processamento...")

    # Encoder para o target
    label_encoder = obter_target_encoder()
    y_encoded = label_encoder.fit_transform(y)
    print(f"     - Classes: {list(label_encoder.classes_)}")

    # Split estratificado
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y_encoded
    )
    print(f"     - Treino: {len(X_train)} | Teste: {len(X_test)}")

    # Preprocessor
    preprocessor = obter_preprocessor()
    X_train_processed = preprocessor.fit_transform(X_train)
    X_test_processed = preprocessor.transform(X_test)
    print(f"     - Features após preprocessing: {X_train_processed.shape[1]}")

    # Modelo
    print("\n[3/5] Treinando RandomForestClassifier...")
    modelo = RandomForestClassifier(
        n_estimators=200,
        max_depth=20,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=RANDOM_STATE,
        n_jobs=-1,
        class_weight="balanced",
    )

    # Validação cruzada
    print("\n[4/5] Validação cruzada (5-fold)...")
    cv = StratifiedKFold(n_splits=N_FOLDS, shuffle=True, random_state=RANDOM_STATE)
    cv_scores = cross_val_score(modelo, X_train_processed, y_train, cv=cv, scoring="accuracy")
    print(f"     - Scores por fold: {[f'{s:.4f}' for s in cv_scores]}")
    print(f"     - Acurácia CV média: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")

    # Treinamento final
    modelo.fit(X_train_processed, y_train)

    # Avaliação no conjunto de teste
    y_pred = modelo.predict(X_test_processed)
    acc_test = accuracy_score(y_test, y_pred)

    print("\n" + "=" * 60)
    print("MÉTRICAS NO CONJUNTO DE TESTE")
    print("=" * 60)
    print(f"\n>>> ACURÁCIA: {acc_test:.4f} ({acc_test * 100:.2f}%) <<<")

    if acc_test >= 0.75:
        print("✅ Meta de 75% ATINGIDA!")
    else:
        print("⚠️ Meta de 75% NÃO atingida - considere ajustar hiperparâmetros")

    print("\nRelatório de Classificação:")
    print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))

    print("Matriz de Confusão:")
    cm = confusion_matrix(y_test, y_pred)
    print(cm)

    # Retornar pipeline completo para serialização
    from sklearn.pipeline import Pipeline

    pipeline_completo = Pipeline([
        ("preprocessor", preprocessor),
        ("classifier", modelo),
    ])

    return pipeline_completo, label_encoder, acc_test


def salvar_artefatos(pipeline: object, label_encoder: object) -> None:
    """Serializa modelo e encoder para arquivos pickle.

    Args:
        pipeline: Pipeline completo (preprocessor + modelo).
        label_encoder: LabelEncoder do target.
    """
    print("\n[5/5] Salvando artefatos...")

    with open(MODEL_PATH, "wb") as f:
        pickle.dump(pipeline, f)
    print(f"     - Modelo salvo: {MODEL_PATH}")

    with open(ENCODER_PATH, "wb") as f:
        pickle.dump(label_encoder, f)
    print(f"     - Encoder salvo: {ENCODER_PATH}")


def main() -> None:
    """Executa o pipeline completo de treinamento."""
    X, y = preparar_dados()
    pipeline, label_encoder, acc = treinar_modelo(X, y)
    salvar_artefatos(pipeline, label_encoder)

    print("\n" + "=" * 60)
    print("TREINAMENTO CONCLUÍDO COM SUCESSO!")
    print(f"Acurácia final: {acc * 100:.2f}%")
    print("=" * 60)


if __name__ == "__main__":
    main()
