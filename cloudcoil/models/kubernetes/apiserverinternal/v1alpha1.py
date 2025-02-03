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


class ServerStorageVersion(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["ServerStorageVersion"]:
            return ServerStorageVersion

        def build(self) -> "ServerStorageVersion":
            return ServerStorageVersion(**self._attrs)

        def api_server_id(self, value: Optional[str], /) -> Self:
            """
            The ID of the reporting API server.
            """
            return self._set("api_server_id", value)

        def decodable_versions(self, value: Optional[List[str]], /) -> Self:
            """
            The API server can decode objects encoded in these versions. The encodingVersion must be included in the decodableVersions.
            """
            return self._set("decodable_versions", value)

        def encoding_version(self, value: Optional[str], /) -> Self:
            """
            The API server encodes the object to this version when persisting it in the backend (e.g., etcd).
            """
            return self._set("encoding_version", value)

        def served_versions(self, value: Optional[List[str]], /) -> Self:
            """
            The API server can serve these versions. DecodableVersions must include all ServedVersions.
            """
            return self._set("served_versions", value)

    class BuilderContext(BuilderContextBase["ServerStorageVersion.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = ServerStorageVersion.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for ServerStorageVersion."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["ServerStorageVersion", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use ServerStorageVersion.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    api_server_id: Annotated[Optional[str], Field(alias="apiServerID")] = None
    """
    The ID of the reporting API server.
    """
    decodable_versions: Annotated[Optional[List[str]], Field(alias="decodableVersions")] = None
    """
    The API server can decode objects encoded in these versions. The encodingVersion must be included in the decodableVersions.
    """
    encoding_version: Annotated[Optional[str], Field(alias="encodingVersion")] = None
    """
    The API server encodes the object to this version when persisting it in the backend (e.g., etcd).
    """
    served_versions: Annotated[Optional[List[str]], Field(alias="servedVersions")] = None
    """
    The API server can serve these versions. DecodableVersions must include all ServedVersions.
    """


class StorageVersionSpec(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["StorageVersionSpec"]:
            return StorageVersionSpec

        def build(self) -> "StorageVersionSpec":
            return StorageVersionSpec(**self._attrs)

    class BuilderContext(BuilderContextBase["StorageVersionSpec.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = StorageVersionSpec.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for StorageVersionSpec."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["StorageVersionSpec", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use StorageVersionSpec.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    pass


class StorageVersionCondition(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["StorageVersionCondition"]:
            return StorageVersionCondition

        def build(self) -> "StorageVersionCondition":
            return StorageVersionCondition(**self._attrs)

        @overload
        def last_transition_time(
            self, value_or_callback: Optional[apimachinery.Time], /
        ) -> "StorageVersionCondition.Builder": ...

        @overload
        def last_transition_time(
            self,
            value_or_callback: Callable[
                [apimachinery.Time.Builder],
                apimachinery.Time.Builder | apimachinery.Time,
            ],
            /,
        ) -> "StorageVersionCondition.Builder": ...

        @overload
        def last_transition_time(
            self, value_or_callback: Never = ...
        ) -> "apimachinery.Time.BuilderContext": ...

        def last_transition_time(self, value_or_callback=None, /):
            """
            Last time the condition transitioned from one status to another.
            """
            if self._in_context and value_or_callback is None:
                context = apimachinery.Time.BuilderContext()
                context._parent_builder = self
                context._field_name = "last_transition_time"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(apimachinery.Time.builder())
                if isinstance(output, apimachinery.Time.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("last_transition_time", value)

        def message(self, value: str, /) -> Self:
            """
            A human readable message indicating details about the transition.
            """
            return self._set("message", value)

        def observed_generation(self, value: Optional[int], /) -> Self:
            """
            If set, this represents the .metadata.generation that the condition was set based upon.
            """
            return self._set("observed_generation", value)

        def reason(self, value: str, /) -> Self:
            """
            The reason for the condition's last transition.
            """
            return self._set("reason", value)

        def status(self, value: str, /) -> Self:
            """
            Status of the condition, one of True, False, Unknown.
            """
            return self._set("status", value)

        def type(self, value: str, /) -> Self:
            """
            Type of the condition.
            """
            return self._set("type", value)

    class BuilderContext(BuilderContextBase["StorageVersionCondition.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = StorageVersionCondition.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for StorageVersionCondition."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["StorageVersionCondition", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use StorageVersionCondition.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    last_transition_time: Annotated[
        Optional[apimachinery.Time], Field(alias="lastTransitionTime")
    ] = None
    """
    Last time the condition transitioned from one status to another.
    """
    message: str
    """
    A human readable message indicating details about the transition.
    """
    observed_generation: Annotated[Optional[int], Field(alias="observedGeneration")] = None
    """
    If set, this represents the .metadata.generation that the condition was set based upon.
    """
    reason: str
    """
    The reason for the condition's last transition.
    """
    status: str
    """
    Status of the condition, one of True, False, Unknown.
    """
    type: str
    """
    Type of the condition.
    """


class StorageVersionStatus(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["StorageVersionStatus"]:
            return StorageVersionStatus

        def build(self) -> "StorageVersionStatus":
            return StorageVersionStatus(**self._attrs)

        def common_encoding_version(self, value: Optional[str], /) -> Self:
            """
            If all API server instances agree on the same encoding storage version, then this field is set to that version. Otherwise this field is left empty. API servers should finish updating its storageVersionStatus entry before serving write operations, so that this field will be in sync with the reality.
            """
            return self._set("common_encoding_version", value)

        @overload
        def conditions(
            self, value_or_callback: List[StorageVersionCondition], /
        ) -> "StorageVersionStatus.Builder": ...

        @overload
        def conditions(
            self,
            value_or_callback: Callable[
                [GenericListBuilder[StorageVersionCondition, StorageVersionCondition.Builder]],
                GenericListBuilder[StorageVersionCondition, StorageVersionCondition.Builder]
                | List[StorageVersionCondition],
            ],
            /,
        ) -> "StorageVersionStatus.Builder": ...

        @overload
        def conditions(
            self, value_or_callback: Never = ...
        ) -> ListBuilderContext[StorageVersionCondition.Builder]: ...

        def conditions(self, value_or_callback=None, /):
            """
            The latest available observations of the storageVersion's state.
            """
            if self._in_context and value_or_callback is None:
                context = ListBuilderContext[StorageVersionCondition.Builder]()
                context._parent_builder = self
                context._field_name = "conditions"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(StorageVersionCondition.list_builder())
                if isinstance(output, GenericListBuilder):
                    value = output.build()
                else:
                    value = output
            return self._set("conditions", value)

        @overload
        def storage_versions(
            self, value_or_callback: List[ServerStorageVersion], /
        ) -> "StorageVersionStatus.Builder": ...

        @overload
        def storage_versions(
            self,
            value_or_callback: Callable[
                [GenericListBuilder[ServerStorageVersion, ServerStorageVersion.Builder]],
                GenericListBuilder[ServerStorageVersion, ServerStorageVersion.Builder]
                | List[ServerStorageVersion],
            ],
            /,
        ) -> "StorageVersionStatus.Builder": ...

        @overload
        def storage_versions(
            self, value_or_callback: Never = ...
        ) -> ListBuilderContext[ServerStorageVersion.Builder]: ...

        def storage_versions(self, value_or_callback=None, /):
            """
            The reported versions per API server instance.
            """
            if self._in_context and value_or_callback is None:
                context = ListBuilderContext[ServerStorageVersion.Builder]()
                context._parent_builder = self
                context._field_name = "storage_versions"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(ServerStorageVersion.list_builder())
                if isinstance(output, GenericListBuilder):
                    value = output.build()
                else:
                    value = output
            return self._set("storage_versions", value)

    class BuilderContext(BuilderContextBase["StorageVersionStatus.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = StorageVersionStatus.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for StorageVersionStatus."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["StorageVersionStatus", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use StorageVersionStatus.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    common_encoding_version: Annotated[Optional[str], Field(alias="commonEncodingVersion")] = None
    """
    If all API server instances agree on the same encoding storage version, then this field is set to that version. Otherwise this field is left empty. API servers should finish updating its storageVersionStatus entry before serving write operations, so that this field will be in sync with the reality.
    """
    conditions: Optional[List[StorageVersionCondition]] = None
    """
    The latest available observations of the storageVersion's state.
    """
    storage_versions: Annotated[
        Optional[List[ServerStorageVersion]], Field(alias="storageVersions")
    ] = None
    """
    The reported versions per API server instance.
    """


class StorageVersion(Resource):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["StorageVersion"]:
            return StorageVersion

        def build(self) -> "StorageVersion":
            return StorageVersion(**self._attrs)

        def api_version(
            self, value: Optional[Literal["internal.apiserver.k8s.io/v1alpha1"]], /
        ) -> Self:
            """
            APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
            """
            return self._set("api_version", value)

        def kind(self, value: Optional[Literal["StorageVersion"]], /) -> Self:
            """
            Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
            """
            return self._set("kind", value)

        @overload
        def metadata(
            self, value_or_callback: Optional[apimachinery.ObjectMeta], /
        ) -> "StorageVersion.Builder": ...

        @overload
        def metadata(
            self,
            value_or_callback: Callable[
                [apimachinery.ObjectMeta.Builder],
                apimachinery.ObjectMeta.Builder | apimachinery.ObjectMeta,
            ],
            /,
        ) -> "StorageVersion.Builder": ...

        @overload
        def metadata(
            self, value_or_callback: Never = ...
        ) -> "apimachinery.ObjectMeta.BuilderContext": ...

        def metadata(self, value_or_callback=None, /):
            """
            The name is <group>.<resource>.
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
        def spec(self, value_or_callback: StorageVersionSpec, /) -> "StorageVersion.Builder": ...

        @overload
        def spec(
            self,
            value_or_callback: Callable[
                [StorageVersionSpec.Builder],
                StorageVersionSpec.Builder | StorageVersionSpec,
            ],
            /,
        ) -> "StorageVersion.Builder": ...

        @overload
        def spec(self, value_or_callback: Never = ...) -> "StorageVersionSpec.BuilderContext": ...

        def spec(self, value_or_callback=None, /):
            """
            Spec is an empty spec. It is here to comply with Kubernetes API style.
            """
            if self._in_context and value_or_callback is None:
                context = StorageVersionSpec.BuilderContext()
                context._parent_builder = self
                context._field_name = "spec"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(StorageVersionSpec.builder())
                if isinstance(output, StorageVersionSpec.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("spec", value)

        @overload
        def status(
            self, value_or_callback: StorageVersionStatus, /
        ) -> "StorageVersion.Builder": ...

        @overload
        def status(
            self,
            value_or_callback: Callable[
                [StorageVersionStatus.Builder],
                StorageVersionStatus.Builder | StorageVersionStatus,
            ],
            /,
        ) -> "StorageVersion.Builder": ...

        @overload
        def status(
            self, value_or_callback: Never = ...
        ) -> "StorageVersionStatus.BuilderContext": ...

        def status(self, value_or_callback=None, /):
            """
            API server instances report the version they can decode and the version they encode objects to when persisting objects in the backend.
            """
            if self._in_context and value_or_callback is None:
                context = StorageVersionStatus.BuilderContext()
                context._parent_builder = self
                context._field_name = "status"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(StorageVersionStatus.builder())
                if isinstance(output, StorageVersionStatus.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("status", value)

    class BuilderContext(BuilderContextBase["StorageVersion.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = StorageVersion.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for StorageVersion."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["StorageVersion", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use StorageVersion.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    api_version: Annotated[
        Optional[Literal["internal.apiserver.k8s.io/v1alpha1"]],
        Field(alias="apiVersion"),
    ] = "internal.apiserver.k8s.io/v1alpha1"
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: Optional[Literal["StorageVersion"]] = "StorageVersion"
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: Optional[apimachinery.ObjectMeta] = None
    """
    The name is <group>.<resource>.
    """
    spec: StorageVersionSpec
    """
    Spec is an empty spec. It is here to comply with Kubernetes API style.
    """
    status: StorageVersionStatus
    """
    API server instances report the version they can decode and the version they encode objects to when persisting objects in the backend.
    """


StorageVersionList = ResourceList["StorageVersion"]
