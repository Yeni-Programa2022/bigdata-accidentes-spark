import time
from pyspark.sql import SparkSession
from pyspark.sql.functions import split, regexp_replace

print("Iniciando Streaming...")

spark = SparkSession.builder.appName("StreamingAccidentes").getOrCreate()

df = spark.read.text("accidentes.csv")

df = df.withColumn("value", regexp_replace("value", '"', ''))
df = df.withColumn("columnas", split(df["value"], ","))

df_final = df.selectExpr(
    "columnas[0] as ORDEN",
    "columnas[1] as IPAT",
    "columnas[2] as FECHA",
    "columnas[3] as ANIO",
    "columnas[4] as MES",
    "columnas[5] as DIA",
    "columnas[6] as GRAVEDAD"
)

df_final = df_final.filter(df_final.ORDEN != "ORDEN")

datos = df_final.collect()

print("Simulación en tiempo real:\n")

for fila in datos[:20]:
    print(f"Día: {fila['DIA']} | Gravedad: {fila['GRAVEDAD']}")
    time.sleep(1)

print("\nResumen:")
df_final.groupBy("GRAVEDAD").count().show()