import boto3

# create session
session=boto3.Session(profile_name='ninjacart_snd', region_name='ap-south-1')

# Create an EC2 client

ec2=session.client('ec2')

# list instances
response=ec2.describe_instances()

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_name= "No Name"
        if 'Tags' in instance:
            for tag in instance['Tags']:
                if tag['Key']=='Name':
                    instance_name=tag['Value']
        print(f"Instance Name: {instance_name}, Intances ID: {instance['InstanceId']}, State: {instance['State']['Name']}")