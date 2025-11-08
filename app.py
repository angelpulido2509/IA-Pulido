import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Importaciones de Machine Learning
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.datasets import make_classification
import xgboost as xgb
import lightgbm as lgb
from catboost import CatBoostClassifier
# Nota: La optimización (GridSearch, BayesSearch) es demasiado lenta para una app, la omitimos o usamos hiperparámetros fijos.

# --- Configuración de la Página ---
st.set_page_config(
    page_title="Guía Práctica de Boosting (XGB, LGBM, Cat)",
    layout="wide"
)

st.title("💡 Guía Práctica de Boosting con Python")
st.markdown("---")

# --- PASO 1: Creación y Carga de Datos (Usamos @st.cache para velocidad) ---

@st.cache_data
def crear_dataset_ejemplo(n_samples, n_features):
    """Crea el dataset sintético de la guía."""
    X, y = make_classification(
        n_samples=n_samples,
        n_features=n_features,
        n_informative=int(n_features * 0.75),
        n_redundant=int(n_features * 0.25),
        random_state=42
    )
    feature_names = [f'feature_{i}' for i in range(n_features)]
    df = pd.DataFrame(X, columns=feature_names)
    
    # Agregar categóricas para CatBoost
    df['categoria_1'] = np.random.choice([0, 1, 2], size=n_samples)
    df['categoria_2'] = np.random.choice([0, 1], size=n_samples)
    
    X_train, X_test, y_train, y_test = train_test_split(
        df, y, test_size=0.2, random_state=42, stratify=y
    )
    return X_train, X_test, y_train, y_test

# --- PASO 2: Entrenar y Evaluar Modelos ---

@st.cache_resource
def entrenar_modelo(modelo_nombre, X_train, y_train, params):
    """Función para entrenar el modelo seleccionado."""
    if modelo_nombre == 'XGBoost':
        model = xgb.XGBClassifier(**params, use_label_encoder=False, eval_metric='logloss', random_state=42)
    elif modelo_nombre == 'LightGBM':
        model = lgb.LGBMClassifier(**params, random_state=42)
    else: # CatBoost
        # CatBoost es más lento, reducimos iteraciones
        model = CatBoostClassifier(**params, cat_features=['categoria_1', 'categoria_2'], verbose=0, random_state=42)
        
    model.fit(X_train, y_train)
    return model

def evaluar_modelo(model, X_test, y_test, X_train, y_train, nombre):
    """Muestra la evaluación y CV del modelo."""
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    st.subheader(f"Resultados de {nombre}")
    col1, col2 = st.columns(2)
    
    # Métrica principal
    with col1:
        st.metric(label="Precisión (Accuracy) en Prueba", value=f"{accuracy:.4f}")
        
    # Validación Cruzada
    with col2:
        cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
        st.metric(label="CV Score (Promedio 5-fold)", value=f"{cv_scores.mean():.4f}", delta=f"Std Dev: {cv_scores.std():.4f}")
        
    # Matriz de Confusión
    st.write("#### Matriz de Confusión")
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
    ax.set_xlabel('Predicción')
    ax.set_ylabel('Real')
    st.pyplot(fig)


# --- Interfaz de Streamlit ---

# Sidebar para control de datos
st.sidebar.header("Control de Datos")
n_samples = st.sidebar.slider("Número de Muestras", 100, 5000, 1000)
n_features = st.sidebar.slider("Número de Características", 10, 50, 20)
X_train, X_test, y_train, y_test = crear_dataset_ejemplo(n_samples, n_features)

st.sidebar.info(f"Datos Cargados:\nEntrenamiento: {X_train.shape}\nPrueba: {X_test.shape}")

# Pestañas principales
tab_xgb, tab_lgbm, tab_cat, tab_comp = st.tabs(["XGBoost", "LightGBM", "CatBoost", "Comparación Final"])

# --- Pestaña de XGBoost ---
with tab_xgb:
    st.header("Análisis de XGBoost")
    st.markdown("Ajusta los hiperparámetros y entrena el modelo.")
    
    # Parámetros controlados por widgets
    max_depth_xgb = st.slider("Max Depth", 3, 15, 6, key='d_xgb')
    n_estimators_xgb = st.slider("N Estimators", 50, 500, 100, key='n_xgb')
    learning_rate_xgb = st.slider("Learning Rate", 0.01, 0.3, 0.1, 0.01, key='lr_xgb')
    
    if st.button("Entrenar XGBoost"):
        params_xgb = {
            'max_depth': max_depth_xgb,
            'n_estimators': n_estimators_xgb,
            'learning_rate': learning_rate_xgb
        }
        modelo_xgb = entrenar_modelo('XGBoost', X_train, y_train, params_xgb)
        evaluar_modelo(modelo_xgb, X_test, y_test, X_train, y_train, "XGBoost")

# ... Puedes replicar las pestañas para LightGBM y CatBoost de manera similar ...

# --- Pestaña de Comparación Final ---
with tab_comp:
    st.header("Comparación General (Implementación Básica)")
    
    if st.button("Ejecutar Comparación"):
        modelos = {
            'XGBoost': xgb.XGBClassifier(n_estimators=100, random_state=42, use_label_encoder=False, eval_metric='logloss'),
            'LightGBM': lgb.LGBMClassifier(n_estimators=100, random_state=42),
            'CatBoost': CatBoostClassifier(n_estimators=100, cat_features=['categoria_1', 'categoria_2'], verbose=0, random_state=42)
        }
        
        resultados = []
        with st.spinner("Entrenando 3 modelos..."):
            for nombre, modelo in modelos.items():
                modelo.fit(X_train, y_train)
                y_pred = modelo.predict(X_test)
                acc = accuracy_score(y_test, y_pred)
                cv_mean = cross_val_score(modelo, X_train, y_train, cv=3, scoring='accuracy').mean()
                resultados.append({'Modelo': nombre, 'Accuracy': f"{acc:.4f}", 'CV Mean': f"{cv_mean:.4f}"})
        
        df_resultados = pd.DataFrame(resultados)
        st.dataframe(df_resultados)
        
        fig, ax = plt.subplots()
        df_resultados.set_index('Modelo')['Accuracy'].astype(float).plot(kind='bar', ax=ax)
        ax.set_ylabel("Accuracy")
        st.pyplot(fig)