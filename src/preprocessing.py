#Importando as bibliotecas para pre processamento
import pandas as pd
import numpy as np

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

#Iniciando o pre processamento:


def make_preprocessor(X_data):
    #Separarando colunas
    num_features = X_data.select_dtypes(include=["int64", "float64"]).columns
    cat_features = X_data.select_dtypes(include=["object"]).columns

    #Criando os Pipelines de Transformação
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    # 3Juntando tudo no ColumnTransformer
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, num_features),
            ('cat', categorical_transformer, cat_features)
        ]
    )

    return preprocessor