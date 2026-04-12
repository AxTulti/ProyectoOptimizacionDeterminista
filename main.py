from clean import load_data, clean_data
from CLI import data_path, ask_gender_segmentation, ask_age_segmentation
from segmentation_p3 import gender_segmentation, age_segmentation
from segregation_p4 import question_segmentation
from deportation_p5 import export_to_excel


def main():
    file_path = data_path()

    # Fase 1 y 2
    df = load_data(file_path)
    df = clean_data(df)

    # Fase 3
    genders = ask_gender_segmentation()
    df = gender_segmentation(df, genders)

    ages = ask_age_segmentation()
    df = age_segmentation(df, ages)

    # Fase 4
    df_importance, df_scoring = question_segmentation(df)

    # Fase 5
    export_to_excel(df, df_importance, df_scoring)

    print("Proceso terminado")


if __name__ == "__main__":
    main()