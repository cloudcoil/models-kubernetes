# Generated by cloudcoil-model-codegen v0.1.1
# DO NOT EDIT

from __future__ import annotations

from typing import Annotated, Callable, Dict, List, Literal, Optional, Type, Union

from pydantic import Field

from cloudcoil import apimachinery
from cloudcoil.pydantic import BaseBuilder, BaseModel, ListBuilder, Self
from cloudcoil.resources import Resource, ResourceList

from ..core import v1


class EndpointConditions(BaseModel):
    class Builder(BaseBuilder):
        def build(self) -> "EndpointConditions":
            return EndpointConditions(**self._attrs)

        def ready(self, value: Optional[bool]) -> Self:
            return self._set("ready", value)

        def serving(self, value: Optional[bool]) -> Self:
            return self._set("serving", value)

        def terminating(self, value: Optional[bool]) -> Self:
            return self._set("terminating", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def list_builder(cls) -> ListBuilder[Self]:
        return ListBuilder[cls]()  # type: ignore[valid-type]

    ready: Annotated[
        Optional[bool],
        Field(
            description='ready indicates that this endpoint is prepared to receive traffic, according to whatever system is managing the endpoint. A nil value indicates an unknown state. In most cases consumers should interpret this unknown state as ready. For compatibility reasons, ready should never be "true" for terminating endpoints, except when the normal readiness behavior is being explicitly overridden, for example when the associated Service has set the publishNotReadyAddresses flag.'
        ),
    ] = None
    serving: Annotated[
        Optional[bool],
        Field(
            description="serving is identical to ready except that it is set regardless of the terminating state of endpoints. This condition should be set to true for a ready endpoint that is terminating. If nil, consumers should defer to the ready condition."
        ),
    ] = None
    terminating: Annotated[
        Optional[bool],
        Field(
            description="terminating indicates that this endpoint is terminating. A nil value indicates an unknown state. Consumers should interpret this unknown state to mean that the endpoint is not terminating."
        ),
    ] = None


class EndpointPort(BaseModel):
    class Builder(BaseBuilder):
        def build(self) -> "EndpointPort":
            return EndpointPort(**self._attrs)

        def app_protocol(self, value: Optional[str]) -> Self:
            return self._set("app_protocol", value)

        def name(self, value: Optional[str]) -> Self:
            return self._set("name", value)

        def port(self, value: Optional[int]) -> Self:
            return self._set("port", value)

        def protocol(self, value: Optional[str]) -> Self:
            return self._set("protocol", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def list_builder(cls) -> ListBuilder[Self]:
        return ListBuilder[cls]()  # type: ignore[valid-type]

    app_protocol: Annotated[
        Optional[str],
        Field(
            alias="appProtocol",
            description="The application protocol for this port. This is used as a hint for implementations to offer richer behavior for protocols that they understand. This field follows standard Kubernetes label syntax. Valid values are either:\n\n* Un-prefixed protocol names - reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names).\n\n* Kubernetes-defined prefixed names:\n  * 'kubernetes.io/h2c' - HTTP/2 prior knowledge over cleartext as described in https://www.rfc-editor.org/rfc/rfc9113.html#name-starting-http-2-with-prior-\n  * 'kubernetes.io/ws'  - WebSocket over cleartext as described in https://www.rfc-editor.org/rfc/rfc6455\n  * 'kubernetes.io/wss' - WebSocket over TLS as described in https://www.rfc-editor.org/rfc/rfc6455\n\n* Other protocols should use implementation-defined prefixed names such as mycompany.com/my-custom-protocol.",
        ),
    ] = None
    name: Annotated[
        Optional[str],
        Field(
            description="name represents the name of this port. All ports in an EndpointSlice must have a unique name. If the EndpointSlice is derived from a Kubernetes service, this corresponds to the Service.ports[].name. Name must either be an empty string or pass DNS_LABEL validation: * must be no more than 63 characters long. * must consist of lower case alphanumeric characters or '-'. * must start and end with an alphanumeric character. Default is empty string."
        ),
    ] = None
    port: Annotated[
        Optional[int],
        Field(
            description="port represents the port number of the endpoint. If this is not specified, ports are not restricted and must be interpreted in the context of the specific consumer."
        ),
    ] = None
    protocol: Annotated[
        Optional[str],
        Field(
            description="protocol represents the IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP."
        ),
    ] = None


class ForZone(BaseModel):
    class Builder(BaseBuilder):
        def build(self) -> "ForZone":
            return ForZone(**self._attrs)

        def name(self, value: str) -> Self:
            return self._set("name", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def list_builder(cls) -> ListBuilder[Self]:
        return ListBuilder[cls]()  # type: ignore[valid-type]

    name: Annotated[str, Field(description="name represents the name of the zone.")]


class EndpointHints(BaseModel):
    class Builder(BaseBuilder):
        def build(self) -> "EndpointHints":
            return EndpointHints(**self._attrs)

        def for_zones(
            self,
            value_or_callback: Union[
                Optional[List[ForZone]], Callable[[Type[ForZone]], List[ForZone]]
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(ForZone)
            return self._set("for_zones", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def list_builder(cls) -> ListBuilder[Self]:
        return ListBuilder[cls]()  # type: ignore[valid-type]

    for_zones: Annotated[
        Optional[List[ForZone]],
        Field(
            alias="forZones",
            description="forZones indicates the zone(s) this endpoint should be consumed by to enable topology aware routing.",
        ),
    ] = None


class Endpoint(BaseModel):
    class Builder(BaseBuilder):
        def build(self) -> "Endpoint":
            return Endpoint(**self._attrs)

        def addresses(self, value: List[str]) -> Self:
            return self._set("addresses", value)

        def conditions(
            self,
            value_or_callback: Union[
                Optional[EndpointConditions],
                Callable[[Type[EndpointConditions]], EndpointConditions],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(EndpointConditions)
            return self._set("conditions", value)

        def deprecated_topology(self, value: Optional[Dict[str, str]]) -> Self:
            return self._set("deprecated_topology", value)

        def hints(
            self,
            value_or_callback: Union[
                Optional[EndpointHints], Callable[[Type[EndpointHints]], EndpointHints]
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(EndpointHints)
            return self._set("hints", value)

        def hostname(self, value: Optional[str]) -> Self:
            return self._set("hostname", value)

        def node_name(self, value: Optional[str]) -> Self:
            return self._set("node_name", value)

        def target_ref(
            self,
            value_or_callback: Union[
                Optional[v1.ObjectReference],
                Callable[[Type[v1.ObjectReference]], v1.ObjectReference],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(v1.ObjectReference)
            return self._set("target_ref", value)

        def zone(self, value: Optional[str]) -> Self:
            return self._set("zone", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def list_builder(cls) -> ListBuilder[Self]:
        return ListBuilder[cls]()  # type: ignore[valid-type]

    addresses: Annotated[
        List[str],
        Field(
            description="addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. Consumers must handle different types of addresses in the context of their own capabilities. This must contain at least one address but no more than 100. These are all assumed to be fungible and clients may choose to only use the first element. Refer to: https://issue.k8s.io/106267"
        ),
    ]
    conditions: Annotated[
        Optional[EndpointConditions],
        Field(
            description="conditions contains information about the current status of the endpoint."
        ),
    ] = None
    deprecated_topology: Annotated[
        Optional[Dict[str, str]],
        Field(
            alias="deprecatedTopology",
            description="deprecatedTopology contains topology information part of the v1beta1 API. This field is deprecated, and will be removed when the v1beta1 API is removed (no sooner than kubernetes v1.24).  While this field can hold values, it is not writable through the v1 API, and any attempts to write to it will be silently ignored. Topology information can be found in the zone and nodeName fields instead.",
        ),
    ] = None
    hints: Annotated[
        Optional[EndpointHints],
        Field(
            description="hints contains information associated with how an endpoint should be consumed."
        ),
    ] = None
    hostname: Annotated[
        Optional[str],
        Field(
            description="hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname should be considered fungible (e.g. multiple A values in DNS). Must be lowercase and pass DNS Label (RFC 1123) validation."
        ),
    ] = None
    node_name: Annotated[
        Optional[str],
        Field(
            alias="nodeName",
            description="nodeName represents the name of the Node hosting this endpoint. This can be used to determine endpoints local to a Node.",
        ),
    ] = None
    target_ref: Annotated[
        Optional[v1.ObjectReference],
        Field(
            alias="targetRef",
            description="targetRef is a reference to a Kubernetes object that represents this endpoint.",
        ),
    ] = None
    zone: Annotated[
        Optional[str],
        Field(description="zone is the name of the Zone this endpoint exists in."),
    ] = None


class EndpointSlice(Resource):
    class Builder(BaseBuilder):
        def build(self) -> "EndpointSlice":
            return EndpointSlice(**self._attrs)

        def address_type(self, value: str) -> Self:
            return self._set("address_type", value)

        def api_version(self, value: Optional[Literal["discovery.k8s.io/v1"]]) -> Self:
            return self._set("api_version", value)

        def endpoints(
            self,
            value_or_callback: Union[List[Endpoint], Callable[[Type[Endpoint]], List[Endpoint]]],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(Endpoint)
            return self._set("endpoints", value)

        def kind(self, value: Optional[Literal["EndpointSlice"]]) -> Self:
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

        def ports(
            self,
            value_or_callback: Union[
                Optional[List[EndpointPort]],
                Callable[[Type[EndpointPort]], List[EndpointPort]],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(EndpointPort)
            return self._set("ports", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def list_builder(cls) -> ListBuilder[Self]:
        return ListBuilder[cls]()  # type: ignore[valid-type]

    address_type: Annotated[
        str,
        Field(
            alias="addressType",
            description="addressType specifies the type of address carried by this EndpointSlice. All addresses in this slice must be the same type. This field is immutable after creation. The following address types are currently supported: * IPv4: Represents an IPv4 Address. * IPv6: Represents an IPv6 Address. * FQDN: Represents a Fully Qualified Domain Name.",
        ),
    ]
    api_version: Annotated[
        Optional[Literal["discovery.k8s.io/v1"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "discovery.k8s.io/v1"
    endpoints: Annotated[
        List[Endpoint],
        Field(
            description="endpoints is a list of unique endpoints in this slice. Each slice may include a maximum of 1000 endpoints."
        ),
    ]
    kind: Annotated[
        Optional[Literal["EndpointSlice"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "EndpointSlice"
    metadata: Annotated[
        Optional[apimachinery.ObjectMeta],
        Field(description="Standard object's metadata."),
    ] = None
    ports: Annotated[
        Optional[List[EndpointPort]],
        Field(
            description='ports specifies the list of network ports exposed by each endpoint in this slice. Each port must have a unique name. When ports is empty, it indicates that there are no defined ports. When a port is defined with a nil port value, it indicates "all ports". Each slice may include a maximum of 100 ports.'
        ),
    ] = None


EndpointSliceList = ResourceList["EndpointSlice"]
