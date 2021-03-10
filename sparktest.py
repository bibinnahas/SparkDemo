from typing import List

from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
import os

# spark configuration
conf = SparkConf().setAppName('spark_test').setMaster('local[*]')

sc = SparkContext(conf=conf)

spark = SparkSession(sc)

from pyspark.sql.types import StructType, StructField, StringType, IntegerType

new_schema = StructType([
    StructField("action", StringType(), True),
    StructField("event_id", StringType(), True),
    StructField("timestamp", StringType(), True),
    StructField("url", StringType(), True),
])

# inferred_schema = StructType(
#     List(
#         StructField(action, StringType, true),
#         StructField(event_id, StringType, true),
#         StructField(timestamp, StringType, true),
#         StructField(url, StringType, true)
#     ))

dF = spark \
    .read \
    .json("/home/thesnibibin/Desktop/sample.json", new_schema)

dF.show()
print(dF.schema.json())

schema_json = dF.schema.json()

schemaa = [i for i in dF.schema]
NewSchema = StructType(schemaa)

print(NewSchema)

a = spark.sparkContext._jvm.org.apache.spark.sql.types.DataType.fromJson(schema_json).toDDL()

print(a)