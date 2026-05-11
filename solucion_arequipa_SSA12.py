# =============================================================================
# DATATHON SUNASS 2026 - RETO COMERCIAL (AREQUIPA)
# Script - Limpieza, Consumo Atípico y Pareto
# Autor: Equipo 12
#Inspeccion de para las tablas dadas 

import polars as pl
import os
import sys

# Ajusta el nombre de tu archivo temporalmente aquí
ARCHIVO_CRUDO = "DATOS/base_arequipa_1.csv"

# --- BLOQUE AÑADIDO: CREACIÓN DE CARPETA AUDITABLE ---
NOMBRE_CARPETA = "Auditable"
if not os.path.exists(NOMBRE_CARPETA):
    os.makedirs(NOMBRE_CARPETA)
    print(f"Carpeta '{NOMBRE_CARPETA}' creada exitosamente.")
else:
    print(f"La carpeta '{NOMBRE_CARPETA}' ya existe.")

def escanear_datos(ruta):
    print(f"\n{'='*60}")
    print(f"ESCÁNER DE RECONOCIMIENTO RÁPIDO (POLARS)")
    print(f"  Archivo: {ruta}")
    print(f"{'='*60}")

    if not os.path.exists(ruta):
        print(f"ERROR: El archivo no existe en {ruta}")
        return

    # Usamos infer_schema_length para evitar errores de parseo iniciales
    try:
        df = pl.read_csv(ruta, infer_schema_length=10000, ignore_errors=True)
    except Exception as e:
        print(f" Error leyendo como CSV. Intentando leer con separador ';' o Excel...")
        print(f"Detalle: {e}")
        return

    # 1. Dimensión de la data
    print(f"\n   DIMENSIONES:")
    print(f"   Filas: {df.height:,}")
    print(f"   Columnas: {df.width}")

    # 2. Nombres exactos de columnas y tipos de datos detectados
    print(f"\n   COLUMNAS Y TIPOS DE DATOS DETECTADOS:")
    for col_name, dtype in zip(df.columns, df.dtypes):
        print(f"   - {col_name:<25} : {dtype}")

    # 3. Conteo de Nulos y Valores Únicos (Rápido)
    print(f"\n   CALIDAD DE DATOS (Nulos):")
    nulos = df.null_count()
    for col in df.columns:
        n_nulos = nulos[col][0]
        if n_nulos > 0:
            pct = (n_nulos / df.height) * 100
            print(f"   - {col:<25} : {n_nulos:>7,} nulos ({pct:.1f}%)")

    # 4. Muestra real de datos (Head)
    print(f"\n   MUESTRA DE DATOS (Primeras 3 filas):")
    print(df.head(3))
    
    print(f"\n{'='*60}")
    print("      RECOMENDACIÓN PARA EL CONFIG.PY:")
    print("Copia los nombres exactos de la sección 'COLUMNAS' y pégalos")
    print("en el diccionario COLS de tu archivo '00_config.py'.")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    escanear_datos(ARCHIVO_CRUDO)

#unificar  las data 
import polars as pl
import os
import time
import glob

def unificar_data():
    print("  Iniciando unificación de 12 meses (Arequipa)...")
    inicio = time.time()
    
    # 1. Definir rutas
    base_dir = os.getcwd()
    ruta_busqueda = os.path.join(base_dir, "DATOS/base_arequipa_*.csv")
    ruta_salida = os.path.join(base_dir, "Auditable/data_comercial_arequipa_completa.csv")
    
    # 2. Encontrar archivos
    archivos = sorted(glob.glob(ruta_busqueda))
    
    if not archivos:
        print(f"  ERROR: No se encontraron archivos en: {ruta_busqueda}")
        return

    print(f" Archivos detectados: {len(archivos)}")
    
    try:
        lista_dfs = []
        for f in archivos:
            print(f"   Leyendo: {os.path.basename(f)}...", end="\r")
            # Leemos cada archivo individualmente
            temp_df = pl.read_csv(f, ignore_errors=True, infer_schema_length=10000)
            lista_dfs.append(temp_df)
        
        print(f"\n⚡ Unificando todos los meses en memoria...")
        # Concatenamos la lista de DataFrames
        df_final = pl.concat(lista_dfs)
        
        print(f"     Guardando {len(df_final):,} registros en el archivo final...")
        df_final.write_csv(ruta_salida)
        
        duracion = time.time() - inicio
        print(f"      ¡Éxito! Archivo unificado creado.")
        print(f"      Destino: data/raw/data_comercial_arequipa_completa.csv")
        print(f"    Tiempo total: {round(duracion, 2)} segundos.")
        
    except Exception as e:
        print(f"\n  Error durante la unificación: {e}")

