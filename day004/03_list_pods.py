from kubernetes import client, config

# load kubeconfig
config.load_kube_config() # Use config.load_incluster_config() if running inside a cluster

# create kubernetes api client
v1=client.CoreV1Api()

# List all pods in kube-system namespace

pods=v1.list_namespaced_pod(namespace='kube-system')
print("Pods in the default namespace: ")
for pod in pods.items:
    print(f'Name: {pod.metadata.name}, Status:{pod.status.phase}')
    