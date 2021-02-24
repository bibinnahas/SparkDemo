import boto3
import os

import com.amazonaws.SDKGlobalConfiguration
System.setProperty(SDKGlobalConfiguration.ENABLE_S3_SIGV4_SYSTEM_PROPERTY, "true")

session = boto3.Session(profile_name='myaws')
s3 = session.resource('s3')
os.environ["AWS_SECRET_KEY_ID"] = "***"
os.environ["AWS_SECRET_ACCESS_KEY"] = "***"
import os

aws_access_key_id = os.environ.get('AWS_SECRET_KEY_ID')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key)
print(list(s3.buckets.all()))
