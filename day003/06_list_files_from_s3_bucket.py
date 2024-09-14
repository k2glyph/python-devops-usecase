import boto3

# Create session

session=boto3.Session(profile_name='profile_name', region_name='ap-south-1')

# Create client
s3=session.client('s3')

bucket_name="bucket_name"

# list all the object in the bucket

try:
    response=s3.list_objects_v2(Bucket=bucket_name)

    # Check if the bucket contains any files

    if 'Contents' in response:
        print(f'Files in bucket {bucket_name}:')
        for obj in response['Contents']:
            print(obj['Key']) # Print the file (object) name
    else:
        print(f'No files found in the bucket {bucket_name}')
except Exception as e:
    print(f'Errors listing files from bucket {bucket_name}')