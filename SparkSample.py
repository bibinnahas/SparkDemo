from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import os

os.environ["AWS_SECRET_KEY_ID"] = "**"
os.environ["AWS_SECRET_ACCESS_KEY"] = "**"
os.environ[
    'PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.hadoop:hadoop-aws:2.7.4 ' \
                             'pyspark-shell '

spark = SparkSession.builder.appName("SimpleApp").getOrCreate()

df = spark.createDataFrame(
    [(0, 0, 4.0), (0, 1, 2.0), (0, 3, 3.0), (1, 0, 4.0), (1, 1, 1.0), (1, 2, 5.0)],
    ["user", "item", "rating"]
)

df_pandas = df.groupBy("user").agg(F.count(F.col("item"))).toPandas()
print(df_pandas)

# import com.amazonaws.SDKGlobalConfiguration
# System.setProperty(SDKGlobalConfiguration.ENABLE_S3_SIGV4_SYSTEM_PROPERTY, "true")

# Setup spark to use s3, and point it to the moto server.
# hadoop_conf = spark.sparkContext._jsc.hadoopConfiguration()
# hadoop_conf.set("fs.s3.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
# hadoop_conf.set("fs.s3a.access.key", os.environ.get('AWS_SECRET_KEY_ID'))
# hadoop_conf.set("fs.s3a.secret.key", os.environ.get('AWS_SECRET_ACCESS_KEY'))
# hadoop_conf.set("fs.s3a.endpoint", "s3.us-east-2.amazonaws.com")
# hadoop_conf.set("com.amazonaws.services.s3.enableV4", "true")
# hadoop_conf.set("fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.BasicAWSCredentialsProvider")

spark._jsc.hadoopConfiguration().set("fs.s3a.access.key", os.environ.get('AWS_SECRET_KEY_ID'))
spark._jsc.hadoopConfiguration().set("fs.s3a.secret.key", os.environ.get('AWS_SECRET_ACCESS_KEY'))
spark._jsc.hadoopConfiguration().set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
spark._jsc.hadoopConfiguration().set("com.amazonaws.services.s3.enableV4", "true")
spark._jsc.hadoopConfiguration().set("fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a"
                                                                        ".TemporaryAWSCredentialsProvider")
# spark._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "s3.us-east-2.amazonaws.com")
# spark._jsc.hadoopConfiguration().set("fs.s3a.path.style.access", "true")

df = spark.read.text('s3a://sparkdemobucketeygds/docker')

spark.stop()
