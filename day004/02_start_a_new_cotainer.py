import docker

# Create a Docker client

client=docker.from_env()

# Start a new container

image='nginx:1.27.1-alpine-slim'
try:
    container = client.containers.run(image, detach=True)
    print(f'Started container with ID {container.id}')
except Exception as e:
    print(f'Error creating cotainer of image: {image}. message: {e}')

