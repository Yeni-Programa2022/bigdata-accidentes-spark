from pyspark.sql import SparkSession
from pyspark.sql.functions import split, regexp_replace

print("Iniciando Spark...")

# Crear sesión de Spark
spark = SparkSession.builder.appName("Accidentes").getOrCreate()

print("Spark iniciado")

# Leer archivo como texto
df = spark.read.text("accidentes.csv")

print("Archivo cargado")

# Limpiar comillas
df = df.withColumn("value", regexp_replace("value", '"', ''))

# Separar columnas
df = df.withColumn("columnas", split(df["value"], ","))

# Crear columnas finales
df_final = df.selectExpr(
    "columnas[0] as ORDEN",
    "columnas[1] as IPAT",
    "columnas[2] as FECHA",
    "columnas[3] as ANIO",
    "columnas[4] as MES",
    "columnas[5] as DIA",
    "columnas[6] as GRAVEDAD"
)

print("Datos limpios:")
df_final.show(5)

df_final = df_final.filter(df_final.ORDEN != "ORDEN")

# 🔥 ANÁLISIS

print("Accidentes por gravedad:")
df_final.groupBy("GRAVEDAD").count().show()

print("Accidentes por día:")
df_final.groupBy("DIA").count().show()

from pyspark.sql.functions import when

df_final = df_final.withColumn(
    "MES_NOMBRE",
    when(df_final.MES == "1", "Enero")
    .when(df_final.MES == "2", "Febrero")
    .when(df_final.MES == "3", "Marzo")
    .when(df_final.MES == "4", "Abril")
    .when(df_final.MES == "5", "Mayo")
    .when(df_final.MES == "6", "Junio")
    .when(df_final.MES == "7", "Julio")
    .when(df_final.MES == "8", "Agosto")
    .when(df_final.MES == "9", "Septiembre")
    .when(df_final.MES == "10", "Octubre")
    .when(df_final.MES == "11", "Noviembre")
    .when(df_final.MES == "12", "Diciembre")
)

print("Accidentes por mes:")
df_final.groupBy("MES_NOMBRE").count().show()