# Generated by cloudcoil-model-codegen v0.1.1
# DO NOT EDIT

from __future__ import annotations

from typing import Annotated, Callable, List, Literal, Optional, Type, Union

from pydantic import Field

from cloudcoil import apimachinery
from cloudcoil.pydantic import BaseBuilder, BaseModel, ListBuilder, Self
from cloudcoil.resources import Resource, ResourceList


class ParentReference(BaseModel):
    class Builder(BaseBuilder):
        def build(self) -> "ParentReference":
            return ParentReference(**self._attrs)

        def group(self, value: Optional[str]) -> Self:
            return self._set("group", value)

        def name(self, value: str) -> Self:
            return self._set("name", value)

        def namespace(self, value: Optional[str]) -> Self:
            return self._set("namespace", value)

        def resource(self, value: str) -> Self:
            return self._set("resource", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def list_builder(cls) -> ListBuilder[Self]:
        return ListBuilder[cls]()  # type: ignore[valid-type]

    group: Annotated[
        Optional[str],
        Field(description="Group is the group of the object being referenced."),
    ] = None
    name: Annotated[str, Field(description="Name is the name of the object being referenced.")]
    namespace: Annotated[
        Optional[str],
        Field(description="Namespace is the namespace of the object being referenced."),
    ] = None
    resource: Annotated[
        str,
        Field(description="Resource is the resource of the object being referenced."),
    ]


class ServiceCIDRSpec(BaseModel):
    class Builder(BaseBuilder):
        def build(self) -> "ServiceCIDRSpec":
            return ServiceCIDRSpec(**self._attrs)

        def cidrs(self, value: Optional[List[str]]) -> Self:
            return self._set("cidrs", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def list_builder(cls) -> ListBuilder[Self]:
        return ListBuilder[cls]()  # type: ignore[valid-type]

    cidrs: Annotated[
        Optional[List[str]],
        Field(
            description='CIDRs defines the IP blocks in CIDR notation (e.g. "192.168.0.0/24" or "2001:db8::/64") from which to assign service cluster IPs. Max of two CIDRs is allowed, one of each IP family. This field is immutable.'
        ),
    ] = None


class IPAddressSpec(BaseModel):
    class Builder(BaseBuilder):
        def build(self) -> "IPAddressSpec":
            return IPAddressSpec(**self._attrs)

        def parent_ref(
            self,
            value_or_callback: Union[
                ParentReference, Callable[[Type[ParentReference]], ParentReference]
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(ParentReference)
            return self._set("parent_ref", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def list_builder(cls) -> ListBuilder[Self]:
        return ListBuilder[cls]()  # type: ignore[valid-type]

    parent_ref: Annotated[
        ParentReference,
        Field(
            alias="parentRef",
            description="ParentRef references the resource that an IPAddress is attached to. An IPAddress must reference a parent object.",
        ),
    ]


class IPAddress(Resource):
    class Builder(BaseBuilder):
        def build(self) -> "IPAddress":
            return IPAddress(**self._attrs)

        def api_version(self, value: Optional[Literal["networking.k8s.io/v1alpha1"]]) -> Self:
            return self._set("api_version", value)

        def kind(self, value: Optional[Literal["IPAddress"]]) -> Self:
            return self._set("kind", value)

        def metadata(
            self,
            value_or_callback: Union[
                Optional[apimachinery.ObjectMeta],
                Callable[[Type[apimachinery.ObjectMeta]], apimachinery.ObjectMeta],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(apimachinery.ObjectMeta)
            return self._set("metadata", value)

        def spec(
            self,
            value_or_callback: Union[
                Optional[IPAddressSpec], Callable[[Type[IPAddressSpec]], IPAddressSpec]
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(IPAddressSpec)
            return self._set("spec", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def list_builder(cls) -> ListBuilder[Self]:
        return ListBuilder[cls]()  # type: ignore[valid-type]

    api_version: Annotated[
        Optional[Literal["networking.k8s.io/v1alpha1"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "networking.k8s.io/v1alpha1"
    kind: Annotated[
        Optional[Literal["IPAddress"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "IPAddress"
    metadata: Annotated[
        Optional[apimachinery.ObjectMeta],
        Field(
            description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    ] = None
    spec: Annotated[
        Optional[IPAddressSpec],
        Field(
            description="spec is the desired state of the IPAddress. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status"
        ),
    ] = None


IPAddressList = ResourceList["IPAddress"]


class ServiceCIDRStatus(BaseModel):
    class Builder(BaseBuilder):
        def build(self) -> "ServiceCIDRStatus":
            return ServiceCIDRStatus(**self._attrs)

        def conditions(
            self,
            value_or_callback: Union[
                Optional[List[apimachinery.Condition]],
                Callable[[Type[apimachinery.Condition]], List[apimachinery.Condition]],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(apimachinery.Condition)
            return self._set("conditions", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def list_builder(cls) -> ListBuilder[Self]:
        return ListBuilder[cls]()  # type: ignore[valid-type]

    conditions: Annotated[
        Optional[List[apimachinery.Condition]],
        Field(
            description="conditions holds an array of metav1.Condition that describe the state of the ServiceCIDR. Current service state"
        ),
    ] = None


class ServiceCIDR(Resource):
    class Builder(BaseBuilder):
        def build(self) -> "ServiceCIDR":
            return ServiceCIDR(**self._attrs)

        def api_version(self, value: Optional[Literal["networking.k8s.io/v1alpha1"]]) -> Self:
            return self._set("api_version", value)

        def kind(self, value: Optional[Literal["ServiceCIDR"]]) -> Self:
            return self._set("kind", value)

        def metadata(
            self,
            value_or_callback: Union[
                Optional[apimachinery.ObjectMeta],
                Callable[[Type[apimachinery.ObjectMeta]], apimachinery.ObjectMeta],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(apimachinery.ObjectMeta)
            return self._set("metadata", value)

        def spec(
            self,
            value_or_callback: Union[
                Optional[ServiceCIDRSpec],
                Callable[[Type[ServiceCIDRSpec]], ServiceCIDRSpec],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(ServiceCIDRSpec)
            return self._set("spec", value)

        def status(
            self,
            value_or_callback: Union[
                Optional[ServiceCIDRStatus],
                Callable[[Type[ServiceCIDRStatus]], ServiceCIDRStatus],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(ServiceCIDRStatus)
            return self._set("status", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def list_builder(cls) -> ListBuilder[Self]:
        return ListBuilder[cls]()  # type: ignore[valid-type]

    api_version: Annotated[
        Optional[Literal["networking.k8s.io/v1alpha1"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "networking.k8s.io/v1alpha1"
    kind: Annotated[
        Optional[Literal["ServiceCIDR"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "ServiceCIDR"
    metadata: Annotated[
        Optional[apimachinery.ObjectMeta],
        Field(
            description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    ] = None
    spec: Annotated[
        Optional[ServiceCIDRSpec],
        Field(
            description="spec is the desired state of the ServiceCIDR. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status"
        ),
    ] = None
    status: Annotated[
        Optional[ServiceCIDRStatus],
        Field(
            description="status represents the current state of the ServiceCIDR. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status"
        ),
    ] = None


ServiceCIDRList = ResourceList["ServiceCIDR"]
