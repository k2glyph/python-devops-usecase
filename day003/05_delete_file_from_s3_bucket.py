import boto3

# Create session
session=boto3.Session(profile_name="profile_name", region_name="ap-south-1")

# Create client
s3=session.client('s3')

bucket_name="bucket_name"
object_name='uploaded-file.txt'

# Delete the file
try:
    s3.delete_object(Bucket=bucket_name, Key=object_name)
    print(f'File {object_name} deleted from bucket {bucket_name}')
except Exception as e:
    print(f'Error deleting file from bucket {bucket_name}: {e}')
