from clean import load_data, clean_data, normalize_genders
from cli import data_path, ask_gender_segmentation, ask_age_segmentation
from segment import gender_segmentation, age_segmentation
from group import question_segmentation
from export import export_to_excel
from analyze import get_analysis_tables 

def main():
    try:
        file_path = data_path()

        # Fase 1 y 2
        df = load_data(file_path)
        df = clean_data(df)
        df = normalize_genders(df)

        # Fase 3
        genders = ask_gender_segmentation()
        if genders:
            df = gender_segmentation(df, genders)

        ages = ask_age_segmentation()
        if ages:
            df = age_segmentation(df, ages)

        # Fase 4
        df_importance, df_scoring = question_segmentation(df)

        # Fase de Análisis
        print("\nGenerando tablas de análisis...")
        stats_importance, stats_scoring = get_analysis_tables(df_importance, df_scoring)

        # Fase 5
        print("Exportando a Excel...")
        export_to_excel(df, df_importance, df_scoring, stats_importance, stats_scoring)
        
        print("\n¡Tablas generadas con éxito en el archivo Excel!")
        
    except Exception as error:
        print(f"Ocurrió un error: {error}")
    finally:
        print("Proceso terminado")

if __name__ == "__main__":
    main()