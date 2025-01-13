import pyspark
from pyspark.sql import SparkSession
from delta import *

def create_spark_session():
    spark = (SparkSession.builder
             .appName("Financial Data Ingestion")
             .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
             .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
             .getOrCreate())
    return spark

def ingest_data(file_path, table_name):
    spark = create_spark_session()

    
    df = spark.read.csv(file_path, header=True, inferSchema=True)

    
    df.write.format("delta").mode("append").save(f"/mnt/delta/{table_name}")

if __name__ == "__main__":
    ingest_data("s3://government-budgets/expenditures.csv", "expenditures")












    