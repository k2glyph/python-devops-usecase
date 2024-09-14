import boto3

# Create session
session=boto3.Session(profile_name="profile_name", region_name='ap-south-1')

# Create budget client
budgets=session.client('budgets')
try:
    budgets.create_budget(
        AccountId="random_account_number",
        Budget={
            'BudgetName': 'Monthly-EC2-Budget',
            'BudgetLimit': {
                'Amount': '1000',  # Set budget amount (in USD)
                'Unit': 'USD'
            },
            'TimeUnit': 'MONTHLY',
            'BudgetType': 'COST',
        },
        NotificationsWithSubscribers=[
            {
                'Notification':{
                    'NotificationType': 'Actual',
                    'ComparisonOperator': "GREATER_THAN",
                    'Threshold': 80.0,
                    'ThresholdType': 'PERCENTAGE'
                },
                'Subscribers':[
                    {
                        'SubscriptionType': 'Email',
                        'Address':'dinesh.k@ninjacart.com'
                    }
                ]
            }
        ]
    )
    print('Budget create and alert setup !')
except Exception as e:
    print(f'Error creating budget: {e}')

