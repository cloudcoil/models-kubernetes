# Generated by cloudcoil-model-codegen v0.4.3
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


class GroupVersionResource(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["GroupVersionResource"]:
            return GroupVersionResource

        def build(self) -> "GroupVersionResource":
            return GroupVersionResource(**self._attrs)

        def group(self, value: Optional[str], /) -> Self:
            """
            The name of the group.
            """
            return self._set("group", value)

        def resource(self, value: Optional[str], /) -> Self:
            """
            The name of the resource.
            """
            return self._set("resource", value)

        def version(self, value: Optional[str], /) -> Self:
            """
            The name of the version.
            """
            return self._set("version", value)

    class BuilderContext(BuilderContextBase["GroupVersionResource.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = GroupVersionResource.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for GroupVersionResource."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["GroupVersionResource", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use GroupVersionResource.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    group: Optional[str] = None
    """
    The name of the group.
    """
    resource: Optional[str] = None
    """
    The name of the resource.
    """
    version: Optional[str] = None
    """
    The name of the version.
    """


class StorageVersionMigrationSpec(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["StorageVersionMigrationSpec"]:
            return StorageVersionMigrationSpec

        def build(self) -> "StorageVersionMigrationSpec":
            return StorageVersionMigrationSpec(**self._attrs)

        def continue_token(self, value: Optional[str], /) -> Self:
            """
            The token used in the list options to get the next chunk of objects to migrate. When the .status.conditions indicates the migration is "Running", users can use this token to check the progress of the migration.
            """
            return self._set("continue_token", value)

        @overload
        def resource(
            self, value_or_callback: GroupVersionResource, /
        ) -> "StorageVersionMigrationSpec.Builder": ...

        @overload
        def resource(
            self,
            value_or_callback: Callable[
                [GroupVersionResource.Builder],
                GroupVersionResource.Builder | GroupVersionResource,
            ],
            /,
        ) -> "StorageVersionMigrationSpec.Builder": ...

        @overload
        def resource(
            self, value_or_callback: Never = ...
        ) -> "GroupVersionResource.BuilderContext": ...

        def resource(self, value_or_callback=None, /):
            """
            The resource that is being migrated. The migrator sends requests to the endpoint serving the resource. Immutable.
            """
            if self._in_context and value_or_callback is None:
                context = GroupVersionResource.BuilderContext()
                context._parent_builder = self
                context._field_name = "resource"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(GroupVersionResource.builder())
                if isinstance(output, GroupVersionResource.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("resource", value)

    class BuilderContext(BuilderContextBase["StorageVersionMigrationSpec.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = StorageVersionMigrationSpec.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for StorageVersionMigrationSpec."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["StorageVersionMigrationSpec", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use StorageVersionMigrationSpec.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    continue_token: Annotated[Optional[str], Field(alias="continueToken")] = None
    """
    The token used in the list options to get the next chunk of objects to migrate. When the .status.conditions indicates the migration is "Running", users can use this token to check the progress of the migration.
    """
    resource: GroupVersionResource
    """
    The resource that is being migrated. The migrator sends requests to the endpoint serving the resource. Immutable.
    """


class MigrationCondition(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["MigrationCondition"]:
            return MigrationCondition

        def build(self) -> "MigrationCondition":
            return MigrationCondition(**self._attrs)

        @overload
        def last_update_time(
            self, value_or_callback: Optional[apimachinery.Time], /
        ) -> "MigrationCondition.Builder": ...

        @overload
        def last_update_time(
            self,
            value_or_callback: Callable[
                [apimachinery.Time.Builder],
                apimachinery.Time.Builder | apimachinery.Time,
            ],
            /,
        ) -> "MigrationCondition.Builder": ...

        @overload
        def last_update_time(
            self, value_or_callback: Never = ...
        ) -> "apimachinery.Time.BuilderContext": ...

        def last_update_time(self, value_or_callback=None, /):
            """
            The last time this condition was updated.
            """
            if self._in_context and value_or_callback is None:
                context = apimachinery.Time.BuilderContext()
                context._parent_builder = self
                context._field_name = "last_update_time"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(apimachinery.Time.builder())
                if isinstance(output, apimachinery.Time.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("last_update_time", value)

        def message(self, value: Optional[str], /) -> Self:
            """
            A human readable message indicating details about the transition.
            """
            return self._set("message", value)

        def reason(self, value: Optional[str], /) -> Self:
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

    class BuilderContext(BuilderContextBase["MigrationCondition.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = MigrationCondition.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for MigrationCondition."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["MigrationCondition", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use MigrationCondition.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    last_update_time: Annotated[Optional[apimachinery.Time], Field(alias="lastUpdateTime")] = None
    """
    The last time this condition was updated.
    """
    message: Optional[str] = None
    """
    A human readable message indicating details about the transition.
    """
    reason: Optional[str] = None
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


class StorageVersionMigrationStatus(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["StorageVersionMigrationStatus"]:
            return StorageVersionMigrationStatus

        def build(self) -> "StorageVersionMigrationStatus":
            return StorageVersionMigrationStatus(**self._attrs)

        @overload
        def conditions(
            self, value_or_callback: List[MigrationCondition], /
        ) -> "StorageVersionMigrationStatus.Builder": ...

        @overload
        def conditions(
            self,
            value_or_callback: Callable[
                [GenericListBuilder[MigrationCondition, MigrationCondition.Builder]],
                GenericListBuilder[MigrationCondition, MigrationCondition.Builder]
                | List[MigrationCondition],
            ],
            /,
        ) -> "StorageVersionMigrationStatus.Builder": ...

        @overload
        def conditions(
            self, value_or_callback: Never = ...
        ) -> ListBuilderContext[MigrationCondition.Builder]: ...

        def conditions(self, value_or_callback=None, /):
            """
            The latest available observations of the migration's current state.
            """
            if self._in_context and value_or_callback is None:
                context = ListBuilderContext[MigrationCondition.Builder]()
                context._parent_builder = self
                context._field_name = "conditions"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(MigrationCondition.list_builder())
                if isinstance(output, GenericListBuilder):
                    value = output.build()
                else:
                    value = output
            return self._set("conditions", value)

        def resource_version(self, value: Optional[str], /) -> Self:
            """
            ResourceVersion to compare with the GC cache for performing the migration. This is the current resource version of given group, version and resource when kube-controller-manager first observes this StorageVersionMigration resource.
            """
            return self._set("resource_version", value)

    class BuilderContext(BuilderContextBase["StorageVersionMigrationStatus.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = StorageVersionMigrationStatus.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for StorageVersionMigrationStatus."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["StorageVersionMigrationStatus", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use StorageVersionMigrationStatus.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    conditions: Optional[List[MigrationCondition]] = None
    """
    The latest available observations of the migration's current state.
    """
    resource_version: Annotated[Optional[str], Field(alias="resourceVersion")] = None
    """
    ResourceVersion to compare with the GC cache for performing the migration. This is the current resource version of given group, version and resource when kube-controller-manager first observes this StorageVersionMigration resource.
    """


class StorageVersionMigration(Resource):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["StorageVersionMigration"]:
            return StorageVersionMigration

        def build(self) -> "StorageVersionMigration":
            return StorageVersionMigration(**self._attrs)

        def api_version(
            self, value: Optional[Literal["storagemigration.k8s.io/v1alpha1"]], /
        ) -> Self:
            """
            APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
            """
            return self._set("api_version", value)

        def kind(self, value: Optional[Literal["StorageVersionMigration"]], /) -> Self:
            """
            Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
            """
            return self._set("kind", value)

        @overload
        def metadata(
            self, value_or_callback: Optional[apimachinery.ObjectMeta], /
        ) -> "StorageVersionMigration.Builder": ...

        @overload
        def metadata(
            self,
            value_or_callback: Callable[
                [apimachinery.ObjectMeta.Builder],
                apimachinery.ObjectMeta.Builder | apimachinery.ObjectMeta,
            ],
            /,
        ) -> "StorageVersionMigration.Builder": ...

        @overload
        def metadata(
            self, value_or_callback: Never = ...
        ) -> "apimachinery.ObjectMeta.BuilderContext": ...

        def metadata(self, value_or_callback=None, /):
            """
            Standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
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
            self, value_or_callback: Optional[StorageVersionMigrationSpec], /
        ) -> "StorageVersionMigration.Builder": ...

        @overload
        def spec(
            self,
            value_or_callback: Callable[
                [StorageVersionMigrationSpec.Builder],
                StorageVersionMigrationSpec.Builder | StorageVersionMigrationSpec,
            ],
            /,
        ) -> "StorageVersionMigration.Builder": ...

        @overload
        def spec(
            self, value_or_callback: Never = ...
        ) -> "StorageVersionMigrationSpec.BuilderContext": ...

        def spec(self, value_or_callback=None, /):
            """
            Specification of the migration.
            """
            if self._in_context and value_or_callback is None:
                context = StorageVersionMigrationSpec.BuilderContext()
                context._parent_builder = self
                context._field_name = "spec"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(StorageVersionMigrationSpec.builder())
                if isinstance(output, StorageVersionMigrationSpec.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("spec", value)

        @overload
        def status(
            self, value_or_callback: Optional[StorageVersionMigrationStatus], /
        ) -> "StorageVersionMigration.Builder": ...

        @overload
        def status(
            self,
            value_or_callback: Callable[
                [StorageVersionMigrationStatus.Builder],
                StorageVersionMigrationStatus.Builder | StorageVersionMigrationStatus,
            ],
            /,
        ) -> "StorageVersionMigration.Builder": ...

        @overload
        def status(
            self, value_or_callback: Never = ...
        ) -> "StorageVersionMigrationStatus.BuilderContext": ...

        def status(self, value_or_callback=None, /):
            """
            Status of the migration.
            """
            if self._in_context and value_or_callback is None:
                context = StorageVersionMigrationStatus.BuilderContext()
                context._parent_builder = self
                context._field_name = "status"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(StorageVersionMigrationStatus.builder())
                if isinstance(output, StorageVersionMigrationStatus.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("status", value)

    class BuilderContext(BuilderContextBase["StorageVersionMigration.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = StorageVersionMigration.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for StorageVersionMigration."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["StorageVersionMigration", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use StorageVersionMigration.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    api_version: Annotated[
        Optional[Literal["storagemigration.k8s.io/v1alpha1"]], Field(alias="apiVersion")
    ] = "storagemigration.k8s.io/v1alpha1"
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: Optional[Literal["StorageVersionMigration"]] = "StorageVersionMigration"
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: Optional[apimachinery.ObjectMeta] = None
    """
    Standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    spec: Optional[StorageVersionMigrationSpec] = None
    """
    Specification of the migration.
    """
    status: Optional[StorageVersionMigrationStatus] = None
    """
    Status of the migration.
    """


StorageVersionMigrationList = ResourceList["StorageVersionMigration"]
