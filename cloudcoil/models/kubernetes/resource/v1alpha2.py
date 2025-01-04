# Generated by cloudcoil-model-codegen v0.0.16
# DO NOT EDIT

from __future__ import annotations

from typing import Annotated, List, Literal, Optional

from pydantic import Field

from cloudcoil import apimachinery
from cloudcoil._pydantic import BaseModel
from cloudcoil.resources import Resource, ResourceList

from ..core import v1


class NamedResourcesAllocationResult(BaseModel):
    name: Annotated[str, Field(description="Name is the name of the selected resource instance.")]


class NamedResourcesFilter(BaseModel):
    selector: Annotated[
        str,
        Field(
            description='Selector is a CEL expression which must evaluate to true if a resource instance is suitable. The language is as defined in https://kubernetes.io/docs/reference/using-api/cel/\n\nIn addition, for each type NamedResourcesin AttributeValue there is a map that resolves to the corresponding value of the instance under evaluation. For example:\n\n   attributes.quantity["a"].isGreaterThan(quantity("0")) &&\n   attributes.stringslice["b"].isSorted()'
        ),
    ]


class NamedResourcesIntSlice(BaseModel):
    ints: Annotated[List[int], Field(description="Ints is the slice of 64-bit integers.")]


class NamedResourcesRequest(BaseModel):
    selector: Annotated[
        str,
        Field(
            description='Selector is a CEL expression which must evaluate to true if a resource instance is suitable. The language is as defined in https://kubernetes.io/docs/reference/using-api/cel/\n\nIn addition, for each type NamedResourcesin AttributeValue there is a map that resolves to the corresponding value of the instance under evaluation. For example:\n\n   attributes.quantity["a"].isGreaterThan(quantity("0")) &&\n   attributes.stringslice["b"].isSorted()'
        ),
    ]


class NamedResourcesStringSlice(BaseModel):
    strings: Annotated[List[str], Field(description="Strings is the slice of strings.")]


class PodSchedulingContextSpec(BaseModel):
    potential_nodes: Annotated[
        Optional[List[str]],
        Field(
            alias="potentialNodes",
            description="PotentialNodes lists nodes where the Pod might be able to run.\n\nThe size of this field is limited to 128. This is large enough for many clusters. Larger clusters may need more attempts to find a node that suits all pending resources. This may get increased in the future, but not reduced.",
        ),
    ] = None
    selected_node: Annotated[
        Optional[str],
        Field(
            alias="selectedNode",
            description='SelectedNode is the node for which allocation of ResourceClaims that are referenced by the Pod and that use "WaitForFirstConsumer" allocation is to be attempted.',
        ),
    ] = None


class ResourceClaimConsumerReference(BaseModel):
    api_group: Annotated[
        Optional[str],
        Field(
            alias="apiGroup",
            description="APIGroup is the group for the resource being referenced. It is empty for the core API. This matches the group in the APIVersion that is used when creating the resources.",
        ),
    ] = None
    name: Annotated[str, Field(description="Name is the name of resource being referenced.")]
    resource: Annotated[
        str,
        Field(description='Resource is the type of resource being referenced, for example "pods".'),
    ]
    uid: Annotated[
        str,
        Field(description="UID identifies exactly one incarnation of the resource."),
    ]


class ResourceClaimParametersReference(BaseModel):
    api_group: Annotated[
        Optional[str],
        Field(
            alias="apiGroup",
            description="APIGroup is the group for the resource being referenced. It is empty for the core API. This matches the group in the APIVersion that is used when creating the resources.",
        ),
    ] = None
    kind: Annotated[
        str,
        Field(
            description='Kind is the type of resource being referenced. This is the same value as in the parameter object\'s metadata, for example "ConfigMap".'
        ),
    ]
    name: Annotated[str, Field(description="Name is the name of resource being referenced.")]


