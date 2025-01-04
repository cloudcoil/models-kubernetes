# cloudcoil

Cloud native made easy with Python

### PyPI stats

[![PyPI](https://img.shields.io/pypi/v/cloudcoil.svg)](https://pypi.python.org/pypi/cloudcoil)
[![Versions](https://img.shields.io/pypi/pyversions/cloudcoil.svg)](https://github.com/cloudcoil/cloudcoil)

[![Downloads](https://static.pepy.tech/badge/cloudcoil)](https://pepy.tech/project/cloudcoil)
[![Downloads/month](https://static.pepy.tech/badge/cloudcoil/month)](https://pepy.tech/project/cloudcoil)
[![Downloads/week](https://static.pepy.tech/badge/cloudcoil/week)](https://pepy.tech/project/cloudcoil)

### Repo information

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/license/apache-2-0/)
[![CI](https://github.com/cloudcoil/cloudcoil/actions/workflows/ci.yml/badge.svg)](https://github.com/cloudcoil/cloudcoil/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/cloudcoil/cloudcoil/branch/main/graph/badge.svg)](https://codecov.io/gh/cloudcoil/cloudcoil)

## Installation

```bash
# Minimal dependencies
# pydantic, httpx and pyyaml
uv add cloudcoil
```

## Quick Start

```python
from pathlib import Path

# Config is the core way to interact with your Kubernetes API Server
from cloudcoil.client import Config
from cloudcoil.client import errors
# All default kubernetes types are neatly arranged
# with appropriate apiversions as module paths
from cloudcoil.models.default.apps import v1 as apps_v1
from cloudcoil.models.default.core import v1 as core_v1
from cloudcoil.models.default.batch import v1 as batch_v1


# Uses the default config based on KUBECONFIG
# Feels just as natural as kubectl
# But comes with full pydantic validation
kubernetes_service = core_v1.Service.get("kubernetes")

# You can create temporary config contexts
# This is similar to doing kubens kube-system
with Config(namespace="kube-system"):
    # This searches for deployments in the kube-system namespace
    core_dns_deployment = apps_v1.Deployment.get("core-dns")
    # Also comes with async client out of the box!
    kube_dns_service = await core_v1.Service.async_get("kube-dns")

# Create new objects with generate name easily
test_namespace = core_v1.Namespace(metadata=dict(generate_name="test-")).create()
# You can also modify the object and update it
test_namespace.metadata.labels = {"test": "true"}
# Get the new value of the test namespace back from the server
# after updating it
test_namespace = test_namespace.update()

# You can also easily fetch namespace using
kube_system_namespace = core_v1.Namespace()
kube_system_namespace.name = "kube-system"
# Fetch the latest version of the namespace from the server
kube_system_namespace = kube_system_namespace.fetch()

# We can access the output from the APIServer from the create method
# Switch to the new namespace
with Config(namespace=test_namespace.metadata.name):
    try:
        core_dns_deployment = apps_v1.Deployment.get("core-dns")
    except errors.ResourceNotFound:
        pass

# Finally you can remove the namespace
# And also inspect the output to ensure it is terminating
test_namespace.remove().status.phase == "Terminating"
# You can also delete it using the name/namespace if you wish
core_v1.Namespace.delete(name=test_namespace.metadata.name)

# You can also parse kubernetes resource easily
from cloudcoil import resources
# Let's assume we have a hello-world.yaml file that looks like so
# apiVersion: batch/v1
# kind: Job
# metadata:
#   name: hello-world
# spec:
#   template:
#     spec:
#       containers:
#       - name: hello-world
#         image: ubuntu
#         command: ["echo", "Hello, World!"]
#       restartPolicy: Never
job = resources.parse_file("hello-world.yaml")
# It is serialized to the correc type
assert isinstance(job, batch_v1.Job)
# You can now create the job
job.create()
# You can also access different registered models by name
Job = resources.get_model("Job")
# Now you can parse the file using the from_file classmethod
job = Job.from_file("hello-world.yaml")
# the above is correctly typed with mypy if you use the cloudcoil mypy extension
# even though the class was dynamically loaded from the scheme via a string
# reveal_type(job) == cloudcoil.models.default.batch.v1.Job

# Listing resources
# cloudcoil provides two ways to list resources:

# 1. Iterator API (Recommended)
# This automatically handles pagination and provides a clean interface
for pod in core_v1.Pod.list(all_namespaces=True):
    print(pod.metadata.name)

# For async code, you can use async iteration
async for pod in await core_v1.Pod.async_list(all_namespaces=True):
    print(pod.metadata.name)

# Get total count for all items
total_pods = len(pods)
print(f"Total pods: {total_pods}")


# 2. Manual Pagination API
# If you need more control over pagination, you can use the raw API
# This returns a ResourceList object that contains the first page
pods = core_v1.Pod.list(namespace="kube-system", limit=10)
print(f"First page has {len(pods.items)} items")

# Access the items directly using the items attribute
for pod in pods.items:
    print(pod.metadata.name)

# Check if there are more pages
if pods.has_next_page():
    # Get the next page
    next_page = pods.get_next_page()
    # For async code
    next_page = await pods.async_get_next_page()

# It's recommended to use the Iterator API as it handles pagination
# automatically and provides a more ergonomic interface
```

### Testing Integration

cloudcoil includes pytest fixtures to help you test your Kubernetes applications. Install with test dependencies:

```bash
uv add cloudcoil[test]
```

The testing integration provides two key fixtures:

- `test_cluster`: Creates and manages a k3d cluster for testing
- `test_config`: Provides a Config instance configured for the test cluster

Example usage:

```python
import pytest
from cloudcoil.models.default.core import v1 as corev1

@pytest.mark.configure_test_cluster(
    cluster_name="my-test-cluster",
    k3d_version="v5.7.5",
    k8s_version="v1.31.4",
    remove=True
)
def test_my_resources(test_config):
    with test_config:
        namespace = corev1.Namespace.get("default")
        assert namespace.metadata.name == "default"
```

#### Test Cluster Configuration

The `configure_test_cluster` mark accepts these arguments:

- `cluster_name`: Name of the test cluster (default: auto-generated)
- `k3d_version`: Version of k3d to use (default: v5.7.5)
- `k8s_version`: Kubernetes version to use (default: v1.31.4)
- `k8s_image`: Custom k3s image (default: rancher/k3s:{k8s_version}-k3s1)
- `remove`: Whether to remove the cluster after tests (default: True)

## mypy Integration

cloudcoil provides a mypy plugin that enables type checking for dynamically loaded kinds from the scheme. To enable the plugin, add this to your pyproject.toml:

```toml
[tool.mypy]
plugins = ['cloudcoil.mypy']
```

This plugin enables full type checking for scheme.get() calls when the kind name is a string literal:

```python
from cloudcoil import scheme

# This will be correctly typed as batch_v1.Job
job_class = scheme.get("Job")

# Type checking works on the returned class
job = job_class(
    metadata={"name": "test"},  # type checked!
    spec={
        "template": {
            "spec": {
                "containers": [{"name": "test", "image": "test"}],
                "restartPolicy": "Never"
            }
        }
    }
)
```

## Documentation

For full documentation, please visit [cloudcoil.github.io/cloudcoil](https://cloudcoil.github.io/cloudcoil)

## License

This project is licensed under the Apache License, Version 2.0 - see the [LICENSE](https://github.com/cloudcoil/cloudcoil/blob/main/LICENSE) file for details.
