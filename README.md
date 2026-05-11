# DATATHON SUNASS 2026 – RETO COMERCIAL (AREQUIPA)

Proyecto desarrollado para el análisis, limpieza y procesamiento de datos comerciales de SUNASS Arequipa utilizando Python y Polars.

## Autores

- Mauricio Morales Cervantes
- Joaquín Sebastian Cárdenas Cotrina

---

# Descripción del Proyecto

Este proyecto tiene como objetivo realizar el tratamiento y análisis de grandes volúmenes de información comercial correspondientes a registros de consumo de agua potable y alcantarillado de la ciudad de Arequipa.

La solución implementa procesos de:

- Exploración de datos
- Validación de calidad
- Unificación de archivos mensuales
- Detección de inconsistencias
- Corrección de registros anómalos
- Generación de archivos auditables
- Evaluación de consumos atípicos
- Análisis tipo Pareto

Todo el procesamiento fue desarrollado en Python empleando la librería **Polars**, optimizada para el manejo eficiente de datasets masivos.

---

# Objetivos del Script

## 1. Escaneo y reconocimiento de datos

El sistema realiza una inspección inicial de cada archivo CSV para:

- Detectar dimensiones de la data
- Identificar columnas y tipos de datos
- Detectar valores nulos
- Mostrar muestras de registros
- Facilitar auditorías y validaciones previas

---

## 2. Unificación de información mensual

El script consolida automáticamente los archivos:

```text
base_arequipa_1.csv
base_arequipa_2.csv
...
base_arequipa_12.csv


Cada archivo representa un mes del año.

---

## 3. Estructura del proyecto
. ├── README.md ├── notebook.ipynb └── data/     ├── base_arequipa_01.csv     ├── ...     └── base_arequipa_12.csv

---

## 4. Ejecución en Google Colab (100% portable)

El notebook no depende de rutas locales ni Google Drive.

### Pasos:
1. Abrir el notebook en Google Colab  
2. Ejecutar todas las celdas  
3. Los datos se cargan desde URLs públicas (GitHub)

---

## 5. Carga de datos

Los archivos se leen directamente desde GitHub:

python import polars as pl  urls = [     "https://raw.githubusercontent.com/USUARIO/REPO/main/base_arequipa_01.csv",     ... ]  df = pl.concat([pl.read_csv(url) for url in urls]) 

---

## 6. Reglas de negocio aplicadas

- Si estado = 1 y volumen = 0:
  - importe_agua = 0
  - importe_alcantarillado = 0

- Si servicios = 2:
  - importe_alcantarillado = 0

- Si servicios = 3:
  - importe_agua = 0

- Valores negativos:
  - Se reemplazan por 0

---

## 7. Validaciones realizadas

- Consistencia entre tipo de servicio e importes  
- Detección de registros inválidos  
- Conteo de filas afectadas por cada regla  

---

## 8. Output

Se genera un único dataset consolidado:

resultado_final.csv

---

## 9. Tecnologías utilizadas

- Python  
- Polars  
- Google Colab  

---

## 10. Consideraciones

- El proyecto está diseñado para ser reproducible  
- No depende de archivos locales  
- Todos los datos deben estar disponibles vía URL  

---
