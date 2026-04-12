# Procesamiento y Segmentación de Datos de Evaluación de Videojuegos Serios

## Integrantes
- Ángel Nicolás Landa Tapia
- Ximena Paola Pérez Sánchez
- Axel Yael Rodríguez Romero
- Emilio Estrada Pérez
- Juan Diego Rodríguez Espinoza

## Descripción
Este proyecto implementa un script en Python para el procesamiento de datos provenientes de una encuesta sobre la evaluación de características de videojuegos serios. El sistema realiza la carga, limpieza, segmentación interactiva y exportación de los datos mediante una estructura modular basada en funciones.

## Objetivo
Desarrollar una herramienta que permita:
1. Cargar un archivo de respuestas en formato `.xlsx`.
2. Aplicar filtros de limpieza según criterios de consentimiento informado y experiencia con videojuegos.
3. Permitir la segmentación interactiva por género y rango de edad.
4. Generar conjuntos de datos específicos para análisis.
5. Exportar los resultados a un archivo Excel con múltiples hojas.

## Estructura del Proyecto
```text
.
├── clean.py                 # Carga y limpieza de datos
├── cly.py                   # Interfaz de segmentación interactiva en consola
├── segmentation.py          # Segmentación por género y edad
├── segregation.py           # Creación de DataFrames de importancia y calificaciones
├── deportation.py           # Exportación de resultados a Excel
├── main.py                  # Script principal de ejecución
└── respuesta_de_encuestas.xlsx  # Archivo de entrada
```

## Requisitos
- Python 3.9 o superior.

## Dependencias
Instalar las siguientes librerías antes de ejecutar el proyecto:

```bash
pip install pandas openpyxl questionary
```

## Ejecución
Para ejecutar el proyecto, utilice el siguiente comando en la terminal:

```bash
python main.py
```

El archivo de entrada `respuesta_de_encuestas.xlsx` debe ubicarse en el mismo directorio del proyecto o especificarse 
