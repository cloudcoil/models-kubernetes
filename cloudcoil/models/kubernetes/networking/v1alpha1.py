# Generated by cloudcoil-model-codegen v0.4.6
# DO NOT EDIT

from __future__ import annotations

from typing import (
    Annotated,
    Callable,
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


class ParentReference(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["ParentReference"]:
            return ParentReference

        def build(self) -> "ParentReference":
            return ParentReference(**self._attrs)

        def group(self, value: Optional[str], /) -> Self:
            """
            Group is the group of the object being referenced.
            """
            return self._set("group", value)

        def name(self, value: Optional[str], /) -> Self:
            """
            Name is the name of the object being referenced.
            """
            return self._set("name", value)

        def namespace(self, value: Optional[str], /) -> Self:
            """
            Namespace is the namespace of the object being referenced.
            """
            return self._set("namespace", value)

        def resource(self, value: Optional[str], /) -> Self:
            """
            Resource is the resource of the object being referenced.
            """
            return self._set("resource", value)

    class BuilderContext(BuilderContextBase["ParentReference.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = ParentReference.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for ParentReference."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["ParentReference", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use ParentReference.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    group: Optional[str] = None
    """
    Group is the group of the object being referenced.
    """
    name: Optional[str] = None
    """
    Name is the name of the object being referenced.
    """
    namespace: Optional[str] = None
    """
    Namespace is the namespace of the object being referenced.
    """
    resource: Optional[str] = None
    """
    Resource is the resource of the object being referenced.
    """


class ServiceCIDRSpec(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["ServiceCIDRSpec"]:
            return ServiceCIDRSpec

        def build(self) -> "ServiceCIDRSpec":
            return ServiceCIDRSpec(**self._attrs)

        def cidrs(self, value: Optional[List[str]], /) -> Self:
            """
            CIDRs defines the IP blocks in CIDR notation (e.g. "192.168.0.0/24" or "2001:db8::/64") from which to assign service cluster IPs. Max of two CIDRs is allowed, one of each IP family. This field is immutable.
            """
            return self._set("cidrs", value)

    class BuilderContext(BuilderContextBase["ServiceCIDRSpec.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = ServiceCIDRSpec.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for ServiceCIDRSpec."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["ServiceCIDRSpec", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use ServiceCIDRSpec.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    cidrs: Optional[List[str]] = None
    """
    CIDRs defines the IP blocks in CIDR notation (e.g. "192.168.0.0/24" or "2001:db8::/64") from which to assign service cluster IPs. Max of two CIDRs is allowed, one of each IP family. This field is immutable.
    """


class IPAddressSpec(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["IPAddressSpec"]:
            return IPAddressSpec

        def build(self) -> "IPAddressSpec":
            return IPAddressSpec(**self._attrs)

        @overload
        def parent_ref(
            self, value_or_callback: Optional[ParentReference], /
        ) -> "IPAddressSpec.Builder": ...

        @overload
        def parent_ref(
            self,
            value_or_callback: Callable[
                [ParentReference.Builder], ParentReference.Builder | ParentReference
            ],
            /,
        ) -> "IPAddressSpec.Builder": ...

        @overload
        def parent_ref(
            self, value_or_callback: Never = ...
        ) -> "ParentReference.BuilderContext": ...

        def parent_ref(self, value_or_callback=None, /):
            """
            ParentRef references the resource that an IPAddress is attached to. An IPAddress must reference a parent object.
            """
            if self._in_context and value_or_callback is None:
                context = ParentReference.BuilderContext()
                context._parent_builder = self
                context._field_name = "parent_ref"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(ParentReference.builder())
                if isinstance(output, ParentReference.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("parent_ref", value)

    class BuilderContext(BuilderContextBase["IPAddressSpec.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = IPAddressSpec.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for IPAddressSpec."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["IPAddressSpec", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use IPAddressSpec.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    parent_ref: Annotated[Optional[ParentReference], Field(alias="parentRef")] = None
    """
    ParentRef references the resource that an IPAddress is attached to. An IPAddress must reference a parent object.
    """


class IPAddress(Resource):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["IPAddress"]:
            return IPAddress

        def build(self) -> "IPAddress":
            return IPAddress(**self._attrs)

        def api_version(self, value: Optional[Literal["networking.k8s.io/v1alpha1"]], /) -> Self:
            """
            APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
            """
            return self._set("api_version", value)

        def kind(self, value: Optional[Literal["IPAddress"]], /) -> Self:
            """
            Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
            """
            return self._set("kind", value)

        @overload
        def metadata(
            self, value_or_callback: Optional[apimachinery.ObjectMeta], /
        ) -> "IPAddress.Builder": ...

        @overload
        def metadata(
            self,
            value_or_callback: Callable[
                [apimachinery.ObjectMeta.Builder],
                apimachinery.ObjectMeta.Builder | apimachinery.ObjectMeta,
            ],
            /,
        ) -> "IPAddress.Builder": ...

        @overload
        def metadata(
            self, value_or_callback: Never = ...
        ) -> "apimachinery.ObjectMeta.BuilderContext": ...

        def metadata(self, value_or_callback=None, /):
            """
            Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
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
        def spec(self, value_or_callback: Optional[IPAddressSpec], /) -> "IPAddress.Builder": ...

        @overload
        def spec(
            self,
            value_or_callback: Callable[
                [IPAddressSpec.Builder], IPAddressSpec.Builder | IPAddressSpec
            ],
            /,
        ) -> "IPAddress.Builder": ...

        @overload
        def spec(self, value_or_callback: Never = ...) -> "IPAddressSpec.BuilderContext": ...

        def spec(self, value_or_callback=None, /):
            """
            spec is the desired state of the IPAddress. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
            """
            if self._in_context and value_or_callback is None:
                context = IPAddressSpec.BuilderContext()
                context._parent_builder = self
                context._field_name = "spec"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(IPAddressSpec.builder())
                if isinstance(output, IPAddressSpec.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("spec", value)

    class BuilderContext(BuilderContextBase["IPAddress.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = IPAddress.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for IPAddress."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["IPAddress", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use IPAddress.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    api_version: Annotated[
        Optional[Literal["networking.k8s.io/v1alpha1"]], Field(alias="apiVersion")
    ] = "networking.k8s.io/v1alpha1"
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: Optional[Literal["IPAddress"]] = "IPAddress"
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: Optional[apimachinery.ObjectMeta] = None
    """
    Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    spec: Optional[IPAddressSpec] = None
    """
    spec is the desired state of the IPAddress. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """


IPAddressList = ResourceList["IPAddress"]


class ServiceCIDRStatus(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["ServiceCIDRStatus"]:
            return ServiceCIDRStatus

        def build(self) -> "ServiceCIDRStatus":
            return ServiceCIDRStatus(**self._attrs)

        @overload
        def conditions(
            self, value_or_callback: List[apimachinery.Condition], /
        ) -> "ServiceCIDRStatus.Builder": ...

        @overload
        def conditions(
            self,
            value_or_callback: Callable[
                [GenericListBuilder[apimachinery.Condition, apimachinery.Condition.Builder]],
                GenericListBuilder[apimachinery.Condition, apimachinery.Condition.Builder]
                | List[apimachinery.Condition],
            ],
            /,
        ) -> "ServiceCIDRStatus.Builder": ...

        @overload
        def conditions(
            self, value_or_callback: Never = ...
        ) -> ListBuilderContext[apimachinery.Condition.Builder]: ...

        def conditions(self, value_or_callback=None, /):
            """
            conditions holds an array of metav1.Condition that describe the state of the ServiceCIDR. Current service state
            """
            if self._in_context and value_or_callback is None:
                context = ListBuilderContext[apimachinery.Condition.Builder]()
                context._parent_builder = self
                context._field_name = "conditions"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(apimachinery.Condition.list_builder())
                if isinstance(output, GenericListBuilder):
                    value = output.build()
                else:
                    value = output
            return self._set("conditions", value)

    class BuilderContext(BuilderContextBase["ServiceCIDRStatus.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = ServiceCIDRStatus.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for ServiceCIDRStatus."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["ServiceCIDRStatus", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use ServiceCIDRStatus.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    conditions: Optional[List[apimachinery.Condition]] = None
    """
    conditions holds an array of metav1.Condition that describe the state of the ServiceCIDR. Current service state
    """


class ServiceCIDR(Resource):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["ServiceCIDR"]:
            return ServiceCIDR

        def build(self) -> "ServiceCIDR":
            return ServiceCIDR(**self._attrs)

        def api_version(self, value: Optional[Literal["networking.k8s.io/v1alpha1"]], /) -> Self:
            """
            APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
            """
            return self._set("api_version", value)

        def kind(self, value: Optional[Literal["ServiceCIDR"]], /) -> Self:
            """
            Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
            """
            return self._set("kind", value)

        @overload
        def metadata(
            self, value_or_callback: Optional[apimachinery.ObjectMeta], /
        ) -> "ServiceCIDR.Builder": ...

        @overload
        def metadata(
            self,
            value_or_callback: Callable[
                [apimachinery.ObjectMeta.Builder],
                apimachinery.ObjectMeta.Builder | apimachinery.ObjectMeta,
            ],
            /,
        ) -> "ServiceCIDR.Builder": ...

        @overload
        def metadata(
            self, value_or_callback: Never = ...
        ) -> "apimachinery.ObjectMeta.BuilderContext": ...

        def metadata(self, value_or_callback=None, /):
            """
            Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
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
        def spec(
            self, value_or_callback: Optional[ServiceCIDRSpec], /
        ) -> "ServiceCIDR.Builder": ...

        @overload
        def spec(
            self,
            value_or_callback: Callable[
                [ServiceCIDRSpec.Builder], ServiceCIDRSpec.Builder | ServiceCIDRSpec
            ],
            /,
        ) -> "ServiceCIDR.Builder": ...

        @overload
        def spec(self, value_or_callback: Never = ...) -> "ServiceCIDRSpec.BuilderContext": ...

        def spec(self, value_or_callback=None, /):
            """
            spec is the desired state of the ServiceCIDR. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
            """
            if self._in_context and value_or_callback is None:
                context = ServiceCIDRSpec.BuilderContext()
                context._parent_builder = self
                context._field_name = "spec"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(ServiceCIDRSpec.builder())
                if isinstance(output, ServiceCIDRSpec.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("spec", value)

        @overload
        def status(
            self, value_or_callback: Optional[ServiceCIDRStatus], /
        ) -> "ServiceCIDR.Builder": ...

        @overload
        def status(
            self,
            value_or_callback: Callable[
                [ServiceCIDRStatus.Builder],
                ServiceCIDRStatus.Builder | ServiceCIDRStatus,
            ],
            /,
        ) -> "ServiceCIDR.Builder": ...

        @overload
        def status(self, value_or_callback: Never = ...) -> "ServiceCIDRStatus.BuilderContext": ...

        def status(self, value_or_callback=None, /):
            """
            status represents the current state of the ServiceCIDR. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
            """
            if self._in_context and value_or_callback is None:
                context = ServiceCIDRStatus.BuilderContext()
                context._parent_builder = self
                context._field_name = "status"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(ServiceCIDRStatus.builder())
                if isinstance(output, ServiceCIDRStatus.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("status", value)

    class BuilderContext(BuilderContextBase["ServiceCIDR.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = ServiceCIDR.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for ServiceCIDR."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["ServiceCIDR", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use ServiceCIDR.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    api_version: Annotated[
        Optional[Literal["networking.k8s.io/v1alpha1"]], Field(alias="apiVersion")
    ] = "networking.k8s.io/v1alpha1"
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: Optional[Literal["ServiceCIDR"]] = "ServiceCIDR"
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: Optional[apimachinery.ObjectMeta] = None
    """
    Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    spec: Optional[ServiceCIDRSpec] = None
    """
    spec is the desired state of the ServiceCIDR. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """
    status: Optional[ServiceCIDRStatus] = None
    """
    status represents the current state of the ServiceCIDR. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """


ServiceCIDRList = ResourceList["ServiceCIDR"]
