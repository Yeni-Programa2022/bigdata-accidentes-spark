# Análisis de Accidentes de Tránsito con Apache Spark

## Descripción del proyecto

Este proyecto realiza el análisis de accidentes de tránsito en Colombia utilizando Apache Spark.  
Se aplican técnicas de procesamiento de datos en **batch** y una **simulación de procesamiento en tiempo real (streaming)** para identificar patrones relacionados con la gravedad, días y meses de ocurrencia de los accidentes.

---

## Problema

Los accidentes de tránsito representan una problemática importante en Colombia.  
Sin embargo, el análisis de los datos disponibles no siempre se realiza de forma eficiente, lo que dificulta la identificación de patrones que ayuden a la toma de decisiones.

Por esta razón, se busca procesar grandes volúmenes de datos utilizando herramientas de Big Data como Apache Spark.

---

## Objetivo general

Analizar el comportamiento de los accidentes de tránsito en Colombia mediante Apache Spark, aplicando procesamiento en batch y simulación de streaming para identificar patrones relevantes.

---

## Objetivos específicos

- Cargar y procesar el dataset de accidentes de tránsito utilizando Apache Spark.
- Realizar limpieza y transformación de los datos.
- Aplicar análisis exploratorio (EDA) según gravedad, día y mes.
- Implementar una simulación de procesamiento en tiempo real.
- Interpretar los resultados para identificar patrones de comportamiento.

---

## Tecnologías utilizadas

- Python 3.11  
- Apache Spark (PySpark)  
- Java 17  
- Git / GitHub  

---

## Dataset

Fuente: Datos Abiertos de Colombia  
Variables principales:

- Fecha  
- Año  
- Mes  
- Día  
- Gravedad del accidente  

---

## Procesamiento Batch (spark_accidentes.py)

Este módulo realiza:

- Carga del dataset
- Limpieza de datos (formato y separación de columnas)
- Análisis exploratorio (EDA)
  - Accidentes por gravedad
  - Accidentes por día de la semana
  - Accidentes por mes

✔ Permite identificar patrones históricos en los datos.

---

## Procesamiento Streaming (streaming_accidentes.py)

Este módulo implementa una **simulación de streaming** utilizando Spark.

- Simula llegada de datos en tiempo real
- Procesa registros de forma continua
- Muestra resultados en consola

✔ Representa el comportamiento de un sistema de análisis en tiempo real.

---

## Nota importante sobre streaming

Se implementó una simulación de procesamiento en streaming utilizando Apache Spark Structured Streaming, debido a limitaciones del entorno de ejecución.  
Esto permite representar el comportamiento de datos en tiempo real sin requerir la integración completa con Kafka.

---

## Resultados obtenidos

- Identificación de los tipos de accidentes más frecuentes
- Análisis de días con mayor número de accidentes
- Comportamiento mensual de los incidentes
- Estructuración de datos para análisis eficiente

---

## Cómo ejecutar el proyecto

### 1. Clonar repositorio
```bash
git clone https://github.com/Yeni-Programa2022/bigdata-accidentes-spark.git
cd bigdata-accidentes-spark
