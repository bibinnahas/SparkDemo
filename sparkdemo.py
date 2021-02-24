from pyspark.sql import SparkSession
import os

os.environ[
    'PYSPARK_SUBMIT_ARGS'] = '--packages com.amazonaws:aws-java-sdk-pom:1.10.34,org.apache.hadoop:hadoop-aws:2.7.2 ' \
                             'pyspark-shell '

access_key_id = "***"
secret_access_key = "***"

spark = SparkSession.builder.getOrCreate()

# hadoop_conf = spark.sparkContext._jsc

spark._jsc.hadoopConfiguration().set("fs.s3a.access.key", access_key_id)
spark._jsc.hadoopConfiguration().set("fs.s3a.secret.key", secret_access_key)
spark._jsc.hadoopConfiguration().set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
spark._jsc.hadoopConfiguration().set("com.amazonaws.services.s3.enableV4", "true")
spark._jsc.hadoopConfiguration().set("fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a"
                                                                        ".BasicAWSCredentialsProvider")
spark._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "us-east-2.amazonaws.com")
spark._jsc.hadoopConfiguration().set("fs.s3a.path.style.access", "true")

df = spark.read.text('s3a://sparkdemobucketeygds/docker').show

