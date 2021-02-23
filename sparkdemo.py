from pyspark.sql import SparkSession
import os

os.environ[
    'PYSPARK_SUBMIT_ARGS'] = '--packages com.amazonaws:aws-java-sdk-pom:1.10.34,org.apache.hadoop:hadoop-aws:2.7.2 pyspark-shell'

from pyspark.python.pyspark.shell import spark

access_key_id = "**"
secret_access_key = "**/**"

spark = SparkSession.builder.getOrCreate()

hadoop_conf = spark.sparkContext._jsc

# Setup spark to use s3, and point it to the moto server.
hadoop_conf = spark.sparkContext._jsc.hadoopConfiguration()
hadoop_conf.set("fs.s3.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
hadoop_conf.set("fs.s3a.access.key", access_key_id)
hadoop_conf.set("fs.s3a.secret.key", secret_access_key)
hadoop_conf.set("fs.s3a.endpoint", "us-east-2.amazonaws.com")
hadoop_conf.set("com.amazonaws.services.s3.enableV4", "true")
hadoop_conf.set("fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.BasicAWSCredentialsProvider")

# spark._jsc.hadoopConfiguration().set("fs.s3a.access.key", access_key_id)
# spark._jsc.hadoopConfiguration().set("fs.s3a.secret.key", secret_access_key)
# spark._jsc.hadoopConfiguration().set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
# spark._jsc.hadoopConfiguration().set("com.amazonaws.services.s3.enableV4", "true")
# spark._jsc.hadoopConfiguration().set("fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a"
#                                                                         ".BasicAWSCredentialsProvider")
# spark._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "us-east-2.amazonaws.com")

# conn = boto3.resource("s3", endpoint_url="http://127.0.0.1:5000")
# conn.create_bucket(Bucket="sparkdemobucketeygds")

df = spark.read.text("s3a://sparkdemobucketeygds/docker").show

# import os
# import pyspark
# os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages com.amazonaws:aws-java-sdk-pom:1.10.34,org.apache.hadoop:hadoop-aws:2.7.2 pyspark-shell'
# from pyspark.sql import SQLContext
# from pyspark import SparkContext
# sc = SparkContext()
# sqlContext = SQLContext(sc)
#
#
# filePath = "s3a://sparkdemobucketeygds/docker"
# df = spark.read.text(filePath)  # Parquet file read example
