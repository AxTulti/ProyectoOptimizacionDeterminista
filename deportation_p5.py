# Phase 5
import os
import pandas as pd
from openpyxl.utils import get_column_letter


def export_to_excel(
    df_complete: pd.DataFrame,
    df_importance: pd.DataFrame,
    df_scoring: pd.DataFrame,
    output_filename: str = "resultados_encuesta.xlsx"
) -> str:
    
    """
    Combines our 3 dataframes into 1 excel file and exports it to a set path
    """
    
    #Where to save file
    output_path = os.path.join(os.getcwd(), output_filename)

    # Create excel sheets
    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        df_complete.to_excel(writer, sheet_name="Datos Completos", index=False)
        df_importance.to_excel(writer, sheet_name="Importancia", index=False)
        df_scoring.to_excel(writer, sheet_name="Calificaciones", index=False)

        for sheet_name, dataframe in {
            "Datos Completos": df_complete,
            "Importancia": df_importance,
            "Calificaciones": df_scoring
        }.items():
            worksheet = writer.book[sheet_name]


            # Adjusting column widht
            for col_idx, column_name in enumerate(dataframe.columns, start=1):
                max_length = len(str(column_name))

                for value in dataframe[column_name]:
                    value_length = len(str(value)) if value is not None else 0
                    if value_length > max_length:
                        max_length = value_length

                adjusted_width = min(max_length + 2, 40)
                col_letter = get_column_letter(col_idx)
                worksheet.column_dimensions[col_letter].width = adjusted_width

    return output_path