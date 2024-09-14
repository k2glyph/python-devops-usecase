import boto3

# Create a session

session =boto3.Session(profile_name='ninjacart_snd', region_name='ap-south-1')

# Create a client

ec2=session.client('ec2')

instance_id='Instance-id'
response=ec2.stop_instances(InstanceIds=[instance_id])

print(f'Stop EC2 instance: {instance_id}')