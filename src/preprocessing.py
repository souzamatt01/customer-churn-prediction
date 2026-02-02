#Importando as bibliotecas para pre processamento
import pandas as pd
import numpy as np

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

#Iniciando o pre processamento:

#Separando colunas numéricas e categóricas  
num_features = X.select_dtypes(include=["int64", "float64"]).columns
cat_features = X.select_dtypes(include=["object"]).columns

#Aplicando o Transformer para colunas numéricas
numeric_transformer = Pipeline(steps=[
    ('scaler',StandardScaler())
])

#Aplicando o Transformer para colunas categóricas
categorical_transformer = Pipeline(steps=[
   ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

#Aplicando o ColumnTransformer para unir os dois transformers
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, num_features),
        ('cat', categorical_transformer, cat_features)
    ])

#Ajustando o preprocessor aos dados