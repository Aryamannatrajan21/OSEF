from .container import get_container_policies
from .kubernetes import get_kubernetes_policies
from .networking import get_networking_policies
from .secrets import get_secrets_policies
from .resources import get_resources_policies

def get_all_policies():
    return (
        get_container_policies() +
        get_kubernetes_policies() +
        get_networking_policies() +
        get_secrets_policies() +
        get_resources_policies()
    )
