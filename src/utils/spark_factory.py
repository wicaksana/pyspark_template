from pyspark.sql import SparkSession


def get_spark():
    spark = SparkSession\
        .builder\
        .enableHiveSupport()\
        .getOrCreate()
    return spark