if __name__ == "__main__":
    unificar_data()

#Limpiar data  general 

import polars as pl
import os
import sys

# Ajusta el nombre de tu archivo temporalmente aquí
ARCHIVO_CRUDO = "Auditable/data_comercial_arequipa_completa.csv"

def escanear_datos(ruta):
    print(f"\n{'='*60}")
    print(f"    ESCÁNER DE RECONOCIMIENTO RÁPIDO (POLARS)")
    print(f"  Archivo: {ruta}")
    print(f"{'='*60}")

    if not os.path.exists(ruta):
        print(f"  ERROR: El archivo no existe en {ruta}")
        return

    # Usamos infer_schema_length para evitar errores de parseo iniciales
    try:
        df = pl.read_csv(ruta, infer_schema_length=10000, ignore_errors=True)
    except Exception as e:
        print(f"  Error leyendo como CSV. Intentando leer con separador ';' o Excel...")
        print(f"Detalle: {e}")
        return

    # 1. Dimensión de la data
    print(f"\n   DIMENSIONES:")
    print(f"   Filas: {df.height:,}")
    print(f"   Columnas: {df.width}")

    # 2. Nombres exactos de columnas y tipos de datos detectados
    print(f"\n   COLUMNAS Y TIPOS DE DATOS DETECTADOS:")
    for col_name, dtype in zip(df.columns, df.dtypes):
        print(f"   - {col_name:<25} : {dtype}")

    # 3. Conteo de Nulos y Valores Únicos (Rápido)
    print(f"\n   CALIDAD DE DATOS (Nulos):")
    nulos = df.null_count()
    for col in df.columns:
        n_nulos = nulos[col][0]
        if n_nulos > 0:
            pct = (n_nulos / df.height) * 100
            print(f"   - {col:<25} : {n_nulos:>7,} nulos ({pct:.1f}%)")

    # 4. Muestra real de datos (Head)
    print(f"\n   MUESTRA DE DATOS (Primeras 3 filas):")
    print(df.head(3))
    

if __name__ == "__main__":
    escanear_datos(ARCHIVO_CRUDO)    
#reto 1 caso 1 
import polars as pl
import os
import time

# --- CONFIGURACIÓN DE RUTAS ACTUALIZADA ---
BASE_DIR = os.getcwd() 

# Definimos la entrada apuntando a la carpeta Auditable y el archivo unificado
RUTA_INPUT = os.path.join(BASE_DIR, "Auditable", "data_comercial_arequipa_completa.csv")

# Definimos la salida (puedes guardarlo en la misma carpeta con otro nombre)
RUTA_OUTPUT = os.path.join(BASE_DIR, "Auditable", "data_Ret1_1.csv")

def resolver_reto_1_1():
    # Verificamos si el archivo unificado existe antes de empezar
    if not os.path.exists(RUTA_INPUT):
        print(f"  ERROR: No se encontró el archivo unificado en: {RUTA_INPUT}")
        print("Asegúrate de correr primero el script de unificación.")
        return

    print(f" Leyendo data unificada desde: {RUTA_INPUT}")
    inicio = time.time()

    # 1. CARGA RÁPIDA
    # Usamos re-scan o lectura directa. Para archivos grandes, read_csv es muy veloz en Polars.
    df = pl.read_csv(RUTA_INPUT, infer_schema_length=10000)

    # 2. EVALUACIÓN (CONTEO)
    condicion = (pl.col("estado") == 1) & (pl.col("volumen_facturado") == 0)
    
    cantidad_cumplen = df.filter(condicion).height
    
    print(f"\n{'='*50}")
    print("    REPORTE RETO 1.1")
    print(f"{'='*50}")
    print(f"Registros con Estado 1 y Volumen 0: {cantidad_cumplen:,}")
    print(f"{'='*50}")

    # 3. MODIFICACIÓN (TRANSFORMACIÓN)
    print("    Aplicando corrección de importes...")
    
    df = df.with_columns([
        pl.when(condicion)
        .then(0.0)
        .otherwise(pl.col("importe_agua"))
        .alias("importe_agua"),
        
        pl.when(condicion)
        .then(0.0)
        .otherwise(pl.col("importe_alcantarillado"))
        .alias("importe_alcantarillado")
    ])

    # 4. GUARDADO DEL NUEVO ARCHIVO
    print(f" Guardando resultado en: {RUTA_OUTPUT}")
    df.write_csv(RUTA_OUTPUT)

    duracion = time.time() - inicio
    print(f" Proceso terminado en {round(duracion, 2)} seg.")

