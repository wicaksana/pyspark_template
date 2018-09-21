# https://github.com/Soluto/spark-submit-with-pyspark-template

from src.utils.logger import Logger
from src.utils.spark_factory import get_spark


def run():
    spark = get_spark()
    sc = spark.sparkContext
    logger = Logger(sc)

    # Logic goes here


if __name__ == '__main__':
    run()
