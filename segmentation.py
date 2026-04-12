import pandas as pd

# Filter rows by gender
def gender_segmentation(df: pd.DataFrame, genders: list) -> pd.DataFrame:
    gender_segmented_df = df.copy()

    normalized_genders = [gen.strip().lower() for gen in genders]
    real_genders = ["masculino", "femenino", "otro"]

    if any(gen not in real_genders for gen in normalized_genders):
        raise ValueError(f"Valid options: {real_genders}")

    gender_segmented_df = gender_segmented_df[
        gender_segmented_df["Genero"].astype(str).str.strip().str.lower()
        .isin(normalized_genders)
    ]

    return gender_segmented_df

# Filter rows by age range
def age_segmentation(df: pd.DataFrame, segments: list) -> pd.DataFrame:
    age_segmented_df = df.copy()

    age_segmented_df = age_segmented_df[
        age_segmented_df["Edad"].astype(str).str.strip().isin(segments)
    ]

    return age_segmented_df