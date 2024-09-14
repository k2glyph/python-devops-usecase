import boto3

#  Create a cloudformation client

cf=boto3.client("cloudformation", region_name='ap-south-1')

# Cloudformation stack details

stack_name='risk-service-testing'
template_url = 'https://s3.amazonaws.com/path/to/your-template.yaml'  # URL to the CloudFormation template

# Create or update the cloudformation stack

try:
    reponse=cf.create_stack(
        StackName=stack_name,
        TemplateURL=template_url,
        Capabilities=['CAPABILITY_NAMED_IAM'],  # Include if your stack uses IAM resources
    )
    print(f"Cloudformation stack {stack_name} created successfully")
except Exception as e:
    print(f"Error creating/updating stack: {e}")