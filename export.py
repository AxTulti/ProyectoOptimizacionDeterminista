# Phase 5
import os
import pandas as pd
from openpyxl.utils import get_column_letter

def export_to_excel(
    df_complete: pd.DataFrame,
    df_importance: pd.DataFrame,
    df_scoring: pd.DataFrame,
    stats_importance: pd.DataFrame,
    stats_scoring: pd.DataFrame,
    output_filename: str = "resultados_encuesta.xlsx"
) -> str:
    
    """
    Combines our dataframes and analysis into 1 excel file and exports it.
    """
    try:
        output_path = os.path.join(os.getcwd(), output_filename)

        with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
            # Hojas de datos crudos/agrupados
            df_complete.to_excel(writer, sheet_name="Datos Completos", index=False)
            df_importance.to_excel(writer, sheet_name="Importancia", index=False)
            df_scoring.to_excel(writer, sheet_name="Calificaciones", index=False)
            
            # Nuevas hojas con el análisis estadístico
            stats_importance.to_excel(writer, sheet_name="Análisis Importancia", index=False)
            stats_scoring.to_excel(writer, sheet_name="Análisis Calificación", index=False)

            # Ajuste de ancho de columnas para todas las hojas
            sheets_dict = {
                "Datos Completos": df_complete,
                "Importancia": df_importance,
                "Calificaciones": df_scoring,
                "Análisis Importancia": stats_importance,
                "Análisis Calificación": stats_scoring
            }

            for sheet_name, dataframe in sheets_dict.items():
                worksheet = writer.book[sheet_name]
                for col_idx, column_name in enumerate(dataframe.columns, start=1):
                    title_length = len(str(column_name))
                    adjusted_width = min(title_length + 2, 50)
                    col_letter = get_column_letter(col_idx)
                    worksheet.column_dimensions[col_letter].width = adjusted_width

        return output_path
    except Exception as e:
        raise RuntimeError(f"Error al exportar archivo: {e}")