import boto3
from datetime import datetime, timedelta
# create session
session=boto3.Session(profile_name="profile_name", region_name="ap-south-1")

# create client
cloudwatch=session.client("cloudwatch")
instance_id="i-0261059484b138b54"

cpu_response=cloudwatch.get_metric_statistics(
    Namespace="AWS/EC2",
    MetricName="CPUUtilization",
    Dimensions=[
        {'Name': "InstanceId", "Value": instance_id},
    ],
    StartTime=datetime.utcnow()-timedelta(hours=1),
    EndTime=datetime.utcnow(),
    Period=300, # 5 minute interval
    Statistics=['Average']
)
# Get EC2 Memory utilization for the past 1 hour (from CloudWatch agent)
memory_response = cloudwatch.get_metric_statistics(
    Namespace='CWAgent',  # Custom namespace for CloudWatch agent metrics
    MetricName='mem_used_percent',  # Memory utilization metric
    Dimensions=[
        {'Name': 'InstanceId', 'Value': instance_id}  # Replace with your EC2 instance ID
    ],
    StartTime=datetime.utcnow() - timedelta(hours=1),
    EndTime=datetime.utcnow(),
    Period=300,  # 5-minute intervals
    Statistics=['Average'],
)
print("CPU Utilization Data:")
for datapoint in cpu_response['Datapoints']:
    print(f"Time:{datapoint['Timestamp']} Average CPU Utilization: {datapoint['Average']:.2f}%")


print("\nMemory Utilization Data:")
for datapoint in memory_response['Datapoints']:
    print(f"Time:{datapoint['Timestamp']} Average Memory Utilization: {datapoint['Average']:.2f}%")