import boto3

# Create a cloudformation client

cf=boto3.client('cloudformation', region_name='ap-south-1')

# Cloudformation stack name
stack_name='risk-service-testing'

# Delete the cloudformation stack

try:
    cf.delete_stack(StackName=stack_name)
    print(f'Cloudformation stack {stack_name} deleted successfully')
except Exception as e:
    print(f'Error while trying to delete stack_name: {stack_name} message: {e}')