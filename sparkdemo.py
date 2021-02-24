from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
import environment_variables
import os

environment_variables.set_variables()

# spark configuration
conf = SparkConf().set('spark.executor.extraJavaOptions', '-Dcom.amazonaws.services.s3.enableV4=true'). \
    set('spark.driver.extraJavaOptions', '-Dcom.amazonaws.services.s3.enableV4=true'). \
    setAppName('pyspark_aws').setMaster('local[*]')

sc = SparkContext(conf=conf)
sc.setSystemProperty('com.amazonaws.services.s3.enableV4', 'true')

access_key_id = str(os.environ['access_key'])
secret_key_ud = str(os.environ['secret_key'])
input_bucket_name = str(os.environ['input_bucket'])
output_bucket_name = str(os.environ['output_bucket'])

hadoopConf = sc._jsc.hadoopConfiguration()
hadoopConf.set('fs.s3a.access.key', access_key_id)
hadoopConf.set('fs.s3a.secret.key', secret_key_ud)
hadoopConf.set('fs.s3a.endpoint', 's3-us-east-2.amazonaws.com')
hadoopConf.set('fs.s3a.impl', 'org.apache.hadoop.fs.s3a.S3AFileSystem')

spark = SparkSession(sc)

# input_path = "s3a://" + input_bucket_name + file_name

df = spark.read.parquet('s3a://sparkdemobucketeygds/*.parquet')
df.write.mode("OVERWRITE").parquet('s3a://mydemooutputbuck/output/')