if __name__ == "__main__":
    resolver_reto_1_1()
#Ver y saber las inconsistencias
import polars as pl
import os

# --- RUTA AL ARCHIVO ORIGINAL ---
# Reemplaza esto con el nombre exacto de tu primera tabla (la que no tiene limpieza)
BASE_DIR = os.getcwd()
RUTA_ORIGINAL = os.path.join(BASE_DIR, "Auditable/data_Ret1_1.csv") 

def verificar_errores_iniciales():
    if not os.path.exists(RUTA_ORIGINAL):
        print(f"Error: No se encuentra el archivo en {RUTA_ORIGINAL}")
        return

    df = pl.read_csv(RUTA_ORIGINAL)

    # 1. Error de localización
    err_loc = df.group_by("conexion").agg(pl.col("localidad").n_unique()).filter(pl.col("localidad") > 1).height

    # 2. Error geográfico (coordenadas)
    err_geo = df.group_by("conexion").agg(pl.struct(["latitud", "longitud"]).n_unique()).filter(pl.col("latitud") > 1).height

    # 3. Volumen facturado — VOLFAC = 0 con importes positivos
    err_vol_cero = df.filter(
        (pl.col("estado") == 1) & 
        (pl.col("volumen_facturado") == 0) & 
        ((pl.col("importe_agua") > 0) | (pl.col("importe_alcantarillado") > 0))
    ).select("conexion").n_unique()

    # 4. Volumen facturado — VOLFAC negativo
    err_vol_neg = df.filter(pl.col("volumen_facturado") < 0).select("conexion").n_unique()

    # 5. Incongruencia de servicio — cobro indebido de alcantarillado
    err_alcant = df.filter((pl.col("servicios") == 2) & (pl.col("importe_alcantarillado") > 0)).select("conexion").n_unique()

    # 6. Incongruencia de servicio — cobro indebido de agua
    err_agua = df.filter((pl.col("servicios") == 3) & (pl.col("importe_agua") > 0)).select("conexion").n_unique()

    # --- SALIDA FORMATO REPORTE ---
    print(f"{'tipo_inconsistencia':<65}\t{'conexiones_con_error'}")
    print(f"{'Error de localización':<65}\t{err_loc:,}")
    print(f"{'Error geográfico (coordenadas)':<65}\t{err_geo:,}")
    print(f"{'Volumen facturado — VOLFAC = 0 con importes positivos':<65}\t{err_vol_cero:,}")
    print(f"{'Volumen facturado — VOLFAC negativo':<65}\t{err_vol_neg:,}")
    print(f"{'Incongruencia de servicio — cobro indebido de alcantarillado':<65}\t{err_alcant:,}")
    print(f"{'Incongruencia de servicio — cobro indebido de agua':<65}\t{err_agua:,}")

if __name__ == "__main__":
    verificar_errores_iniciales()
    

#reto 1 caso 2
### Script: 03_auditoria_estadistica_volumen.py python
import polars as pl
import os
import time

# --- RUTAS ---
BASE_DIR = os.getcwd()
# Usamos el archivo que ya tiene la corrección del Reto 1.1
RUTA_INPUT = os.path.join(BASE_DIR, "Auditable/data_Ret1_1.csv")

