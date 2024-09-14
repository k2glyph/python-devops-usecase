- Scripting & Automation
    - Creating report
    - Rotate database password
    - Read a csv file, read csv file from s3 
    - python integration with ansible
    - python integration with terraform
    - python integration with docker
    - python integration with kubernetes
    - python integration with prometheus like exact metrics from ec2
    - python library: psutils, flask
    - Python pandas, matplotlib

Use cases:
- Currently AWS automation using boto3 and server management using Fabric
- Various ETL projects getting some fairly gnarly data from various platforms imported into a DW. Subsequent processing of the same data to produce accurate cost information
- Energy cost modelling. Producing a model which accurately predicts per customer energy usage.
- Network cost modelling. Producing software which accurately reports per-customer network transit costs. (This also goes well into big-data territory with ca 1010 records per month to process).
- Large scale simulation (1Tn) packets of network data to determine optimum sampling rates.
- Out of band bulk server management tools.
- Network inventory software including using e.g. fuzzy logic to reconcile real-world data with that in the backend DB.
- Various activities related to bulk patching of security vulnerabilities.
- Development of Python bindings/wrappers around various APIs.
- Oh I've just remembered developed some symmetric encryption code which AES encrypts things like database credentials at rest and then decrypts them on the fly when required by an application.

I'm not a DevOps Engineer, just a sysadmin, but we mainly work on AWS and recently our Network Engineer asked me for help to deploy Cloudformation stacks. I wrote a script that takes a custom config I made with configparser, where you can set IPs, ports and endpoint services, then run the script have have a fully templated CF template using Jinja2. I barely know anything about Cloudformations role, but it was very fun to work on it.

Other stuff I do with Python is mainly automating manual tasks. There's this cool tool called script-server that you can deploy in your org to have a nice front-end for the users, and a secure back-end that runs the scripts. We use for a lot of things.


As a real-world example, I've use Python a lot in conjunction with AWS Lambda to automate MS SQL Server updates, adding users, verifying the right configs are in tables, etc. This is something you can't really do cleanly in Ansible and just goes a lot faster by running it in Lambda. Python also makes quick work of APIs using Lambda and API Gateway in AWS as well. The AWS SAM CLI is a great place to start for this, but I have a crisp pipeline that deploys all the infrastructure for this via Terraform. We require our Lambda functions to run in a VPC that has access to the databases privately, so we deploy a separate function in each account, with API gateway only being in a shared account. Depending on what is chosen, it knows which Lambda function in what account to use. I also split it up so the actual building and storing of the Lambda app is done in one Terraform state while the actual deploying of the Lambda function and API Gateway setup is done after. This means I also can detect changes in zip file via s3, it's in a shared spot, and it's dirt cheap to run. I think most months it costs us like 50 cents.

If you combine Lambda and Python correctly, it can take some of those less-than-pretty automation tasks and make them look really nice.


Recently made a script to automate our terraform upgrade. We're going from 0.13->0.14 and I created a small script to do everything. It'll be easy to modify it to go from 0.14->1.0 in the future.

Many many small automations have been made similar to this using Python.



I personally mostly use Python to make integrations. Taking data from one place using rest api, and probably reformating it a bit and pushing it to some other place, using rest api.

I install it and then install the modules and then have to venv it or dockerize it because the data analysts get stuck in a specific version… and then i have to reach the analysts to venv it or how to use docker…



get a .war from ftp and replacing the running web application, emails the result of a test after the start is done.

Talk to AWS, Pandas, and Numpy

I built a bit of software designed to facilitate a migration of our SCM system to GitHub using Python. I've also built a tonne of lambdas designed to clean up our AWS Accounts, monitor logs/security groups, and automatically manage our GitHub organisation. In general, my team uses python to automatically create Hashicorp Vault access policies based on data in our inventory management system (a Flask app), and to automatically create AWS accounts and add their billing details/sign in details to Vault/our asset system.


Real world:

Ansible Modules - Allow me to automate stuff. I mostly just contribute bug fixes or docs.

Related to Ansible, I love to load test my Ansible configs so I can see whether adding things like Redis or DB Read Replicas makes a difference on how much load my site can take. Either manually script it or use Locust Framework. With Terraform you can set up a really powerful Locust swarm to load test and then tear down.

