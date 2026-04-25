# SUNASS Arequipa – Procesamiento y Validación de Datos

## 1. Objetivo
Consolidar y validar información comercial de Arequipa a partir de múltiples archivos mensuales en formato CSV, generando un único dataset limpio y consistente para análisis.

---

## 2. Fuente de datos
Los datos provienen de archivos mensuales:

- base_arequipa_01.csv
- base_arequipa_02.csv
- ...
- base_arequipa_12.csv

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

## 11. Autor

Mauricio Morales Cervantes  
Arequipa, Perú
