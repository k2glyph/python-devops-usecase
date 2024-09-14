import boto3

# Create session

session=boto3.Session(profile_name="ninjacart_snd", region_name="ap-south-1")

# Create client
ec2=session.client("ec2")

# Start a ec2 instance
instance_id='your-instance-id'
response=ec2.start_instances(InstanceIds=[instance_id])

print(f'Started ec2 instance: {instance_id}')