def auditar_volumen():
    print(f"Analizando distribución de volumen en 12M de registros...")
    inicio = time.time()

    # Leemos solo las columnas necesarias para ahorrar RAM
    df = pl.read_csv(RUTA_INPUT, columns=["conexion", "estado", "volumen_facturado", "categoria"])

    # 1. Filtro de Negativos en Conexiones Activas (Caso 2)
    negativos_df = df.filter((pl.col("estado") == 1) & (pl.col("volumen_facturado") < 0))
    
    # 2. Estadísticas Descriptivas Globales (Solo de valores positivos para comparar)
    stats_global = df.filter(pl.col("volumen_facturado") >= 0).select([
        pl.col("volumen_facturado").mean().alias("media"),
        pl.col("volumen_facturado").median().alias("mediana"),
        pl.col("volumen_facturado").std().alias("desviacion_std"),
        pl.col("volumen_facturado").min().alias("minimo"),
        pl.col("volumen_facturado").max().alias("maximo")
    ])

    # 3. Percentiles (Para detectar valores atípicos/Pareto)
    percentiles = df.select([
        pl.col("volumen_facturado").quantile(0.25).alias("P25"),
        pl.col("volumen_facturado").quantile(0.50).alias("P50_Mediana"),
        pl.col("volumen_facturado").quantile(0.75).alias("P75"),
        pl.col("volumen_facturado").quantile(0.90).alias("P90"),
        pl.col("volumen_facturado").quantile(0.99).alias("P99")
    ])

    print(f"\n{'='*60}")
    print("    RESULTADOS DE LA AUDITORÍA DE VOLUMEN")
    print(f"{'='*60}")
    print(f"Total registros con VOLUMEN NEGATIVO: {negativos_df.height:,}")
    
    if negativos_df.height > 0:
        sum_negativos = negativos_df.select(pl.col("volumen_facturado").sum()).item()
        print(f"Suma total de volumen negativo: {sum_negativos:,.2f} m3")
        print(f"Valor negativo más extremo: {negativos_df.select(pl.col('volumen_facturado').min()).item():,.2f} m3")
    
    print(f"\n DISTRIBUCIÓN DE VALORES VÁLIDOS (>= 0):")
    print(stats_global)
    
    print(f"\nPERCENTILES (Detección de sesgo):")
    print(percentiles)
    print(f"{'='*60}")

    # 4. Análisis por Categoría (Para ver si los negativos son de Industriales o Domésticos)
    if "categoria" in df.columns:
        print("\n Negativos detectados por Categoría:")
        conteo_cat = negativos_df.group_by("categoria").agg(pl.count().alias("cantidad_negativos"))
        print(conteo_cat)

    print(f"\n      Auditoría completada en {round(time.time() - inicio, 2)} seg.")

if __name__ == "__main__":
    auditar_volumen()

import polars as pl
import os
import time

# --- RUTAS ---
BASE_DIR = os.getcwd()
RUTA_INPUT = os.path.join(BASE_DIR, "Auditable/data_Ret1_1.csv")
RUTA_OUTPUT = os.path.join(BASE_DIR, "Auditable/data_Ret1_2.csv")

def corregir_negativos():
    print(f"    Iniciando corrección de 77,800 negativos...")
    inicio = time.time()

    # 1. Carga de datos
    df = pl.read_csv(RUTA_INPUT)

    # 2. Calcular la Mediana por Conexión (usando solo valores válidos >= 0)
    print("   Calculando medianas históricas por conexión...")
    medianas_conexion = (
        df.filter(pl.col("volumen_facturado") >= 0)
        .group_by("conexion")
        .agg(pl.col("volumen_facturado").median().alias("mediana_conn"))
    )

    # 3. Unir medianas al DF principal
    df = df.join(medianas_conexion, on="conexion", how="left")

    # 4. Lógica de Imputación:
    # Si (estado=1 Y vol < 0):
    #    Si tiene mediana histórica -> usar mediana_conn
    #    Sino -> usar 0
    # Caso contrario -> mantener original
    
    print(" Imputando valores...")
    df = df.with_columns(
        pl.when((pl.col("estado") == 1) & (pl.col("volumen_facturado") < 0))
        .then(
            pl.col("mediana_conn").fill_null(0.0)
        )
        .otherwise(pl.col("volumen_facturado"))
        .alias("volumen_facturado")
    )

    # 5. Limpieza y Guardado
    # Eliminamos la columna temporal de medianas y guardamos
    df = df.drop("mediana_conn")
    
    print(f"     Guardando en: {RUTA_OUTPUT}")
    df.write_csv(RUTA_OUTPUT)

    print(f"      ¡Reto 1 Caso 2 completado!")
    print(f"  Tiempo de ejecución: {round(time.time() - inicio, 2)} seg.")

