import boto3

# Create session

session=boto3.Session(profile_name='ninjacart_snd', region_name="ap-south-1")

# Create client
s3=session.client('s3')

file_name=".gitlab-ci.yml"
bucket_name="hetzner-cluster-etcd-backup"
object_name='uploaded-file.txt'

# upload files

try:
    s3.upload_file(file_name, bucket_name, object_name)
    print(f"file {file_name} uploaded to {bucket_name}/{object_name}")
except Exception as e:
    print(f"Error uploading file: {e}")