class ResourceClaimSchedulingStatus(BaseModel):
    name: Annotated[
        Optional[str],
        Field(description="Name matches the pod.spec.resourceClaims[*].Name field."),
    ] = None
    unsuitable_nodes: Annotated[
        Optional[List[str]],
        Field(
            alias="unsuitableNodes",
            description="UnsuitableNodes lists nodes that the ResourceClaim cannot be allocated for.\n\nThe size of this field is limited to 128, the same as for PodSchedulingSpec.PotentialNodes. This may get increased in the future, but not reduced.",
        ),
    ] = None


class ResourceClaimSpec(BaseModel):
    allocation_mode: Annotated[
        Optional[str],
        Field(
            alias="allocationMode",
            description='Allocation can start immediately or when a Pod wants to use the resource. "WaitForFirstConsumer" is the default.',
        ),
    ] = None
    parameters_ref: Annotated[
        Optional[ResourceClaimParametersReference],
        Field(
            alias="parametersRef",
            description="ParametersRef references a separate object with arbitrary parameters that will be used by the driver when allocating a resource for the claim.\n\nThe object must be in the same namespace as the ResourceClaim.",
        ),
    ] = None
    resource_class_name: Annotated[
        str,
        Field(
            alias="resourceClassName",
            description="ResourceClassName references the driver and additional parameters via the name of a ResourceClass that was created as part of the driver deployment.",
        ),
    ]


class ResourceClassParametersReference(BaseModel):
    api_group: Annotated[
        Optional[str],
        Field(
            alias="apiGroup",
            description="APIGroup is the group for the resource being referenced. It is empty for the core API. This matches the group in the APIVersion that is used when creating the resources.",
        ),
    ] = None
    kind: Annotated[
        str,
        Field(
            description="Kind is the type of resource being referenced. This is the same value as in the parameter object's metadata."
        ),
    ]
    name: Annotated[str, Field(description="Name is the name of resource being referenced.")]
    namespace: Annotated[
        Optional[str],
        Field(
            description="Namespace that contains the referenced resource. Must be empty for cluster-scoped resources and non-empty for namespaced resources."
        ),
    ] = None


class ResourceFilter(BaseModel):
    driver_name: Annotated[
        Optional[str],
        Field(
            alias="driverName",
            description="DriverName is the name used by the DRA driver kubelet plugin.",
        ),
    ] = None
    named_resources: Annotated[
        Optional[NamedResourcesFilter],
        Field(
            alias="namedResources",
            description="NamedResources describes a resource filter using the named resources model.",
        ),
    ] = None


class DriverAllocationResult(BaseModel):
    named_resources: Annotated[
        Optional[NamedResourcesAllocationResult],
        Field(
            alias="namedResources",
            description="NamedResources describes the allocation result when using the named resources model.",
        ),
    ] = None
    vendor_request_parameters: Annotated[
        Optional[apimachinery.RawExtension],
        Field(
            alias="vendorRequestParameters",
            description="VendorRequestParameters are the per-request configuration parameters from the time that the claim was allocated.",
        ),
    ] = None


class NamedResourcesAttribute(BaseModel):
    bool: Annotated[Optional[bool], Field(description="BoolValue is a true/false value.")] = None
    int: Annotated[Optional[int], Field(description="IntValue is a 64-bit integer.")] = None
    int_slice: Annotated[
        Optional[NamedResourcesIntSlice],
        Field(
            alias="intSlice",
            description="IntSliceValue is an array of 64-bit integers.",
        ),
    ] = None
    name: Annotated[
        str,
        Field(
            description="Name is unique identifier among all resource instances managed by the driver on the node. It must be a DNS subdomain."
        ),
    ]
    quantity: Annotated[
        Optional[apimachinery.Quantity],
        Field(description="QuantityValue is a quantity."),
    ] = None
    string: Annotated[Optional[str], Field(description="StringValue is a string.")] = None
    string_slice: Annotated[
        Optional[NamedResourcesStringSlice],
        Field(alias="stringSlice", description="StringSliceValue is an array of strings."),
    ] = None
    version: Annotated[
        Optional[str],
        Field(description="VersionValue is a semantic version according to semver.org spec 2.0.0."),
    ] = None