if __name__ == "__main__":
    corregir_negativos()

#caso 3 
import polars as pl
df = pl.read_csv("Auditable/data_Ret1_2.csv")
# Esto nos dirá qué etiquetas exactas existen
print(df.select("modalidad_facturacion").unique()) 
# Y si tienes una columna llamada 'tipo_servicio' o similar, búscala:
print(df.columns)
import polars as pl
import os
import time

# --- RUTAS ---
BASE_DIR = os.getcwd()
RUTA_INPUT = os.path.join(BASE_DIR, "Auditable/data_Ret1_2.csv")
RUTA_OUTPUT = os.path.join(BASE_DIR, "Auditable/data_Ret1_3.csv")

def corregir_servicios():
    print(f"  Iniciando auditoría y corrección de incongruencias...")
    inicio = time.time()

    # 1. Carga de datos
    df = pl.read_csv(RUTA_INPUT)

    # 2. AUDITORÍA PREVIA (Identificar el problema antes de limpiar)
    # Incongruencia de agua: Servicio 3 (Solo Alcant) pero tiene importe_agua > 0
    df_error_agua = df.filter((pl.col("servicios") == 3) & (pl.col("importe_agua") > 0))
    errores_agua_filas = df_error_agua.height
    errores_agua_conexiones = df_error_agua.select("conexion").n_unique()

    # Incongruencia de alcantarillado: Servicio 2 (Solo Agua) pero tiene importe_alcantarillado > 0
    df_error_alcant = df.filter((pl.col("servicios") == 2) & (pl.col("importe_alcantarillado") > 0))
    errores_alcant_filas = df_error_alcant.height
    errores_alcant_conexiones = df_error_alcant.select("conexion").n_unique()

    # 3. APLICAR CORRECCIÓN (Limpieza quirúrgica)
    # Usamos la lógica de "Si el contrato dice X, limpia lo que no sea X"
    df_limpio = df.with_columns([
        # Si es Solo Alcantarillado (3), el agua debe ser 0.0
        pl.when(pl.col("servicios") == 3)
        .then(0.0)
        .otherwise(pl.col("importe_agua"))
        .alias("importe_agua"),
        
        # Si es Solo Agua (2), el alcantarillado debe ser 0.0
        pl.when(pl.col("servicios") == 2)
        .then(0.0)
        .otherwise(pl.col("importe_alcantarillado"))
        .alias("importe_alcantarillado")
    ])

    # 4. IMPRESIÓN DE RESULTADOS EN CONSOLA
    print(f"\n{'='*60}")
    print(" REPORTE DE INCONGRUENCIAS DETECTADAS")
    print(f"{'='*60}")
    print(f"  Cobro indebido de AGUA (Servicio Solo Alcantarillado):")
    print(f"   - Filas afectadas: {errores_agua_filas:,}")
    print(f"   - Conexiones únicas: {errores_agua_conexiones:,}")
    
    print(f"\n  Cobro indebido de ALCANTARILLADO (Servicio Solo Agua):")
    print(f"   - Filas afectadas: {errores_alcant_filas:,}")
    print(f"   - Conexiones únicas: {errores_alcant_conexiones:,}")
    print(f"{'='*60}")

    # 5. GUARDADO
    print(f"     Guardando datos limpios en: {RUTA_OUTPUT}")
    df_limpio.write_csv(RUTA_OUTPUT)

    print(f"      Proceso terminado en {round(time.time() - inicio, 2)} seg.")

if __name__ == "__main__":
    corregir_servicios()
#caso 4
import polars as pl
import os
import time

# --- RUTAS ---
BASE_DIR = os.getcwd()
RUTA_INPUT = os.path.join(BASE_DIR, "Auditable/data_Ret1_3.csv")
RUTA_OUTPUT = os.path.join(BASE_DIR, "Auditable/data_Ret1_4.csv")

