from pyspark.sql import SparkSession
from delta.tables import *

def clean_data(table_name):
    spark = SparkSession.builder.appName("Data Cleaning").getOrCreate()

    
    delta_table = DeltaTable.forPath(spark, f"/mnt/delta/{table_name}")

    
    df = delta_table.toDF()
    cleaned_df = df.dropna().dropDuplicates()

    
    cleaned_df.write.format("delta").mode("overwrite").save(f"/mnt/delta/{table_name}")

if __name__ == "__main__":
    clean_data("expenditures")