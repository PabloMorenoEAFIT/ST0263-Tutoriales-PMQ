# Laboratorios Big Data  

### **Curso:** ST0263 - Tópicos Especiales en Telemática
### **Título:** Big Data  
### **Objetivo:**

Desarrollar competencias para el uso correcto de AWS EMR, AWS S3, HDFS, HIVE, SPARKQL, PYSPARK. Con enfoque en manejo grandes volúmenes de datos

### **Estudiante:**
- Pablo Moreno Quintero

### Profesor: 
Edwin Montoya - emontoya@eafit.edu.co
---
### 1. Descripción de la actividad

Desarrollar una serie de laboratorios con el proposito de recrear una guía para la fácil replicación de las actividades propuestas en https://github.com/st0263eafit/st0263-242/tree/main/bigdata.
---
### 1.1 Aspectos cumplidos del proyecto

- Realización del laboratorio 0 / [Guía](https://github.com/PabloMorenoEAFIT/ST0263-Tutoriales-PMQ/blob/main/L0-AWS-EMR/L0-AWS-EMR.pdf)
- Realización del laboratorio 1 / [Guía](https://github.com/PabloMorenoEAFIT/ST0263-Tutoriales-PMQ/blob/main/L1-HDFS-HUE-S3/L1-HUE-HDFS.pdf)
- Realización del laboratorio 2 / [Guía](https://github.com/PabloMorenoEAFIT/ST0263-Tutoriales-PMQ/blob/main/L2-HIVE-SPARKSQL/L2-HIVE-SPARKQL.pdf)
- Realización del laboratorio 3 / [Guía](https://github.com/PabloMorenoEAFIT/ST0263-Tutoriales-PMQ/blob/main/L3-NOTEBOOKS-SPARK/L3-NOTEBOOKS-SPARK.pdf)
- Realización del laboratorio Map Reduce
---
### 1.2 Aspectos no cumplidos
(No Aplica)
---
### 2. Arquitectura
![image](https://github.com/user-attachments/assets/01f9a74a-5386-413b-ad93-f9064bd0bb12)

---
### 3. Información adicional del proyecto
#### Características de Big Data utilizando EMR de AWS

Amazon EMR (Elastic MapReduce) es una solución escalable y gestionada que permite procesar y analizar grandes volúmenes de datos mediante herramientas de Big Data en un clúster. Este servicio facilita la integración de tecnologías populares para el análisis de datos, ofreciendo flexibilidad y alta disponibilidad.

## Principales Servicios en EMR

### 1. **Apache Spark**
Apache Spark es un motor de análisis rápido y en memoria que admite procesamiento por lotes y en tiempo real. En EMR, Spark permite:
- Procesar grandes volúmenes de datos de manera eficiente.
- Ejecutar tareas de análisis en memoria, reduciendo el tiempo de cómputo.
- Integrarse fácilmente con otras tecnologías como Hadoop y Hive.

**Casos de uso**:
- Procesamiento de datos en tiempo real.
- Análisis predictivo mediante aprendizaje automático (ML).
- Transformación y limpieza de datos.

---

### 2. **Apache Hive**
Hive es un sistema de almacenamiento de datos construido sobre Hadoop, que utiliza un lenguaje similar a SQL (HiveQL). En EMR, Hive permite:
- Consultar y analizar grandes conjuntos de datos almacenados en S3 o HDFS.
- Simplificar tareas de ETL (extracción, transformación y carga) mediante scripts SQL.

**Casos de uso**:
- Generación de informes.
- Creación de almacenes de datos para análisis empresarial.

---

### 3. **Hue**
Hue es una interfaz web que facilita el uso de herramientas de Big Data en EMR. Funciona como un frontend para interactuar con servicios como Hive, Spark, y HDFS.

**Funciones clave**:
- Permite ejecutar consultas SQL en bases de datos conectadas a EMR.
- Facilita la navegación por el sistema de archivos HDFS o S3.
- Proporciona una interfaz visual para crear scripts y flujos de trabajo.

**Casos de uso**:
- Exploración y visualización de datos.
- Administración de clústeres en EMR.

---

### 4. **Zeppelin**
Apache Zeppelin es una herramienta basada en notebooks que permite realizar análisis interactivo. En EMR, Zeppelin soporta múltiples lenguajes como Python, Scala y SQL.

**Funciones clave**:
- Crear visualizaciones interactivas para análisis de datos.
- Prototipar y ejecutar algoritmos de ML utilizando Spark y PySpark.
- Colaborar en proyectos de análisis en tiempo real.

**Casos de uso**:
- Exploración de datos en un entorno visual.
- Creación de dashboards dinámicos para compartir información.

---

### 5. **PySpark**
PySpark es la API de Python para Apache Spark, que facilita a los desarrolladores utilizar Spark con scripts de Python. En EMR, PySpark permite:
- Realizar transformaciones y acciones en grandes volúmenes de datos.
- Desarrollar modelos de aprendizaje automático usando bibliotecas como MLlib.

**Casos de uso**:
- Análisis de datos científicos.
- Desarrollo rápido de prototipos de análisis.

---

### 6. **SparkSQL**
SparkSQL permite ejecutar consultas SQL en datos estructurados utilizando Spark. Combina la familiaridad del SQL con la potencia del procesamiento distribuido.

**Funciones clave**:
- Consultar datos desde fuentes como S3, HDFS o bases de datos relacionales.
- Combinar SQL con APIs de Spark para transformaciones complejas.

**Casos de uso**:
- Consultas ad hoc en grandes conjuntos de datos.
- Construcción de pipelines ETL.

---

### 7. **Amazon S3**
Amazon S3 (Simple Storage Service) es un almacenamiento escalable utilizado en EMR para:
- Almacenar datos de entrada y salida de procesos de análisis.
- Servir como un repositorio central para datos estructurados y no estructurados.
- Habilitar la separación entre almacenamiento y computación, optimizando costos.

**Casos de uso**:
- Almacenamiento de datos en formato Parquet, ORC, o CSV.
- Copias de seguridad y recuperación de datos.
- Data lakes para análisis en múltiples servicios.

---
## Conexiones Entre Servicios en EMR

1. **Spark y Hive**: SparkSQL puede integrarse con el metastore de Hive para consultas más avanzadas.
2. **Spark y S3**: Spark utiliza `s3a` para acceder directamente a los datos almacenados en Amazon S3.
3. **Hive y S3**: HiveQL permite cargar tablas desde S3 o almacenar resultados de consultas directamente en buckets.
4. **Hue y EMR**: Hue actúa como un panel unificado para gestionar consultas y trabajos en el clúster.
5. **Zeppelin y PySpark**: Zeppelin ejecuta scripts interactivos que usan PySpark para análisis en tiempo real.

---

## Beneficios Generales de Utilizar EMR

1. **Escalabilidad**: Permite añadir o eliminar nodos de clústeres según las necesidades del proyecto.
2. **Costo-Eficiencia**: Integra instancias Spot para reducir costos computacionales.
3. **Integración con AWS**: Compatible con servicios como S3, IAM, CloudWatch y más.
4. **Gestión Simplificada**: Automatiza configuraciones, despliegues y administración de clústeres.
5. **Flexibilidad**: Admite diversas tecnologías y lenguajes de programación para análisis.

---

## Usos Comunes de EMR

- **Procesamiento ETL**: Transformar datos para consumo analítico.
- **Machine Learning**: Entrenamiento de modelos en grandes volúmenes de datos.
- **Análisis de Logs**: Procesar logs de aplicaciones o sitios web.
- **Data Warehousing**: Crear sistemas de análisis con herramientas como Hive y SparkSQL.

EMR es una solución robusta que combina la potencia de tecnologías de Big Data con la flexibilidad de AWS, ideal para proyectos de análisis y procesamiento avanzado de datos.