def corregir_localidad():
    print(f"  Iniciando corrección de estabilidad geográfica...")
    inicio = time.time()

    # 1. Carga de datos
    df = pl.read_csv(RUTA_INPUT)

    # 2. CALCULAR LA MODA POR CONEXIÓN
    # Contamos ocurrencias de cada localidad por conexión
    moda_localidad = (
        df.group_by(["conexion", "localidad"])
        .agg(pl.len().alias("conteo"))
        .sort("conteo", descending=True)
        .group_by("conexion")
        .first() # Al estar ordenado por conteo, el primero es la MODA
        .select(["conexion", "localidad"])
        .rename({"localidad": "localidad_correcta"})
    )

    # 3. IDENTIFICAR ERRORES ANTES DE APLICAR
    # Unimos temporalmente para comparar
    check_df = df.select(["conexion", "localidad"]).join(moda_localidad, on="conexion")
    inconsistencias = check_df.filter(pl.col("localidad") != pl.col("localidad_correcta")).height
    conexiones_afectadas = check_df.filter(pl.col("localidad") != pl.col("localidad_correcta")).select("conexion").n_unique()

    # 4. APLICAR CORRECCIÓN
    df = df.join(moda_localidad, on="conexion", how="left")
    df = df.with_columns(pl.col("localidad_correcta").alias("localidad")).drop("localidad_correcta")

    # 5. REPORTE
    print(f"\n{'='*60}")
    print("   REPORTE DE ERRORES DE LOCALIZACIÓN")
    print(f"{'='*60}")
    print(f"  Registros (filas) con localidad errónea: {inconsistencias:,}")
    print(f"  Conexiones que 'cambiaron' de lugar: {conexiones_afectadas:,}")
    print(f"{'='*60}")

    # 6. GUARDADO
    print(f"     Guardando en: {RUTA_OUTPUT}")
    df.write_csv(RUTA_OUTPUT)

    print(f"      Proceso terminado en {round(time.time() - inicio, 2)} seg.")

if __name__ == "__main__":
    corregir_localidad()
#caso 5
import polars as pl
import os
import time

# --- RUTAS ---
BASE_DIR = os.getcwd()
RUTA_INPUT = os.path.join(BASE_DIR, "Auditable/data_Ret1_4.csv")
RUTA_OUTPUT = os.path.join(BASE_DIR, "Auditable/data_Ret1_5.csv")

def corregir_coordenadas():
    print(f"  Iniciando corrección de estabilidad en coordenadas (Lat/Long)...")
    inicio = time.time()

    # 1. Carga de datos
    df = pl.read_csv(RUTA_INPUT)

    # 2. CALCULAR LA MODA DEL PAR (LATITUD, LONGITUD) POR CONEXIÓN
    # Agrupamos por conexión y ambas coordenadas para contar repeticiones
    moda_coordenadas = (
        df.group_by(["conexion", "latitud", "longitud"])
        .agg(pl.len().alias("conteo"))
        .sort("conteo", descending=True)
        .group_by("conexion")
        .first() # Tomamos el par (Lat, Long) más frecuente
        .select([
            pl.col("conexion"),
            pl.col("latitud").alias("lat_correcta"),
            pl.col("longitud").alias("long_correcta")
        ])
    )

    # 3. AUDITORÍA DE CAMBIOS
    # Unimos para comparar valores originales vs calculados
    df_check = df.join(moda_coordenadas, on="conexion", how="left")
    
    filas_erroneas = df_check.filter(
        (pl.col("latitud") != pl.col("lat_correcta")) | 
        (pl.col("longitud") != pl.col("long_correcta"))
    ).height

    conexiones_erroneas = df_check.filter(
        (pl.col("latitud") != pl.col("lat_correcta")) | 
        (pl.col("longitud") != pl.col("long_correcta"))
    ).select("conexion").n_unique()

    # 4. APLICAR CORRECCIÓN
    df_final = df_check.with_columns([
        pl.col("lat_correcta").alias("latitud"),
        pl.col("long_correcta").alias("longitud")
    ]).drop(["lat_correcta", "long_correcta"])

    # 5. REPORTE EN CONSOLA
    print(f"\n{'='*60}")
    print("   REPORTE DE INCONSISTENCIAS GEOGRÁFICAS (LAT/LONG)")
    print(f"{'='*60}")
    print(f"  Filas con coordenadas desviadas: {filas_erroneas:,}")
    print(f"  Conexiones con 'salto' geográfico: {conexiones_erroneas:,}")
    print(f"{'='*60}")

    # 6. GUARDADO
    print(f"     Guardando en: {RUTA_OUTPUT}")
    df_final.write_csv(RUTA_OUTPUT)

    print(f"      Proceso terminado en {round(time.time() - inicio, 2)} seg.")

