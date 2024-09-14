from python_terraform import Terraform

# Create a terraform object
tf=Terraform()

# Initialize the terraform directory (where .tf files are)

tf.init()

# Apply Terraform to provision resources
return_code, stdout, stderr=tf.apply(skip_plan=True)

if return_code==0:
    print("Terraform apply successfully")
else:
    print(f'Terraform apply failed with error: {stderr}')