Anything quick and dirty. Examples: a) easy 100 liner that does some DB queries, gets the number of people with MFA turned on at my Org and then send to a spreadsheet that gets pulled into other reports or diagrams. b) Script that runs on our monitoring system to set the default values of warning and alarm limits using their API.


I recently wrote a script that does ec2 instance lifecycle management. Updates launch configs, ups autoscale group to double, waits for readiness, reduce autoscale group to original size based on age. Essentially k8s lifecycle management using ec2 VM's instead of containers.


Almost everything, both on work and at home.

Examples: I like working with python when talking to certain modbus devices (such as my inverter)

It takes 20 lines of code to set stuff up, let it post metrics to an MQTT endpoint, and maybe expose on an API endpoint with flask, so my telegram bot can fetch realtime data


AWS lambda service that manages letsencrypt certs in ACM. (for. . . reasons. Stupid reasons).

Also; volume snapshot backup/rotation script, (wrote my own with a custom grooming method to suit my company's batshit requirements)

also some nifty one-liners for xml wrangling.

I’ve used it for so many things over the years. Right now, I’m setting up an API for a server provisioning endpoint that does IaC with GitHub commits. It uses fastapi (along with slowapi for rate limiting). It also has a simple locking mechanism for parallel activities to get around some peculiarities of what our Network Team wants and doesn’t want to do.


Python is one of the most powerful language to work on. One of my script which I wrote in python was to Dataset Generation from the logs of website (server) into an excel sheet.
Logs contains -

IP Address -
DateTime Visited -
OS used by client -

And it was dynamic with only python, concepts of regular expression was used

I use it to write an idempotent postgres script. It allows me to define databases, users, extensions, roles, etc via YAML and the python script would simply create those if they do not yet exist.

Cloning any AWS server on a press of a button, or executing DB cleanup tasks on a weekly basis - as some of the more recent examples.

Mainly scripts around handling data or data quality (SQL based checks). Lately switched projects and did some scripting on custom resources in kubernetes. https://github.com/sigviper/python-kubernetes

Build machine learning pipelines. Check out kubeflow pipelines.

Some things I've written over the years:

Basic CD tool that uses boto3 to run SSM commands against EC2 instances (in our case, it was used to trigger a local Ansible run)

A bunch of Nagios, Jira, and GitHub scripts

Kubernetes namespace/database cleanup tool for automatically nuking dev environments if a branch is deleted from GitHub or if the environment is unused

More involved EKS CD tool that supports multiple AWS accounts, Vault/SecretsManager secrets, templating Helm charts, custom namespaces based on branch name, and ECR docker builds. Currently waiting for our company lawyer to okay open-sourcing it. The point was to build IAM auth into the tool itself.

Script for setting up awscli config to work with AWS SSO then automatically login to a kube cluster in another account (avoids lots of manual work when dealing with 10-20 kube clusters)

AWS Lambda to scan third-party IP list and restric specific security groups to only those IP ranges


I write test automation code in Python (underneath Robot Framework). Everything from sending and reading messages from Kafka to using pandas to compare data sets.


Potentially not mentioned - I use python regularly in my terminal-based workflow

python -c "print(len('somelongstringimvalidating'))";

prints the character count without opening up an IDE or browser

:%!python -m json.tool

in Vim; prettify JSON

python -m http.server 8888

Create a quick web-server at current directory. Really handy for sharing something quickly between two PC (or mobile device). No extra messaging apps or programs required

You wanted real world examples :)


CI/CD and Configuration Management Pipelines: SaltStack, Ansible
Deployment: Fabric, Cuisine
Cloud Automation: Boto, major cloud providers have Python SDKs, most CLIs (AWS, Google Cloud) are written in Python
More DevOps Tools: Docker Compose, Ambassador API Gateway, Apache Libcloud are handy DevOps tools developed in Python.
More relatevely fresh domains: AIOps, MLOps, ModelOps


I wrote a script to automatically submit tickets through our internal ticketing system so my boss didn't need to submit 60 some tickets manually. Unfortunately the API for the ticketing system (and the system itself) is a mess and has no documentation that I could find, so the script is a little touchy and doesn't always successfully submit every ticket, but it did really cut down the amount of tickets they had to submit, so partial success.

I've also used it to parse inventory files for Ansible from CSV files.

