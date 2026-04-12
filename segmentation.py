import pandas as pd

# Creates new df filtering rows by gender
def gender_segmentation(df: pd.DataFrame, genders: list) -> pd.DataFrame:
    """
    Creates new df filtering rows by gender/s
    """
    gender_segmented_df = df.copy()

    normalized_genders = [gen.strip().lower() for gen in genders]
    real_genders = ["masculino", "femenino", "otro"]

    if any(gen not in real_genders for gen in normalized_genders):
        raise ValueError(f"Valid options: {real_genders}")

    #
    gender_segmented_df = gender_segmented_df[
        gender_segmented_df["Genero"].astype(str).str.strip().str.lower()
        .isin(normalized_genders)
    ]

    return gender_segmented_df


def age_segmentation(df: pd.DataFrame, segments: list) -> pd.DataFrame:
    """
    Creates new df filtering rows by age range/s
    """
    age_segmented_df = df.copy()

    age_segmented_df = age_segmented_df[
        age_segmented_df["Edad"].astype(str).str.strip().isin(segments)
    ]

    return age_segmented_df