class NamedResourcesInstance(BaseModel):
    attributes: Annotated[
        Optional[List[NamedResourcesAttribute]],
        Field(
            description="Attributes defines the attributes of this resource instance. The name of each attribute must be unique."
        ),
    ] = None
    name: Annotated[
        str,
        Field(
            description="Name is unique identifier among all resource instances managed by the driver on the node. It must be a DNS subdomain."
        ),
    ]


class NamedResourcesResources(BaseModel):
    instances: Annotated[
        List[NamedResourcesInstance],
        Field(description="The list of all individual resources instances currently available."),
    ]


class PodSchedulingContextStatus(BaseModel):
    resource_claims: Annotated[
        Optional[List[ResourceClaimSchedulingStatus]],
        Field(
            alias="resourceClaims",
            description='ResourceClaims describes resource availability for each pod.spec.resourceClaim entry where the corresponding ResourceClaim uses "WaitForFirstConsumer" allocation mode.',
        ),
    ] = None


class ResourceRequest(BaseModel):
    named_resources: Annotated[
        Optional[NamedResourcesRequest],
        Field(
            alias="namedResources",
            description="NamedResources describes a request for resources with the named resources model.",
        ),
    ] = None
    vendor_parameters: Annotated[
        Optional[apimachinery.RawExtension],
        Field(
            alias="vendorParameters",
            description="VendorParameters are arbitrary setup parameters for the requested resource. They are ignored while allocating a claim.",
        ),
    ] = None


class StructuredResourceHandle(BaseModel):
    node_name: Annotated[
        Optional[str],
        Field(
            alias="nodeName",
            description="NodeName is the name of the node providing the necessary resources if the resources are local to a node.",
        ),
    ] = None
    results: Annotated[
        List[DriverAllocationResult],
        Field(description="Results lists all allocated driver resources."),
    ]
    vendor_claim_parameters: Annotated[
        Optional[apimachinery.RawExtension],
        Field(
            alias="vendorClaimParameters",
            description="VendorClaimParameters are the per-claim configuration parameters from the resource claim parameters at the time that the claim was allocated.",
        ),
    ] = None
    vendor_class_parameters: Annotated[
        Optional[apimachinery.RawExtension],
        Field(
            alias="vendorClassParameters",
            description="VendorClassParameters are the per-claim configuration parameters from the resource class at the time that the claim was allocated.",
        ),
    ] = None


class VendorParameters(BaseModel):
    driver_name: Annotated[
        Optional[str],
        Field(
            alias="driverName",
            description="DriverName is the name used by the DRA driver kubelet plugin.",
        ),
    ] = None
    parameters: Annotated[
        Optional[apimachinery.RawExtension],
        Field(
            description="Parameters can be arbitrary setup parameters. They are ignored while allocating a claim."
        ),
    ] = None


class DriverRequests(BaseModel):
    driver_name: Annotated[
        Optional[str],
        Field(
            alias="driverName",
            description="DriverName is the name used by the DRA driver kubelet plugin.",
        ),
    ] = None
    requests: Annotated[
        Optional[List[ResourceRequest]],
        Field(description="Requests describes all resources that are needed from the driver."),
    ] = None
    vendor_parameters: Annotated[
        Optional[apimachinery.RawExtension],
        Field(
            alias="vendorParameters",
            description="VendorParameters are arbitrary setup parameters for all requests of the claim. They are ignored while allocating the claim.",
        ),
    ] = None


