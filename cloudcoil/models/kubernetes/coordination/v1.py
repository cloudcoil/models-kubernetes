# Generated by cloudcoil-model-codegen v0.4.3
# DO NOT EDIT

from __future__ import annotations

from typing import (
    Annotated,
    Callable,
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
    Never,
    Self,
)
from cloudcoil.resources import Resource, ResourceList


class LeaseSpec(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["LeaseSpec"]:
            return LeaseSpec

        def build(self) -> "LeaseSpec":
            return LeaseSpec(**self._attrs)

        @overload
        def acquire_time(
            self, value_or_callback: Optional[apimachinery.MicroTime], /
        ) -> "LeaseSpec.Builder": ...

        @overload
        def acquire_time(
            self,
            value_or_callback: Callable[
                [apimachinery.MicroTime.Builder],
                apimachinery.MicroTime.Builder | apimachinery.MicroTime,
            ],
            /,
        ) -> "LeaseSpec.Builder": ...

        @overload
        def acquire_time(
            self, value_or_callback: Never = ...
        ) -> "apimachinery.MicroTime.BuilderContext": ...

        def acquire_time(self, value_or_callback=None, /):
            """
            acquireTime is a time when the current lease was acquired.
            """
            if self._in_context and value_or_callback is None:
                context = apimachinery.MicroTime.BuilderContext()
                context._parent_builder = self
                context._field_name = "acquire_time"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(apimachinery.MicroTime.builder())
                if isinstance(output, apimachinery.MicroTime.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("acquire_time", value)

        def holder_identity(self, value: Optional[str], /) -> Self:
            """
            holderIdentity contains the identity of the holder of a current lease.
            """
            return self._set("holder_identity", value)

        def lease_duration_seconds(self, value: Optional[int], /) -> Self:
            """
            leaseDurationSeconds is a duration that candidates for a lease need to wait to force acquire it. This is measure against time of last observed renewTime.
            """
            return self._set("lease_duration_seconds", value)

        def lease_transitions(self, value: Optional[int], /) -> Self:
            """
            leaseTransitions is the number of transitions of a lease between holders.
            """
            return self._set("lease_transitions", value)

        @overload
        def renew_time(
            self, value_or_callback: Optional[apimachinery.MicroTime], /
        ) -> "LeaseSpec.Builder": ...

        @overload
        def renew_time(
            self,
            value_or_callback: Callable[
                [apimachinery.MicroTime.Builder],
                apimachinery.MicroTime.Builder | apimachinery.MicroTime,
            ],
            /,
        ) -> "LeaseSpec.Builder": ...

        @overload
        def renew_time(
            self, value_or_callback: Never = ...
        ) -> "apimachinery.MicroTime.BuilderContext": ...

        def renew_time(self, value_or_callback=None, /):
            """
            renewTime is a time when the current holder of a lease has last updated the lease.
            """
            if self._in_context and value_or_callback is None:
                context = apimachinery.MicroTime.BuilderContext()
                context._parent_builder = self
                context._field_name = "renew_time"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(apimachinery.MicroTime.builder())
                if isinstance(output, apimachinery.MicroTime.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("renew_time", value)

    class BuilderContext(BuilderContextBase["LeaseSpec.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = LeaseSpec.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for LeaseSpec."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["LeaseSpec", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use LeaseSpec.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    acquire_time: Annotated[Optional[apimachinery.MicroTime], Field(alias="acquireTime")] = None
    """
    acquireTime is a time when the current lease was acquired.
    """
    holder_identity: Annotated[Optional[str], Field(alias="holderIdentity")] = None
    """
    holderIdentity contains the identity of the holder of a current lease.
    """
    lease_duration_seconds: Annotated[Optional[int], Field(alias="leaseDurationSeconds")] = None
    """
    leaseDurationSeconds is a duration that candidates for a lease need to wait to force acquire it. This is measure against time of last observed renewTime.
    """
    lease_transitions: Annotated[Optional[int], Field(alias="leaseTransitions")] = None
    """
    leaseTransitions is the number of transitions of a lease between holders.
    """
    renew_time: Annotated[Optional[apimachinery.MicroTime], Field(alias="renewTime")] = None
    """
    renewTime is a time when the current holder of a lease has last updated the lease.
    """


class Lease(Resource):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["Lease"]:
            return Lease

        def build(self) -> "Lease":
            return Lease(**self._attrs)

        def api_version(self, value: Optional[Literal["coordination.k8s.io/v1"]], /) -> Self:
            """
            APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
            """
            return self._set("api_version", value)

        def kind(self, value: Optional[Literal["Lease"]], /) -> Self:
            """
            Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
            """
            return self._set("kind", value)

        @overload
        def metadata(
            self, value_or_callback: Optional[apimachinery.ObjectMeta], /
        ) -> "Lease.Builder": ...

        @overload
        def metadata(
            self,
            value_or_callback: Callable[
                [apimachinery.ObjectMeta.Builder],
                apimachinery.ObjectMeta.Builder | apimachinery.ObjectMeta,
            ],
            /,
        ) -> "Lease.Builder": ...

        @overload
        def metadata(
            self, value_or_callback: Never = ...
        ) -> "apimachinery.ObjectMeta.BuilderContext": ...

        def metadata(self, value_or_callback=None, /):
            """
            More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
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
        def spec(self, value_or_callback: Optional[LeaseSpec], /) -> "Lease.Builder": ...

        @overload
        def spec(
            self,
            value_or_callback: Callable[[LeaseSpec.Builder], LeaseSpec.Builder | LeaseSpec],
            /,
        ) -> "Lease.Builder": ...

        @overload
        def spec(self, value_or_callback: Never = ...) -> "LeaseSpec.BuilderContext": ...

        def spec(self, value_or_callback=None, /):
            """
            spec contains the specification of the Lease. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
            """
            if self._in_context and value_or_callback is None:
                context = LeaseSpec.BuilderContext()
                context._parent_builder = self
                context._field_name = "spec"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(LeaseSpec.builder())
                if isinstance(output, LeaseSpec.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("spec", value)

    class BuilderContext(BuilderContextBase["Lease.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = Lease.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for Lease."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["Lease", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use Lease.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    api_version: Annotated[
        Optional[Literal["coordination.k8s.io/v1"]], Field(alias="apiVersion")
    ] = "coordination.k8s.io/v1"
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: Optional[Literal["Lease"]] = "Lease"
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: Optional[apimachinery.ObjectMeta] = None
    """
    More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    spec: Optional[LeaseSpec] = None
    """
    spec contains the specification of the Lease. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """


LeaseList = ResourceList["Lease"]
