import pandas as pd
import questionary

# Fase 1 — Carga de datos y limpieza inicial

raw_data = pd.read_excel("./data/respuestas_de_encuestas.xlsx", header=None)

print("Original entries:", len(raw_data))

data = raw_data[(raw_data[2] == "Si") & (raw_data[14] == "Sí")]

print("Filtered entries:", len(data))

# Fase 2 — Selección y renombramiento de columnas

new_columns = {
    4: "Género",
    5: "Edad",
    21: "Nombre Videojuego",
    22: "Categoría Videojuego",
    23: "Desafío",
    24: "Desafío",
    25: "Retroalimentación",
    26: "Retroalimentación",
    27: "Inmersión",
    28: "Inmersión",
    29: "Concentración",
    30: "Concentración",
    31: "Claridad de objetivos",
    32: "Claridad de objetivos",
    33: "Autonomía",
    34: "Autonomía",
    35: "Interacción social",
    36: "Interacción social",
    37: "Mejora del conocimiento",
    38: "Mejora del conocimiento",
    39: "Involucramiento emocional",
    40: "Involucramiento emocional",
    41: "Equilibrio entre habilidades y tareas",
    42: "Equilibrio entre habilidades y tareas",
    43: "Narrativa atractiva",
    44: "Narrativa atractiva",
    45: "Estructura de progresión",
    46: "Estructura de progresión",
    47: "Animación y sonido",
    48: "Animación y sonido",
    49: "Calificación Global"
}

data = data.rename(columns=new_columns).loc[:, new_columns.values()]

# Fase 3 — Segmentación interactiva

## Función 1 — Decisión de segmentar

## Función 2 — Segmentación por género

## Función 3 — Segmentación por rango de edad

# Fase 4 — Creación de los conjuntos de datos

## DataFrame: Importancia

## DataFrame: Calificaciones

# Fase 5 — Exportación a Excel