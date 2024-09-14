import boto3

# Create session with aws credentials

session=boto3.Session(profile_name='hetzner_ninjacart')

# create client
s3=session.client('s3')

# list buckets
response=s3.list_buckets()
print("S3 Buckets:")
for bucket in response['Buckets']:
    print(f'- {bucket["Name"]}')