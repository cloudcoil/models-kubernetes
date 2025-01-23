# Generated by cloudcoil-model-codegen v0.2.0
# DO NOT EDIT

from __future__ import annotations

from typing import Annotated, Callable, Literal, Optional, Type, Union

from pydantic import Field

from cloudcoil import apimachinery
from cloudcoil.pydantic import BaseBuilder, BaseModel, GenericListBuilder, Self
from cloudcoil.resources import Resource, ResourceList


class LeaseCandidateSpec(BaseModel):
    class Builder(BaseBuilder):
        @property
        def base_class(self) -> Type["LeaseCandidateSpec"]:
            return LeaseCandidateSpec

        def build(self) -> "LeaseCandidateSpec":
            return LeaseCandidateSpec(**self._attrs)

        def binary_version(self, value: str) -> Self:
            return self._set("binary_version", value)

        def emulation_version(self, value: Optional[str]) -> Self:
            return self._set("emulation_version", value)

        def lease_name(self, value: str) -> Self:
            return self._set("lease_name", value)

        """  """

        def ping_time(
            self,
            value_or_callback: Union[
                Optional[apimachinery.MicroTime],
                Callable[[apimachinery.MicroTime.Builder], apimachinery.MicroTime.Builder],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(apimachinery.MicroTime.builder()).build()
            return self._set("ping_time", value)

        """  """

        def renew_time(
            self,
            value_or_callback: Union[
                Optional[apimachinery.MicroTime],
                Callable[[apimachinery.MicroTime.Builder], apimachinery.MicroTime.Builder],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(apimachinery.MicroTime.builder()).build()
            return self._set("renew_time", value)

        def strategy(self, value: str) -> Self:
            return self._set("strategy", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    class ListBuilder(GenericListBuilder["LeaseCandidateSpec", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use LeaseCandidateSpec.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    binary_version: Annotated[
        str,
        Field(
            alias="binaryVersion",
            description="BinaryVersion is the binary version. It must be in a semver format without leading `v`. This field is required.",
        ),
    ]
    emulation_version: Annotated[
        Optional[str],
        Field(
            alias="emulationVersion",
            description='EmulationVersion is the emulation version. It must be in a semver format without leading `v`. EmulationVersion must be less than or equal to BinaryVersion. This field is required when strategy is "OldestEmulationVersion"',
        ),
    ] = None
    lease_name: Annotated[
        str,
        Field(
            alias="leaseName",
            description="LeaseName is the name of the lease for which this candidate is contending. This field is immutable.",
        ),
    ]
    ping_time: Annotated[
        Optional[apimachinery.MicroTime],
        Field(
            alias="pingTime",
            description="PingTime is the last time that the server has requested the LeaseCandidate to renew. It is only done during leader election to check if any LeaseCandidates have become ineligible. When PingTime is updated, the LeaseCandidate will respond by updating RenewTime.",
        ),
    ] = None
    renew_time: Annotated[
        Optional[apimachinery.MicroTime],
        Field(
            alias="renewTime",
            description="RenewTime is the time that the LeaseCandidate was last updated. Any time a Lease needs to do leader election, the PingTime field is updated to signal to the LeaseCandidate that they should update the RenewTime. Old LeaseCandidate objects are also garbage collected if it has been hours since the last renew. The PingTime field is updated regularly to prevent garbage collection for still active LeaseCandidates.",
        ),
    ] = None
    strategy: Annotated[
        str,
        Field(
            description="Strategy is the strategy that coordinated leader election will use for picking the leader. If multiple candidates for the same Lease return different strategies, the strategy provided by the candidate with the latest BinaryVersion will be used. If there is still conflict, this is a user error and coordinated leader election will not operate the Lease until resolved. (Alpha) Using this field requires the CoordinatedLeaderElection feature gate to be enabled."
        ),
    ]


class LeaseCandidate(Resource):
    class Builder(BaseBuilder):
        @property
        def base_class(self) -> Type["LeaseCandidate"]:
            return LeaseCandidate

        def build(self) -> "LeaseCandidate":
            return LeaseCandidate(**self._attrs)

        def api_version(self, value: Optional[Literal["coordination.k8s.io/v1alpha2"]]) -> Self:
            return self._set("api_version", value)

        def kind(self, value: Optional[Literal["LeaseCandidate"]]) -> Self:
            return self._set("kind", value)

        """  """

        def metadata(
            self,
            value_or_callback: Union[
                Optional[apimachinery.ObjectMeta],
                Callable[[apimachinery.ObjectMeta.Builder], apimachinery.ObjectMeta.Builder],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(apimachinery.ObjectMeta.builder()).build()
            return self._set("metadata", value)

        """  """

        def spec(
            self,
            value_or_callback: Union[
                Optional[LeaseCandidateSpec],
                Callable[[LeaseCandidateSpec.Builder], LeaseCandidateSpec.Builder],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(LeaseCandidateSpec.builder()).build()
            return self._set("spec", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    class ListBuilder(GenericListBuilder["LeaseCandidate", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use LeaseCandidate.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    api_version: Annotated[
        Optional[Literal["coordination.k8s.io/v1alpha2"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "coordination.k8s.io/v1alpha2"
    kind: Annotated[
        Optional[Literal["LeaseCandidate"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "LeaseCandidate"
    metadata: Annotated[
        Optional[apimachinery.ObjectMeta],
        Field(
            description="More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    ] = None
    spec: Annotated[
        Optional[LeaseCandidateSpec],
        Field(
            description="spec contains the specification of the Lease. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status"
        ),
    ] = None


LeaseCandidateList = ResourceList["LeaseCandidate"]
