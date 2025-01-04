# Generated by cloudcoil-model-codegen v0.0.14
# DO NOT EDIT

from __future__ import annotations

from typing import Annotated, Dict, List, Literal, Optional

from pydantic import Field

from cloudcoil import apimachinery
from cloudcoil._pydantic import BaseModel
from cloudcoil.resources import Resource, ResourceList

from ..core import v1


class Scheduling(BaseModel):
    node_selector: Annotated[
        Optional[Dict[str, str]],
        Field(
            alias="nodeSelector",
            description="nodeSelector lists labels that must be present on nodes that support this RuntimeClass. Pods using this RuntimeClass can only be scheduled to a node matched by this selector. The RuntimeClass nodeSelector is merged with a pod's existing nodeSelector. Any conflicts will cause the pod to be rejected in admission.",
        ),
    ] = None
    tolerations: Annotated[
        Optional[List[v1.Toleration]],
        Field(
            description="tolerations are appended (excluding duplicates) to pods running with this RuntimeClass during admission, effectively unioning the set of nodes tolerated by the pod and the RuntimeClass."
        ),
    ] = None


class Overhead(BaseModel):
    pod_fixed: Annotated[
        Optional[Dict[str, apimachinery.Quantity]],
        Field(
            alias="podFixed",
            description="podFixed represents the fixed resource overhead associated with running a pod.",
        ),
    ] = None


class RuntimeClass(Resource):
    api_version: Annotated[
        Optional[Literal["node.k8s.io/v1"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "node.k8s.io/v1"
    handler: Annotated[
        str,
        Field(
            description='handler specifies the underlying runtime and configuration that the CRI implementation will use to handle pods of this class. The possible values are specific to the node & CRI configuration.  It is assumed that all handlers are available on every node, and handlers of the same name are equivalent on every node. For example, a handler called "runc" might specify that the runc OCI runtime (using native Linux containers) will be used to run the containers in a pod. The Handler must be lowercase, conform to the DNS Label (RFC 1123) requirements, and is immutable.'
        ),
    ]
    kind: Annotated[
        Optional[Literal["RuntimeClass"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "RuntimeClass"
    metadata: Annotated[
        Optional[apimachinery.ObjectMeta],
        Field(
            description="More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    ] = None
    overhead: Annotated[
        Optional[Overhead],
        Field(
            description="overhead represents the resource overhead associated with running a pod for a given RuntimeClass. For more details, see\n https://kubernetes.io/docs/concepts/scheduling-eviction/pod-overhead/"
        ),
    ] = None
    scheduling: Annotated[
        Optional[Scheduling],
        Field(
            description="scheduling holds the scheduling constraints to ensure that pods running with this RuntimeClass are scheduled to nodes that support it. If scheduling is nil, this RuntimeClass is assumed to be supported by all nodes."
        ),
    ] = None


RuntimeClassList = ResourceList["RuntimeClass"]
