import boto3

# Create session
session=boto3.Session(profile_name='profile-name', region_name='ap-south-1')

# Create client cloudwatch
cloudwatch=session.client('cloudwatch')

# Create an alarm for EC2 CPU Utilization
try:
    response=cloudwatch.put_metric_alarm(
        AlarmName="HIGH-CPU-UTILIZATION",
        MetricName="CPUUTILIZATION",
        Namespace='AWS/EC2',
        Statistic='Average',
        Dimensions=[
            {'Name': 'InstanceId', 'Value': 'your-instance-id'}
        ],
        Period=300,
        EvaluationPeriods=1,
        Threshold=80.0,
        ComparisonOperator='GreaterThanThreshold',
        AlarmActions=['sns-topic-arn']
    )
    print('Cloudwatch alarm created')
except Exception as e:
    print(f'Exception occur while trying to create cloudalarm: {e}')