if __name__ == "__main__":
    corregir_coordenadas()
#parte 2 Reto 2 
import polars as pl
import os
import time

# --- RUTAS ---
BASE_DIR = os.getcwd()
RUTA_INPUT = os.path.join(BASE_DIR, "Auditable/data_Ret1_5.csv")
RUTA_OUTPUT = os.path.join(BASE_DIR, "Auditable/data_Ret2_ConsumoAtipico.csv")

def identificar_consumo_atipico():
    print(f"   Procesando datos para el reporte mensual...")
    inicio = time.time()

    df = pl.read_csv(RUTA_INPUT)

    # 1. Mapeo de Asignación
    mapa_asignacion = {101: 15, 201: 15, 301: 15, 401: 50, 501: 95}
    
    df = df.with_columns(
        pl.col("codigo_categoria").replace_strict(mapa_asignacion, default=15).alias("asig_u")
    )

    # 2. Filtrar Universo Válido y Agregar por Conexión-Mes
    df_agg = (
        df.filter((pl.col("estado") == 1) & (pl.col("modalidad_facturacion") == "L"))
        .group_by(["conexion", "mes"])
        .agg([
            pl.col("volumen_facturado").sum().alias("vol_mes"),
            pl.col("asig_u").sum().alias("asig_mes")
        ])
        .sort(["conexion", "mes"])
    )

    # 3. Promedio Histórico Móvil (6 meses, min 2)
    df_agg = df_agg.with_columns(
        pl.col("vol_mes")
        .shift(1)
        .rolling_mean(window_size=6, min_periods=2)
        .over("conexion")
        .alias("prom_hist")
    )

    # 4. Cálculo de Límites y Marcado de Atípicos
    # Nota: No filtramos mes >= 3 aquí para que la tabla muestre todos los meses (1-12)
    df_final = df_agg.with_columns(
        pl.max_horizontal(pl.col("prom_hist") * 2, pl.col("asig_mes") * 2).alias("limite")
    ).with_columns(
        pl.when(pl.col("prom_hist").is_not_null() & (pl.col("vol_mes") > pl.col("limite")))
        .then(1)
        .otherwise(0)
        .alias("es_atipico")
    )

    # 5. GENERACIÓN DEL REPORTE MENSUAL (Lo que pediste)
    reporte_mensual = (
        df_final.group_by("mes")
        .agg([
            pl.len().alias("total_conexiones"),
            pl.col("es_atipico").sum().alias("conexiones_atipicas")
        ])
        .with_columns(
            (pl.col("conexiones_atipicas") / pl.col("total_conexiones") * 100).round(1).alias("porcentaje")
        )
        .sort("mes")
    )

    # 6. SALIDA A CONSOLA
    print(f"\n{'='*65}")
    print(f"{'MES':<5} | {'TOTAL CONEX.':<15} | {'ATÍPICAS':<12} | {'PORCENTAJE':<10}")
    print(f"{'-'*65}")
    
    for row in reporte_mensual.iter_rows(named=True):
        print(f"{row['mes']:<5} | {row['total_conexiones']:<15,} | {row['conexiones_atipicas']:<12,} | {row['porcentaje']}%")
    
    print(f"{'='*65}")

    # 7. GUARDADO
    df_final.write_csv(RUTA_OUTPUT)
    print(f"   Resultado completo guardado en: {RUTA_OUTPUT}")
    print(f"   Tiempo total: {round(time.time() - inicio, 2)} seg.")

