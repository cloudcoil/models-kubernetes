# Generated by cloudcoil-model-codegen v0.5.5
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


class LeaseCandidateSpec(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["LeaseCandidateSpec"]:
            return LeaseCandidateSpec

        def build(self) -> "LeaseCandidateSpec":
            return LeaseCandidateSpec(**self._attrs)

        def binary_version(self, value: str, /) -> Self:
            """
            BinaryVersion is the binary version. It must be in a semver format without leading `v`. This field is required.
            """
            return self._set("binary_version", value)

        def emulation_version(self, value: Optional[str], /) -> Self:
            """
            EmulationVersion is the emulation version. It must be in a semver format without leading `v`. EmulationVersion must be less than or equal to BinaryVersion. This field is required when strategy is "OldestEmulationVersion"
            """
            return self._set("emulation_version", value)

        def lease_name(self, value: str, /) -> Self:
            """
            LeaseName is the name of the lease for which this candidate is contending. This field is immutable.
            """
            return self._set("lease_name", value)

        @overload
        def ping_time(
            self, value_or_callback: Optional[apimachinery.MicroTime], /
        ) -> "LeaseCandidateSpec.Builder": ...

        @overload
        def ping_time(
            self,
            value_or_callback: Callable[
                [apimachinery.MicroTime.Builder],
                apimachinery.MicroTime.Builder | apimachinery.MicroTime,
            ],
            /,
        ) -> "LeaseCandidateSpec.Builder": ...

        @overload
        def ping_time(
            self, value_or_callback: Never = ...
        ) -> "apimachinery.MicroTime.BuilderContext": ...

        def ping_time(self, value_or_callback=None, /):
            """
            PingTime is the last time that the server has requested the LeaseCandidate to renew. It is only done during leader election to check if any LeaseCandidates have become ineligible. When PingTime is updated, the LeaseCandidate will respond by updating RenewTime.
            """
            if self._in_context and value_or_callback is None:
                context = apimachinery.MicroTime.BuilderContext()
                context._parent_builder = self
                context._field_name = "ping_time"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(apimachinery.MicroTime.builder())
                if isinstance(output, apimachinery.MicroTime.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("ping_time", value)

        @overload
        def renew_time(
            self, value_or_callback: Optional[apimachinery.MicroTime], /
        ) -> "LeaseCandidateSpec.Builder": ...

        @overload
        def renew_time(
            self,
            value_or_callback: Callable[
                [apimachinery.MicroTime.Builder],
                apimachinery.MicroTime.Builder | apimachinery.MicroTime,
            ],
            /,
        ) -> "LeaseCandidateSpec.Builder": ...

        @overload
        def renew_time(
            self, value_or_callback: Never = ...
        ) -> "apimachinery.MicroTime.BuilderContext": ...

        def renew_time(self, value_or_callback=None, /):
            """
            RenewTime is the time that the LeaseCandidate was last updated. Any time a Lease needs to do leader election, the PingTime field is updated to signal to the LeaseCandidate that they should update the RenewTime. Old LeaseCandidate objects are also garbage collected if it has been hours since the last renew. The PingTime field is updated regularly to prevent garbage collection for still active LeaseCandidates.
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

        def strategy(self, value: str, /) -> Self:
            """
            Strategy is the strategy that coordinated leader election will use for picking the leader. If multiple candidates for the same Lease return different strategies, the strategy provided by the candidate with the latest BinaryVersion will be used. If there is still conflict, this is a user error and coordinated leader election will not operate the Lease until resolved. (Alpha) Using this field requires the CoordinatedLeaderElection feature gate to be enabled.
            """
            return self._set("strategy", value)

    class BuilderContext(BuilderContextBase["LeaseCandidateSpec.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = LeaseCandidateSpec.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for LeaseCandidateSpec."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["LeaseCandidateSpec", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use LeaseCandidateSpec.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    binary_version: Annotated[str, Field(alias="binaryVersion")]
    """
    BinaryVersion is the binary version. It must be in a semver format without leading `v`. This field is required.
    """
    emulation_version: Annotated[Optional[str], Field(alias="emulationVersion")] = None
    """
    EmulationVersion is the emulation version. It must be in a semver format without leading `v`. EmulationVersion must be less than or equal to BinaryVersion. This field is required when strategy is "OldestEmulationVersion"
    """
    lease_name: Annotated[str, Field(alias="leaseName")]
    """
    LeaseName is the name of the lease for which this candidate is contending. This field is immutable.
    """
    ping_time: Annotated[Optional[apimachinery.MicroTime], Field(alias="pingTime")] = None
    """
    PingTime is the last time that the server has requested the LeaseCandidate to renew. It is only done during leader election to check if any LeaseCandidates have become ineligible. When PingTime is updated, the LeaseCandidate will respond by updating RenewTime.
    """
    renew_time: Annotated[Optional[apimachinery.MicroTime], Field(alias="renewTime")] = None
    """
    RenewTime is the time that the LeaseCandidate was last updated. Any time a Lease needs to do leader election, the PingTime field is updated to signal to the LeaseCandidate that they should update the RenewTime. Old LeaseCandidate objects are also garbage collected if it has been hours since the last renew. The PingTime field is updated regularly to prevent garbage collection for still active LeaseCandidates.
    """
    strategy: str
    """
    Strategy is the strategy that coordinated leader election will use for picking the leader. If multiple candidates for the same Lease return different strategies, the strategy provided by the candidate with the latest BinaryVersion will be used. If there is still conflict, this is a user error and coordinated leader election will not operate the Lease until resolved. (Alpha) Using this field requires the CoordinatedLeaderElection feature gate to be enabled.
    """


class LeaseCandidate(Resource):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["LeaseCandidate"]:
            return LeaseCandidate

        def build(self) -> "LeaseCandidate":
            return LeaseCandidate(**self._attrs)

        def api_version(self, value: Optional[Literal["coordination.k8s.io/v1alpha2"]], /) -> Self:
            """
            APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
            """
            return self._set("api_version", value)

        def kind(self, value: Optional[Literal["LeaseCandidate"]], /) -> Self:
            """
            Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
            """
            return self._set("kind", value)

        @overload
        def metadata(
            self, value_or_callback: Optional[apimachinery.ObjectMeta], /
        ) -> "LeaseCandidate.Builder": ...

        @overload
        def metadata(
            self,
            value_or_callback: Callable[
                [apimachinery.ObjectMeta.Builder],
                apimachinery.ObjectMeta.Builder | apimachinery.ObjectMeta,
            ],
            /,
        ) -> "LeaseCandidate.Builder": ...

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
        def spec(
            self, value_or_callback: Optional[LeaseCandidateSpec], /
        ) -> "LeaseCandidate.Builder": ...

        @overload
        def spec(
            self,
            value_or_callback: Callable[
                [LeaseCandidateSpec.Builder],
                LeaseCandidateSpec.Builder | LeaseCandidateSpec,
            ],
            /,
        ) -> "LeaseCandidate.Builder": ...

        @overload
        def spec(self, value_or_callback: Never = ...) -> "LeaseCandidateSpec.BuilderContext": ...

        def spec(self, value_or_callback=None, /):
            """
            spec contains the specification of the Lease. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
            """
            if self._in_context and value_or_callback is None:
                context = LeaseCandidateSpec.BuilderContext()
                context._parent_builder = self
                context._field_name = "spec"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(LeaseCandidateSpec.builder())
                if isinstance(output, LeaseCandidateSpec.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("spec", value)

    class BuilderContext(BuilderContextBase["LeaseCandidate.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = LeaseCandidate.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for LeaseCandidate."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["LeaseCandidate", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use LeaseCandidate.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    api_version: Annotated[
        Optional[Literal["coordination.k8s.io/v1alpha2"]], Field(alias="apiVersion")
    ] = "coordination.k8s.io/v1alpha2"
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: Optional[Literal["LeaseCandidate"]] = "LeaseCandidate"
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: Optional[apimachinery.ObjectMeta] = None
    """
    More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    spec: Optional[LeaseCandidateSpec] = None
    """
    spec contains the specification of the Lease. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
    """


LeaseCandidateList = ResourceList["LeaseCandidate"]
