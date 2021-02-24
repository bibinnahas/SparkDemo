from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
import os


def set_variables():
    os.environ['access_key'] = "**"
    os.environ['secret_key'] = "**"
    os.environ['input_bucket'] = "sparkdemobucketeygds"
    os.environ['output_bucket'] = "mydemooutputbuck"


set_variables()

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

from datetime import datetime

now = datetime.now()  # current date and time

year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")
time = now.strftime("%H:%M:%S")
date_time = now.strftime("%d%m%Y_%H%M%S")

input_path = "s3a://" + input_bucket_name + "/" + "*.parquet"
output_path = "s3a://" + output_bucket_name + "/" + date_time + "/"

print("input s3 path is in " + input_path)
print("output s3 path is in" + output_path)

df = spark.read.parquet(input_path)
print("Dataframe was read from " + input_path)
df.write.mode("OVERWRITE").parquet(output_path)

