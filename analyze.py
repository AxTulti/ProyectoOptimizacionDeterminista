import pandas as pd
import numpy as np

def calculate_descriptive_stats(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Calcula n, media (x̄) y desviación estándar (σ) para una lista de columnas,
    segmentado por género.
    """
    try:
        stats_list = []
        
        # Asegurar que las columnas sean numéricas para poder calcular media y varianza
        df_numeric = df.copy()
        for col in columns:
            df_numeric[col] = pd.to_numeric(df_numeric[col], errors='coerce')
            
        for col in columns:
            # Formatear el nombre de la característica para que se lea natural (como en tus imágenes)
            feature_name = col.replace('_importancia', '').replace('_calificacion', '').replace('_', ' ').capitalize()
            
            row_data = {'Característica': feature_name}
            
            # Segmentar y calcular para Hombres y Mujeres
            for gender in ['Masculino', 'Femenino']:
                # Filtrar por género y eliminar valores nulos en esta pregunta específica
                subset = df_numeric[df_numeric['genero'] == gender][col].dropna()
                
                n = len(subset)
                mean = subset.mean()
                std = subset.std()
                
                # Almacenar con símbolos y redondeado a 2 decimales
                row_data[f'n ({gender})'] = n
                row_data[f'x̄ ({gender})'] = round(mean, 2) if pd.notnull(mean) else 0.0
                row_data[f'σ ({gender})'] = round(std, 2) if pd.notnull(std) else 0.0
                
            stats_list.append(row_data)
            
        return pd.DataFrame(stats_list)
    except Exception as e:
        raise RuntimeError(f"Error al calcular estadísticas: {e}")

def get_analysis_tables(df_importance: pd.DataFrame, df_scoring: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Genera las tablas finales de análisis para Importancia y Calificación.
    """
    try:
        # Extraer solo las columnas de preguntas
        importance_cols = [col for col in df_importance.columns if col.endswith('_importancia')]
        
        scoring_cols = [col for col in df_scoring.columns if col.endswith('_calificacion')]
        if 'calificacion_global' in df_scoring.columns:
            scoring_cols.append('calificacion_global')

        # Calcular estadísticas
        stats_importance = calculate_descriptive_stats(df_importance, importance_cols)
        stats_scoring = calculate_descriptive_stats(df_scoring, scoring_cols)
        
        return stats_importance, stats_scoring
    except:
        raise RuntimeError("Error al generar las tablas de análisis")