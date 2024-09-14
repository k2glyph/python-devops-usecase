import docker

# Create a Docker client

client=docker.from_env()

# list all the container
containers=client.containers.list()

print('Running Containers:')

for container in containers:
    print(f'ID: {container.id}, Name: {container.name}, Status: {container.status}')