# Análisis de Accidentes de Tránsito con Apache Spark

## Descripción
Este proyecto realiza un análisis de datos de accidentes de tránsito en Colombia utilizando Apache Spark.

## Procesamiento en Batch
Se realizó la carga, limpieza y análisis de los datos para identificar patrones según:
- Gravedad del accidente
- Día de ocurrencia
- Mes

## Procesamiento en Tiempo Real
Se implementó una simulación de streaming donde los datos se procesan de forma secuencial para representar su comportamiento en tiempo real.

## Tecnologías utilizadas
- Python
- Apache Spark

## Archivos
- spark_accidentes.py
- streaming_accidentes.py

## Ejecución
Ejecutar en consola:
py -3.11 spark_accidentes.py
py -3.11 streaming_accidentes.py
