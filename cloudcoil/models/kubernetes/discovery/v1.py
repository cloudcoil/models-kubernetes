# Generated by cloudcoil-model-codegen v0.4.2
# DO NOT EDIT

from __future__ import annotations

from typing import (
    Annotated,
    Callable,
    Dict,
    List,
    Literal,
    Optional,
    Type,
    overload,
)

from pydantic import Field

from cloudcoil import apimachinery
from cloudcoil.pydantic import (
    BaseModel,
    BaseModelBuilder,
    BuilderContextBase,
    GenericListBuilder,
    ListBuilderContext,
    Never,
    Self,
)
from cloudcoil.resources import Resource, ResourceList

from ..core import v1


class EndpointConditions(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["EndpointConditions"]:
            return EndpointConditions

        def build(self) -> "EndpointConditions":
            return EndpointConditions(**self._attrs)

        def ready(self, value: Optional[bool], /) -> Self:
            """
            ready indicates that this endpoint is prepared to receive traffic, according to whatever system is managing the endpoint. A nil value indicates an unknown state. In most cases consumers should interpret this unknown state as ready. For compatibility reasons, ready should never be "true" for terminating endpoints, except when the normal readiness behavior is being explicitly overridden, for example when the associated Service has set the publishNotReadyAddresses flag.
            """
            return self._set("ready", value)

        def serving(self, value: Optional[bool], /) -> Self:
            """
            serving is identical to ready except that it is set regardless of the terminating state of endpoints. This condition should be set to true for a ready endpoint that is terminating. If nil, consumers should defer to the ready condition.
            """
            return self._set("serving", value)

        def terminating(self, value: Optional[bool], /) -> Self:
            """
            terminating indicates that this endpoint is terminating. A nil value indicates an unknown state. Consumers should interpret this unknown state to mean that the endpoint is not terminating.
            """
            return self._set("terminating", value)

    class BuilderContext(BuilderContextBase["EndpointConditions.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = EndpointConditions.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for EndpointConditions."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["EndpointConditions", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use EndpointConditions.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    ready: Optional[bool] = None
    """
    ready indicates that this endpoint is prepared to receive traffic, according to whatever system is managing the endpoint. A nil value indicates an unknown state. In most cases consumers should interpret this unknown state as ready. For compatibility reasons, ready should never be "true" for terminating endpoints, except when the normal readiness behavior is being explicitly overridden, for example when the associated Service has set the publishNotReadyAddresses flag.
    """
    serving: Optional[bool] = None
    """
    serving is identical to ready except that it is set regardless of the terminating state of endpoints. This condition should be set to true for a ready endpoint that is terminating. If nil, consumers should defer to the ready condition.
    """
    terminating: Optional[bool] = None
    """
    terminating indicates that this endpoint is terminating. A nil value indicates an unknown state. Consumers should interpret this unknown state to mean that the endpoint is not terminating.
    """


class EndpointPort(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["EndpointPort"]:
            return EndpointPort

        def build(self) -> "EndpointPort":
            return EndpointPort(**self._attrs)

        def app_protocol(self, value: Optional[str], /) -> Self:
            """
            The application protocol for this port. This is used as a hint for implementations to offer richer behavior for protocols that they understand. This field follows standard Kubernetes label syntax. Valid values are either:

            * Un-prefixed protocol names - reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names).

            * Kubernetes-defined prefixed names:
              * 'kubernetes.io/h2c' - HTTP/2 prior knowledge over cleartext as described in https://www.rfc-editor.org/rfc/rfc9113.html#name-starting-http-2-with-prior-
              * 'kubernetes.io/ws'  - WebSocket over cleartext as described in https://www.rfc-editor.org/rfc/rfc6455
              * 'kubernetes.io/wss' - WebSocket over TLS as described in https://www.rfc-editor.org/rfc/rfc6455

            * Other protocols should use implementation-defined prefixed names such as mycompany.com/my-custom-protocol.
            """
            return self._set("app_protocol", value)

        def name(self, value: Optional[str], /) -> Self:
            """
            name represents the name of this port. All ports in an EndpointSlice must have a unique name. If the EndpointSlice is derived from a Kubernetes service, this corresponds to the Service.ports[].name. Name must either be an empty string or pass DNS_LABEL validation: * must be no more than 63 characters long. * must consist of lower case alphanumeric characters or '-'. * must start and end with an alphanumeric character. Default is empty string.
            """
            return self._set("name", value)

        def port(self, value: Optional[int], /) -> Self:
            """
            port represents the port number of the endpoint. If this is not specified, ports are not restricted and must be interpreted in the context of the specific consumer.
            """
            return self._set("port", value)

        def protocol(self, value: Optional[str], /) -> Self:
            """
            protocol represents the IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP.
            """
            return self._set("protocol", value)

    class BuilderContext(BuilderContextBase["EndpointPort.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = EndpointPort.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for EndpointPort."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["EndpointPort", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use EndpointPort.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    app_protocol: Annotated[Optional[str], Field(alias="appProtocol")] = None
    """
    The application protocol for this port. This is used as a hint for implementations to offer richer behavior for protocols that they understand. This field follows standard Kubernetes label syntax. Valid values are either:

    * Un-prefixed protocol names - reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names).

    * Kubernetes-defined prefixed names:
      * 'kubernetes.io/h2c' - HTTP/2 prior knowledge over cleartext as described in https://www.rfc-editor.org/rfc/rfc9113.html#name-starting-http-2-with-prior-
      * 'kubernetes.io/ws'  - WebSocket over cleartext as described in https://www.rfc-editor.org/rfc/rfc6455
      * 'kubernetes.io/wss' - WebSocket over TLS as described in https://www.rfc-editor.org/rfc/rfc6455

    * Other protocols should use implementation-defined prefixed names such as mycompany.com/my-custom-protocol.
    """
    name: Optional[str] = None
    """
    name represents the name of this port. All ports in an EndpointSlice must have a unique name. If the EndpointSlice is derived from a Kubernetes service, this corresponds to the Service.ports[].name. Name must either be an empty string or pass DNS_LABEL validation: * must be no more than 63 characters long. * must consist of lower case alphanumeric characters or '-'. * must start and end with an alphanumeric character. Default is empty string.
    """
    port: Optional[int] = None
    """
    port represents the port number of the endpoint. If this is not specified, ports are not restricted and must be interpreted in the context of the specific consumer.
    """
    protocol: Optional[str] = None
    """
    protocol represents the IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP.
    """


class ForZone(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["ForZone"]:
            return ForZone

        def build(self) -> "ForZone":
            return ForZone(**self._attrs)

        def name(self, value: str, /) -> Self:
            """
            name represents the name of the zone.
            """
            return self._set("name", value)

    class BuilderContext(BuilderContextBase["ForZone.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = ForZone.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for ForZone."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["ForZone", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use ForZone.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    name: str
    """
    name represents the name of the zone.
    """


class EndpointHints(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["EndpointHints"]:
            return EndpointHints

        def build(self) -> "EndpointHints":
            return EndpointHints(**self._attrs)

        @overload
        def for_zones(self, value_or_callback: List[ForZone], /) -> "EndpointHints.Builder": ...

        @overload
        def for_zones(
            self,
            value_or_callback: Callable[
                [GenericListBuilder[ForZone, ForZone.Builder]],
                GenericListBuilder[ForZone, ForZone.Builder] | List[ForZone],
            ],
            /,
        ) -> "EndpointHints.Builder": ...

        @overload
        def for_zones(
            self, value_or_callback: Never = ...
        ) -> ListBuilderContext[ForZone.Builder]: ...

        def for_zones(self, value_or_callback=None, /):
            """
            forZones indicates the zone(s) this endpoint should be consumed by to enable topology aware routing.
            """
            if self._in_context and value_or_callback is None:
                context = ListBuilderContext[ForZone.Builder]()
                context._parent_builder = self
                context._field_name = "for_zones"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(ForZone.list_builder())
                if isinstance(output, GenericListBuilder):
                    value = output.build()
                else:
                    value = output
            return self._set("for_zones", value)

    class BuilderContext(BuilderContextBase["EndpointHints.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = EndpointHints.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for EndpointHints."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["EndpointHints", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use EndpointHints.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    for_zones: Annotated[Optional[List[ForZone]], Field(alias="forZones")] = None
    """
    forZones indicates the zone(s) this endpoint should be consumed by to enable topology aware routing.
    """


class Endpoint(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["Endpoint"]:
            return Endpoint

        def build(self) -> "Endpoint":
            return Endpoint(**self._attrs)

        def addresses(self, value: List[str], /) -> Self:
            """
            addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. Consumers must handle different types of addresses in the context of their own capabilities. This must contain at least one address but no more than 100. These are all assumed to be fungible and clients may choose to only use the first element. Refer to: https://issue.k8s.io/106267
            """
            return self._set("addresses", value)

        @overload
        def conditions(
            self, value_or_callback: Optional[EndpointConditions], /
        ) -> "Endpoint.Builder": ...

        @overload
        def conditions(
            self,
            value_or_callback: Callable[
                [EndpointConditions.Builder],
                EndpointConditions.Builder | EndpointConditions,
            ],
            /,
        ) -> "Endpoint.Builder": ...

        @overload
        def conditions(
            self, value_or_callback: Never = ...
        ) -> "EndpointConditions.BuilderContext": ...

        def conditions(self, value_or_callback=None, /):
            """
            conditions contains information about the current status of the endpoint.
            """
            if self._in_context and value_or_callback is None:
                context = EndpointConditions.BuilderContext()
                context._parent_builder = self
                context._field_name = "conditions"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(EndpointConditions.builder())
                if isinstance(output, EndpointConditions.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("conditions", value)

        def deprecated_topology(self, value: Optional[Dict[str, str]], /) -> Self:
            """
            deprecatedTopology contains topology information part of the v1beta1 API. This field is deprecated, and will be removed when the v1beta1 API is removed (no sooner than kubernetes v1.24).  While this field can hold values, it is not writable through the v1 API, and any attempts to write to it will be silently ignored. Topology information can be found in the zone and nodeName fields instead.
            """
            return self._set("deprecated_topology", value)

        @overload
        def hints(self, value_or_callback: Optional[EndpointHints], /) -> "Endpoint.Builder": ...

        @overload
        def hints(
            self,
            value_or_callback: Callable[
                [EndpointHints.Builder], EndpointHints.Builder | EndpointHints
            ],
            /,
        ) -> "Endpoint.Builder": ...

        @overload
        def hints(self, value_or_callback: Never = ...) -> "EndpointHints.BuilderContext": ...

        def hints(self, value_or_callback=None, /):
            """
            hints contains information associated with how an endpoint should be consumed.
            """
            if self._in_context and value_or_callback is None:
                context = EndpointHints.BuilderContext()
                context._parent_builder = self
                context._field_name = "hints"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(EndpointHints.builder())
                if isinstance(output, EndpointHints.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("hints", value)

        def hostname(self, value: Optional[str], /) -> Self:
            """
            hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname should be considered fungible (e.g. multiple A values in DNS). Must be lowercase and pass DNS Label (RFC 1123) validation.
            """
            return self._set("hostname", value)

        def node_name(self, value: Optional[str], /) -> Self:
            """
            nodeName represents the name of the Node hosting this endpoint. This can be used to determine endpoints local to a Node.
            """
            return self._set("node_name", value)

        @overload
        def target_ref(
            self, value_or_callback: Optional[v1.ObjectReference], /
        ) -> "Endpoint.Builder": ...

        @overload
        def target_ref(
            self,
            value_or_callback: Callable[
                [v1.ObjectReference.Builder],
                v1.ObjectReference.Builder | v1.ObjectReference,
            ],
            /,
        ) -> "Endpoint.Builder": ...

        @overload
        def target_ref(
            self, value_or_callback: Never = ...
        ) -> "v1.ObjectReference.BuilderContext": ...

        def target_ref(self, value_or_callback=None, /):
            """
            targetRef is a reference to a Kubernetes object that represents this endpoint.
            """
            if self._in_context and value_or_callback is None:
                context = v1.ObjectReference.BuilderContext()
                context._parent_builder = self
                context._field_name = "target_ref"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(v1.ObjectReference.builder())
                if isinstance(output, v1.ObjectReference.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("target_ref", value)

        def zone(self, value: Optional[str], /) -> Self:
            """
            zone is the name of the Zone this endpoint exists in.
            """
            return self._set("zone", value)

    class BuilderContext(BuilderContextBase["Endpoint.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = Endpoint.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for Endpoint."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["Endpoint", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use Endpoint.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    addresses: List[str]
    """
    addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. Consumers must handle different types of addresses in the context of their own capabilities. This must contain at least one address but no more than 100. These are all assumed to be fungible and clients may choose to only use the first element. Refer to: https://issue.k8s.io/106267
    """
    conditions: Optional[EndpointConditions] = None
    """
    conditions contains information about the current status of the endpoint.
    """
    deprecated_topology: Annotated[Optional[Dict[str, str]], Field(alias="deprecatedTopology")] = (
        None
    )
    """
    deprecatedTopology contains topology information part of the v1beta1 API. This field is deprecated, and will be removed when the v1beta1 API is removed (no sooner than kubernetes v1.24).  While this field can hold values, it is not writable through the v1 API, and any attempts to write to it will be silently ignored. Topology information can be found in the zone and nodeName fields instead.
    """
    hints: Optional[EndpointHints] = None
    """
    hints contains information associated with how an endpoint should be consumed.
    """
    hostname: Optional[str] = None
    """
    hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname should be considered fungible (e.g. multiple A values in DNS). Must be lowercase and pass DNS Label (RFC 1123) validation.
    """
    node_name: Annotated[Optional[str], Field(alias="nodeName")] = None
    """
    nodeName represents the name of the Node hosting this endpoint. This can be used to determine endpoints local to a Node.
    """
    target_ref: Annotated[Optional[v1.ObjectReference], Field(alias="targetRef")] = None
    """
    targetRef is a reference to a Kubernetes object that represents this endpoint.
    """
    zone: Optional[str] = None
    """
    zone is the name of the Zone this endpoint exists in.
    """


class EndpointSlice(Resource):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["EndpointSlice"]:
            return EndpointSlice

        def build(self) -> "EndpointSlice":
            return EndpointSlice(**self._attrs)

        def address_type(self, value: str, /) -> Self:
            """
            addressType specifies the type of address carried by this EndpointSlice. All addresses in this slice must be the same type. This field is immutable after creation. The following address types are currently supported: * IPv4: Represents an IPv4 Address. * IPv6: Represents an IPv6 Address. * FQDN: Represents a Fully Qualified Domain Name.
            """
            return self._set("address_type", value)

        def api_version(self, value: Optional[Literal["discovery.k8s.io/v1"]], /) -> Self:
            """
            APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
            """
            return self._set("api_version", value)

        @overload
        def endpoints(self, value_or_callback: List[Endpoint], /) -> "EndpointSlice.Builder": ...

        @overload
        def endpoints(
            self,
            value_or_callback: Callable[
                [GenericListBuilder[Endpoint, Endpoint.Builder]],
                GenericListBuilder[Endpoint, Endpoint.Builder] | List[Endpoint],
            ],
            /,
        ) -> "EndpointSlice.Builder": ...

        @overload
        def endpoints(
            self, value_or_callback: Never = ...
        ) -> ListBuilderContext[Endpoint.Builder]: ...

        def endpoints(self, value_or_callback=None, /):
            """
            endpoints is a list of unique endpoints in this slice. Each slice may include a maximum of 1000 endpoints.
            """
            if self._in_context and value_or_callback is None:
                context = ListBuilderContext[Endpoint.Builder]()
                context._parent_builder = self
                context._field_name = "endpoints"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(Endpoint.list_builder())
                if isinstance(output, GenericListBuilder):
                    value = output.build()
                else:
                    value = output
            return self._set("endpoints", value)

        def kind(self, value: Optional[Literal["EndpointSlice"]], /) -> Self:
            """
            Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
            """
            return self._set("kind", value)

        @overload
        def metadata(
            self, value_or_callback: Optional[apimachinery.ObjectMeta], /
        ) -> "EndpointSlice.Builder": ...

        @overload
        def metadata(
            self,
            value_or_callback: Callable[
                [apimachinery.ObjectMeta.Builder],
                apimachinery.ObjectMeta.Builder | apimachinery.ObjectMeta,
            ],
            /,
        ) -> "EndpointSlice.Builder": ...

        @overload
        def metadata(
            self, value_or_callback: Never = ...
        ) -> "apimachinery.ObjectMeta.BuilderContext": ...

        def metadata(self, value_or_callback=None, /):
            """
            Standard object's metadata.
            """
            if self._in_context and value_or_callback is None:
                context = apimachinery.ObjectMeta.BuilderContext()
                context._parent_builder = self
                context._field_name = "metadata"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(apimachinery.ObjectMeta.builder())
                if isinstance(output, apimachinery.ObjectMeta.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("metadata", value)

        @overload
        def ports(self, value_or_callback: List[EndpointPort], /) -> "EndpointSlice.Builder": ...

        @overload
        def ports(
            self,
            value_or_callback: Callable[
                [GenericListBuilder[EndpointPort, EndpointPort.Builder]],
                GenericListBuilder[EndpointPort, EndpointPort.Builder] | List[EndpointPort],
            ],
            /,
        ) -> "EndpointSlice.Builder": ...

        @overload
        def ports(
            self, value_or_callback: Never = ...
        ) -> ListBuilderContext[EndpointPort.Builder]: ...

        def ports(self, value_or_callback=None, /):
            """
            ports specifies the list of network ports exposed by each endpoint in this slice. Each port must have a unique name. When ports is empty, it indicates that there are no defined ports. When a port is defined with a nil port value, it indicates "all ports". Each slice may include a maximum of 100 ports.
            """
            if self._in_context and value_or_callback is None:
                context = ListBuilderContext[EndpointPort.Builder]()
                context._parent_builder = self
                context._field_name = "ports"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(EndpointPort.list_builder())
                if isinstance(output, GenericListBuilder):
                    value = output.build()
                else:
                    value = output
            return self._set("ports", value)

    class BuilderContext(BuilderContextBase["EndpointSlice.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = EndpointSlice.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for EndpointSlice."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["EndpointSlice", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use EndpointSlice.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    address_type: Annotated[str, Field(alias="addressType")]
    """
    addressType specifies the type of address carried by this EndpointSlice. All addresses in this slice must be the same type. This field is immutable after creation. The following address types are currently supported: * IPv4: Represents an IPv4 Address. * IPv6: Represents an IPv6 Address. * FQDN: Represents a Fully Qualified Domain Name.
    """
    api_version: Annotated[Optional[Literal["discovery.k8s.io/v1"]], Field(alias="apiVersion")] = (
        "discovery.k8s.io/v1"
    )
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    endpoints: List[Endpoint]
    """
    endpoints is a list of unique endpoints in this slice. Each slice may include a maximum of 1000 endpoints.
    """
    kind: Optional[Literal["EndpointSlice"]] = "EndpointSlice"
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: Optional[apimachinery.ObjectMeta] = None
    """
    Standard object's metadata.
    """
    ports: Optional[List[EndpointPort]] = None
    """
    ports specifies the list of network ports exposed by each endpoint in this slice. Each port must have a unique name. When ports is empty, it indicates that there are no defined ports. When a port is defined with a nil port value, it indicates "all ports". Each slice may include a maximum of 100 ports.
    """


EndpointSliceList = ResourceList["EndpointSlice"]