if __name__ == "__main__":
    identificar_consumo_atipico()
#Reto 3

import polars as pl
import os
import time

# --- RUTAS ---
BASE_DIR = os.getcwd()
RUTA_INPUT = os.path.join(BASE_DIR, "Auditable/data_Ret1_5.csv")
RUTA_OUTPUT = os.path.join(BASE_DIR, "Auditable/data_Ret3_GrandesUsuarios.csv")

def identificar_grandes_usuarios():
    print(f"   Iniciando Reto 3: Análisis de Pareto (80/20)...")
    inicio = time.time()

    # 1. Carga y Preparación
    df = pl.read_csv(RUTA_INPUT)
    
    # Solo activos. Sumamos todos los importes para el 'Importe Total'
    df_activos = df.filter(pl.col("estado") == 1).with_columns(
        (pl.col("importe_agua") + pl.col("importe_alcantarillado") + pl.col("importe_cargo_fijo")).alias("importe_u")
    )

    # 2. Agregación a nivel de Conexión-Mes
    df_agg = (
        df_activos.group_by(["conexion", "mes"])
        .agg([
            pl.col("volumen_facturado").sum().alias("vol_tot"),
            pl.col("importe_u").sum().alias("imp_tot"),
            pl.len().alias("uds_tot")
        ])
    )

    # 3. Función interna para aplicar Pareto 80/20 por dimensión y mes
    def aplicar_pareto(df_input, col_name, alias_flag):
        return (
            df_input.sort(["mes", col_name], descending=[False, True])
            .with_columns(
                (pl.col(col_name).cum_sum().over("mes") / pl.col(col_name).sum().over("mes")).alias("pct_acum")
            )
            .with_columns(
                pl.when(pl.col("pct_acum") <= 0.80000001) # Margen por precisión float
                .then(1).otherwise(0).alias(alias_flag)
            )
            .drop("pct_acum")
        )

    # Aplicamos Pareto para las 3 dimensiones
    df_agg = aplicar_pareto(df_agg, "vol_tot", "g_vol")
    df_agg = aplicar_pareto(df_agg, "imp_tot", "g_imp")
    df_agg = aplicar_pareto(df_agg, "uds_tot", "g_uds")

    # Una conexión es Gran Usuario si cumple al menos una
    df_agg = df_agg.with_columns(
        pl.max_horizontal("g_vol", "g_imp", "g_uds").alias("es_grand_usuario")
    )

    # 4. GENERACIÓN DEL REPORTE MENSUAL REQUERIDO
    reporte = (
        df_agg.group_by("mes")
        .agg([
            pl.len().alias("conexiones"),
            pl.col("g_vol").sum().alias("grandes_volfac"),
            pl.col("g_imp").sum().alias("grandes_importe"),
            pl.col("g_uds").sum().alias("grandes_uso")
        ])
        .with_columns([
            (pl.col("grandes_volfac") / pl.col("conexiones") * 100).round(1).alias("vol_pct"),
            (pl.col("grandes_importe") / pl.col("conexiones") * 100).round(1).alias("imp_pct"),
            (pl.col("grandes_uso") / pl.col("conexiones") * 100).round(1).alias("uso_pct")
        ])
        .sort("mes")
    )

    # 5. SALIDA A CONSOLA (Formato solicitado)
    print(f"\n{'mes':<4} | {'conexiones':<12} | {'g_vol':<8} | {'%_vol':<7} | {'g_imp':<8} | {'%_imp':<7} | {'g_uso':<8} | {'%_uso':<7}")
    print("-" * 90)
    for r in reporte.iter_rows(named=True):
        print(f"{r['mes']:<4} | {r['conexiones']:<12,} | {r['grandes_volfac']:<8,} | {r['vol_pct']}%  | {r['grandes_importe']:<8,} | {r['imp_pct']}%  | {r['grandes_uso']:<8,} | {r['uso_pct']}%")

    # 6. GUARDADO
    df_agg.write_csv(RUTA_OUTPUT)
    print(f"\n   Archivo guardado: {RUTA_OUTPUT}")
    print(f"   Tiempo: {round(time.time() - inicio, 2)} seg.")

if __name__ == "__main__":
    identificar_grandes_usuarios()