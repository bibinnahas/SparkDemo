### Spark Demo using EMR/S3/Lambda
#### Tools Used
- S3
- EMR
- Lambda
- Pyspark
  
#### Process Flow
- S3 put operation in input bucket triggers Lambda function
- Lambda function spins up an EMR cluster which runs the spark application
- Spark application reads the parquet file from input bucket and writes it to the output bucket

#### Ways of execution
- Create Lambda function in AWS console using the python code lambda_emr.py, make the trigger as s3 put object to input bucket. Trigger Lambda using s3 put to input bucket
- Run the aws cli command in the file awscli_command_emr directly from a server that has access to s3 (server should have credentials or role set to read/write to s3)

##### Useful links
- https://bartek-blog.github.io/python/spark/2019/04/22/how-to-access-s3-from-pyspark.html
- https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/launch-a-spark-job-in-a-transient-emr-cluster-using-a-lambda-function.html
- https://stackoverflow.com/questions/20461130/building-an-egg-of-my-python-project




