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
    BaseModelBuilder,
    BuilderContextBase,
    GenericListBuilder,
    Never,
    Self,
)
from cloudcoil.resources import Resource, ResourceList


class PriorityClass(Resource):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["PriorityClass"]:
            return PriorityClass

        def build(self) -> "PriorityClass":
            return PriorityClass(**self._attrs)

        def api_version(self, value: Optional[Literal["scheduling.k8s.io/v1"]], /) -> Self:
            """
            APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
            """
            return self._set("api_version", value)

        def description(self, value: Optional[str], /) -> Self:
            """
            description is an arbitrary string that usually provides guidelines on when this priority class should be used.
            """
            return self._set("description", value)

        def global_default(self, value: Optional[bool], /) -> Self:
            """
            globalDefault specifies whether this PriorityClass should be considered as the default priority for pods that do not have any priority class. Only one PriorityClass can be marked as `globalDefault`. However, if more than one PriorityClasses exists with their `globalDefault` field set to true, the smallest value of such global default PriorityClasses will be used as the default priority.
            """
            return self._set("global_default", value)

        def kind(self, value: Optional[Literal["PriorityClass"]], /) -> Self:
            """
            Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
            """
            return self._set("kind", value)

        @overload
        def metadata(
            self, value_or_callback: Optional[apimachinery.ObjectMeta], /
        ) -> "PriorityClass.Builder": ...

        @overload
        def metadata(
            self,
            value_or_callback: Callable[
                [apimachinery.ObjectMeta.Builder],
                apimachinery.ObjectMeta.Builder | apimachinery.ObjectMeta,
            ],
            /,
        ) -> "PriorityClass.Builder": ...

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

        def preemption_policy(self, value: Optional[str], /) -> Self:
            """
            preemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset.
            """
            return self._set("preemption_policy", value)

        def value(self, value: int, /) -> Self:
            """
            value represents the integer value of this priority class. This is the actual priority that pods receive when they have the name of this class in their pod spec.
            """
            return self._set("value", value)

    class BuilderContext(BuilderContextBase["PriorityClass.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = PriorityClass.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for PriorityClass."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["PriorityClass", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use PriorityClass.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    api_version: Annotated[Optional[Literal["scheduling.k8s.io/v1"]], Field(alias="apiVersion")] = (
        "scheduling.k8s.io/v1"
    )
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    description: Optional[str] = None
    """
    description is an arbitrary string that usually provides guidelines on when this priority class should be used.
    """
    global_default: Annotated[Optional[bool], Field(alias="globalDefault")] = None
    """
    globalDefault specifies whether this PriorityClass should be considered as the default priority for pods that do not have any priority class. Only one PriorityClass can be marked as `globalDefault`. However, if more than one PriorityClasses exists with their `globalDefault` field set to true, the smallest value of such global default PriorityClasses will be used as the default priority.
    """
    kind: Optional[Literal["PriorityClass"]] = "PriorityClass"
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: Optional[apimachinery.ObjectMeta] = None
    """
    Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    preemption_policy: Annotated[Optional[str], Field(alias="preemptionPolicy")] = None
    """
    preemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset.
    """
    value: int
    """
    value represents the integer value of this priority class. This is the actual priority that pods receive when they have the name of this class in their pod spec.
    """


PriorityClassList = ResourceList["PriorityClass"]