class PodSchedulingContext(Resource):
    api_version: Annotated[
        Optional[Literal["resource.k8s.io/v1alpha2"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "resource.k8s.io/v1alpha2"
    kind: Annotated[
        Optional[Literal["PodSchedulingContext"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "PodSchedulingContext"
    metadata: Annotated[
        Optional[apimachinery.ObjectMeta], Field(description="Standard object metadata")
    ] = None
    spec: Annotated[
        PodSchedulingContextSpec,
        Field(description="Spec describes where resources for the Pod are needed."),
    ]
    status: Annotated[
        Optional[PodSchedulingContextStatus],
        Field(description="Status describes where resources for the Pod can be allocated."),
    ] = None


PodSchedulingContextList = ResourceList["PodSchedulingContext"]


class ResourceClaimParameters(Resource):
    api_version: Annotated[
        Optional[Literal["resource.k8s.io/v1alpha2"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "resource.k8s.io/v1alpha2"
    driver_requests: Annotated[
        Optional[List[DriverRequests]],
        Field(
            alias="driverRequests",
            description="DriverRequests describes all resources that are needed for the allocated claim. A single claim may use resources coming from different drivers. For each driver, this array has at most one entry which then may have one or more per-driver requests.\n\nMay be empty, in which case the claim can always be allocated.",
        ),
    ] = None
    generated_from: Annotated[
        Optional[ResourceClaimParametersReference],
        Field(
            alias="generatedFrom",
            description="If this object was created from some other resource, then this links back to that resource. This field is used to find the in-tree representation of the claim parameters when the parameter reference of the claim refers to some unknown type.",
        ),
    ] = None
    kind: Annotated[
        Optional[Literal["ResourceClaimParameters"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "ResourceClaimParameters"
    metadata: Annotated[
        Optional[apimachinery.ObjectMeta], Field(description="Standard object metadata")
    ] = None
    shareable: Annotated[
        Optional[bool],
        Field(
            description="Shareable indicates whether the allocated claim is meant to be shareable by multiple consumers at the same time."
        ),
    ] = None


ResourceClaimParametersList = ResourceList["ResourceClaimParameters"]


class ResourceClaimTemplateSpec(BaseModel):
    metadata: Annotated[
        Optional[apimachinery.ObjectMeta],
        Field(
            description="ObjectMeta may contain labels and annotations that will be copied into the PVC when creating it. No other fields are allowed and will be rejected during validation."
        ),
    ] = None
    spec: Annotated[
        ResourceClaimSpec,
        Field(
            description="Spec for the ResourceClaim. The entire content is copied unchanged into the ResourceClaim that gets created from this template. The same fields as in a ResourceClaim are also valid here."
        ),
    ]


class ResourceClass(Resource):
    api_version: Annotated[
        Optional[Literal["resource.k8s.io/v1alpha2"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "resource.k8s.io/v1alpha2"
    driver_name: Annotated[
        str,
        Field(
            alias="driverName",
            description="DriverName defines the name of the dynamic resource driver that is used for allocation of a ResourceClaim that uses this class.\n\nResource drivers have a unique name in forward domain order (acme.example.com).",
        ),
    ]
    kind: Annotated[
        Optional[Literal["ResourceClass"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "ResourceClass"
    metadata: Annotated[
        Optional[apimachinery.ObjectMeta], Field(description="Standard object metadata")
    ] = None
    parameters_ref: Annotated[
        Optional[ResourceClassParametersReference],
        Field(
            alias="parametersRef",
            description="ParametersRef references an arbitrary separate object that may hold parameters that will be used by the driver when allocating a resource that uses this class. A dynamic resource driver can distinguish between parameters stored here and and those stored in ResourceClaimSpec.",
        ),
    ] = None
    structured_parameters: Annotated[
        Optional[bool],
        Field(
            alias="structuredParameters",
            description="If and only if allocation of claims using this class is handled via structured parameters, then StructuredParameters must be set to true.",
        ),
    ] = None
    suitable_nodes: Annotated[
        Optional[v1.NodeSelector],
        Field(
            alias="suitableNodes",
            description="Only nodes matching the selector will be considered by the scheduler when trying to find a Node that fits a Pod when that Pod uses a ResourceClaim that has not been allocated yet.\n\nSetting this field is optional. If null, all nodes are candidates.",
        ),
    ] = None


ResourceClassList = ResourceList["ResourceClass"]


class ResourceClassParameters(Resource):
    api_version: Annotated[
        Optional[Literal["resource.k8s.io/v1alpha2"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "resource.k8s.io/v1alpha2"
    filters: Annotated[
        Optional[List[ResourceFilter]],
        Field(
            description="Filters describes additional contraints that must be met when using the class."
        ),
    ] = None
    generated_from: Annotated[
        Optional[ResourceClassParametersReference],
        Field(
            alias="generatedFrom",
            description="If this object was created from some other resource, then this links back to that resource. This field is used to find the in-tree representation of the class parameters when the parameter reference of the class refers to some unknown type.",
        ),
    ] = None
    kind: Annotated[
        Optional[Literal["ResourceClassParameters"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "ResourceClassParameters"
    metadata: Annotated[
        Optional[apimachinery.ObjectMeta], Field(description="Standard object metadata")
    ] = None
    vendor_parameters: Annotated[
        Optional[List[VendorParameters]],
        Field(
            alias="vendorParameters",
            description="VendorParameters are arbitrary setup parameters for all claims using this class. They are ignored while allocating the claim. There must not be more than one entry per driver.",
        ),
    ] = None


ResourceClassParametersList = ResourceList["ResourceClassParameters"]


class ResourceHandle(BaseModel):
    data: Annotated[
        Optional[str],
        Field(
            description="Data contains the opaque data associated with this ResourceHandle. It is set by the controller component of the resource driver whose name matches the DriverName set in the ResourceClaimStatus this ResourceHandle is embedded in. It is set at allocation time and is intended for processing by the kubelet plugin whose name matches the DriverName set in this ResourceHandle.\n\nThe maximum size of this field is 16KiB. This may get increased in the future, but not reduced."
        ),
    ] = None
    driver_name: Annotated[
        Optional[str],
        Field(
            alias="driverName",
            description="DriverName specifies the name of the resource driver whose kubelet plugin should be invoked to process this ResourceHandle's data once it lands on a node. This may differ from the DriverName set in ResourceClaimStatus this ResourceHandle is embedded in.",
        ),
    ] = None
    structured_data: Annotated[
        Optional[StructuredResourceHandle],
        Field(
            alias="structuredData",
            description="If StructuredData is set, then it needs to be used instead of Data.",
        ),
    ] = None


class ResourceSlice(Resource):
    api_version: Annotated[
        Optional[Literal["resource.k8s.io/v1alpha2"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "resource.k8s.io/v1alpha2"
    driver_name: Annotated[
        str,
        Field(
            alias="driverName",
            description="DriverName identifies the DRA driver providing the capacity information. A field selector can be used to list only ResourceSlice objects with a certain driver name.",
        ),
    ]
    kind: Annotated[
        Optional[Literal["ResourceSlice"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "ResourceSlice"
    metadata: Annotated[
        Optional[apimachinery.ObjectMeta], Field(description="Standard object metadata")
    ] = None
    named_resources: Annotated[
        Optional[NamedResourcesResources],
        Field(
            alias="namedResources",
            description="NamedResources describes available resources using the named resources model.",
        ),
    ] = None
    node_name: Annotated[
        Optional[str],
        Field(
            alias="nodeName",
            description="NodeName identifies the node which provides the resources if they are local to a node.\n\nA field selector can be used to list only ResourceSlice objects with a certain node name.",
        ),
    ] = None


ResourceSliceList = ResourceList["ResourceSlice"]


class AllocationResult(BaseModel):
    available_on_nodes: Annotated[
        Optional[v1.NodeSelector],
        Field(
            alias="availableOnNodes",
            description="This field will get set by the resource driver after it has allocated the resource to inform the scheduler where it can schedule Pods using the ResourceClaim.\n\nSetting this field is optional. If null, the resource is available everywhere.",
        ),
    ] = None
    resource_handles: Annotated[
        Optional[List[ResourceHandle]],
        Field(
            alias="resourceHandles",
            description="ResourceHandles contain the state associated with an allocation that should be maintained throughout the lifetime of a claim. Each ResourceHandle contains data that should be passed to a specific kubelet plugin once it lands on a node. This data is returned by the driver after a successful allocation and is opaque to Kubernetes. Driver documentation may explain to users how to interpret this data if needed.\n\nSetting this field is optional. It has a maximum size of 32 entries. If null (or empty), it is assumed this allocation will be processed by a single kubelet plugin with no ResourceHandle data attached. The name of the kubelet plugin invoked will match the DriverName set in the ResourceClaimStatus this AllocationResult is embedded in.",
        ),
    ] = None
    shareable: Annotated[
        Optional[bool],
        Field(
            description="Shareable determines whether the resource supports more than one consumer at a time."
        ),
    ] = None


class ResourceClaimStatus(BaseModel):
    allocation: Annotated[
        Optional[AllocationResult],
        Field(
            description="Allocation is set by the resource driver once a resource or set of resources has been allocated successfully. If this is not specified, the resources have not been allocated yet."
        ),
    ] = None
    deallocation_requested: Annotated[
        Optional[bool],
        Field(
            alias="deallocationRequested",
            description="DeallocationRequested indicates that a ResourceClaim is to be deallocated.\n\nThe driver then must deallocate this claim and reset the field together with clearing the Allocation field.\n\nWhile DeallocationRequested is set, no new consumers may be added to ReservedFor.",
        ),
    ] = None
    driver_name: Annotated[
        Optional[str],
        Field(
            alias="driverName",
            description="DriverName is a copy of the driver name from the ResourceClass at the time when allocation started.",
        ),
    ] = None
    reserved_for: Annotated[
        Optional[List[ResourceClaimConsumerReference]],
        Field(
            alias="reservedFor",
            description="ReservedFor indicates which entities are currently allowed to use the claim. A Pod which references a ResourceClaim which is not reserved for that Pod will not be started.\n\nThere can be at most 32 such reservations. This may get increased in the future, but not reduced.",
        ),
    ] = None


class ResourceClaimTemplate(Resource):
    api_version: Annotated[
        Optional[Literal["resource.k8s.io/v1alpha2"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "resource.k8s.io/v1alpha2"
    kind: Annotated[
        Optional[Literal["ResourceClaimTemplate"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "ResourceClaimTemplate"
    metadata: Annotated[
        Optional[apimachinery.ObjectMeta], Field(description="Standard object metadata")
    ] = None
    spec: Annotated[
        ResourceClaimTemplateSpec,
        Field(
            description="Describes the ResourceClaim that is to be generated.\n\nThis field is immutable. A ResourceClaim will get created by the control plane for a Pod when needed and then not get updated anymore."
        ),
    ]


ResourceClaimTemplateList = ResourceList["ResourceClaimTemplate"]


class ResourceClaim(Resource):
    api_version: Annotated[
        Optional[Literal["resource.k8s.io/v1alpha2"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "resource.k8s.io/v1alpha2"
    kind: Annotated[
        Optional[Literal["ResourceClaim"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "ResourceClaim"
    metadata: Annotated[
        Optional[apimachinery.ObjectMeta], Field(description="Standard object metadata")
    ] = None
    spec: Annotated[
        ResourceClaimSpec,
        Field(
            description="Spec describes the desired attributes of a resource that then needs to be allocated. It can only be set once when creating the ResourceClaim."
        ),
    ]
    status: Annotated[
        Optional[ResourceClaimStatus],
        Field(
            description="Status describes whether the resource is available and with which attributes."
        ),
    ] = None


ResourceClaimList = ResourceList["ResourceClaim"]
