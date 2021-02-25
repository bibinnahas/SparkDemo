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


