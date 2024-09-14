from kubernetes import client, config

# load kubeconfig
config.load_kube_config()

# Create kubernetes api client
v1=client.CoreV1Api()

# define a new pod
pod=client.V1Pod(
    metadata=client.V1ObjectMeta(name='example-pod'),
    spec=client.V1PodSpec(
        containers=[client.V1Container(
            name='example-container',
            image='nginx:latest',
            ports=[client.V1ContainerPort(container_port=80)]
        )]
    )
)

# Create the pod
v1.create_namespaced_pod(namespace='default', body=pod)
print('Created a new pod in default namespace')