# Generated by cloudcoil-model-codegen v0.5.3
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


class Scheduling(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["Scheduling"]:
            return Scheduling

        def build(self) -> "Scheduling":
            return Scheduling(**self._attrs)

        def node_selector(self, value: Optional[Dict[str, str]], /) -> Self:
            """
            nodeSelector lists labels that must be present on nodes that support this RuntimeClass. Pods using this RuntimeClass can only be scheduled to a node matched by this selector. The RuntimeClass nodeSelector is merged with a pod's existing nodeSelector. Any conflicts will cause the pod to be rejected in admission.
            """
            return self._set("node_selector", value)

        @overload
        def tolerations(
            self, value_or_callback: List[v1.Toleration], /
        ) -> "Scheduling.Builder": ...

        @overload
        def tolerations(
            self,
            value_or_callback: Callable[
                [GenericListBuilder[v1.Toleration, v1.Toleration.Builder]],
                GenericListBuilder[v1.Toleration, v1.Toleration.Builder] | List[v1.Toleration],
            ],
            /,
        ) -> "Scheduling.Builder": ...

        @overload
        def tolerations(
            self, value_or_callback: Never = ...
        ) -> ListBuilderContext[v1.Toleration.Builder]: ...

        def tolerations(self, value_or_callback=None, /):
            """
            tolerations are appended (excluding duplicates) to pods running with this RuntimeClass during admission, effectively unioning the set of nodes tolerated by the pod and the RuntimeClass.
            """
            if self._in_context and value_or_callback is None:
                context = ListBuilderContext[v1.Toleration.Builder]()
                context._parent_builder = self
                context._field_name = "tolerations"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(v1.Toleration.list_builder())
                if isinstance(output, GenericListBuilder):
                    value = output.build()
                else:
                    value = output
            return self._set("tolerations", value)

    class BuilderContext(BuilderContextBase["Scheduling.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = Scheduling.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for Scheduling."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["Scheduling", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use Scheduling.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    node_selector: Annotated[Optional[Dict[str, str]], Field(alias="nodeSelector")] = None
    """
    nodeSelector lists labels that must be present on nodes that support this RuntimeClass. Pods using this RuntimeClass can only be scheduled to a node matched by this selector. The RuntimeClass nodeSelector is merged with a pod's existing nodeSelector. Any conflicts will cause the pod to be rejected in admission.
    """
    tolerations: Optional[List[v1.Toleration]] = None
    """
    tolerations are appended (excluding duplicates) to pods running with this RuntimeClass during admission, effectively unioning the set of nodes tolerated by the pod and the RuntimeClass.
    """


class Overhead(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["Overhead"]:
            return Overhead

        def build(self) -> "Overhead":
            return Overhead(**self._attrs)

        def pod_fixed(self, value: Optional[Dict[str, apimachinery.Quantity]], /) -> Self:
            """
            podFixed represents the fixed resource overhead associated with running a pod.
            """
            return self._set("pod_fixed", value)

    class BuilderContext(BuilderContextBase["Overhead.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = Overhead.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for Overhead."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["Overhead", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use Overhead.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    pod_fixed: Annotated[Optional[Dict[str, apimachinery.Quantity]], Field(alias="podFixed")] = None
    """
    podFixed represents the fixed resource overhead associated with running a pod.
    """


class RuntimeClass(Resource):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["RuntimeClass"]:
            return RuntimeClass

        def build(self) -> "RuntimeClass":
            return RuntimeClass(**self._attrs)

        def api_version(self, value: Optional[Literal["node.k8s.io/v1"]], /) -> Self:
            """
            APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
            """
            return self._set("api_version", value)

        def handler(self, value: str, /) -> Self:
            """
            handler specifies the underlying runtime and configuration that the CRI implementation will use to handle pods of this class. The possible values are specific to the node & CRI configuration.  It is assumed that all handlers are available on every node, and handlers of the same name are equivalent on every node. For example, a handler called "runc" might specify that the runc OCI runtime (using native Linux containers) will be used to run the containers in a pod. The Handler must be lowercase, conform to the DNS Label (RFC 1123) requirements, and is immutable.
            """
            return self._set("handler", value)

        def kind(self, value: Optional[Literal["RuntimeClass"]], /) -> Self:
            """
            Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
            """
            return self._set("kind", value)

        @overload
        def metadata(
            self, value_or_callback: Optional[apimachinery.ObjectMeta], /
        ) -> "RuntimeClass.Builder": ...

        @overload
        def metadata(
            self,
            value_or_callback: Callable[
                [apimachinery.ObjectMeta.Builder],
                apimachinery.ObjectMeta.Builder | apimachinery.ObjectMeta,
            ],
            /,
        ) -> "RuntimeClass.Builder": ...

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
        def overhead(self, value_or_callback: Optional[Overhead], /) -> "RuntimeClass.Builder": ...

        @overload
        def overhead(
            self,
            value_or_callback: Callable[[Overhead.Builder], Overhead.Builder | Overhead],
            /,
        ) -> "RuntimeClass.Builder": ...

        @overload
        def overhead(self, value_or_callback: Never = ...) -> "Overhead.BuilderContext": ...

        def overhead(self, value_or_callback=None, /):
            """
            overhead represents the resource overhead associated with running a pod for a given RuntimeClass. For more details, see
             https://kubernetes.io/docs/concepts/scheduling-eviction/pod-overhead/
            """
            if self._in_context and value_or_callback is None:
                context = Overhead.BuilderContext()
                context._parent_builder = self
                context._field_name = "overhead"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(Overhead.builder())
                if isinstance(output, Overhead.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("overhead", value)

        @overload
        def scheduling(
            self, value_or_callback: Optional[Scheduling], /
        ) -> "RuntimeClass.Builder": ...

        @overload
        def scheduling(
            self,
            value_or_callback: Callable[[Scheduling.Builder], Scheduling.Builder | Scheduling],
            /,
        ) -> "RuntimeClass.Builder": ...

        @overload
        def scheduling(self, value_or_callback: Never = ...) -> "Scheduling.BuilderContext": ...

        def scheduling(self, value_or_callback=None, /):
            """
            scheduling holds the scheduling constraints to ensure that pods running with this RuntimeClass are scheduled to nodes that support it. If scheduling is nil, this RuntimeClass is assumed to be supported by all nodes.
            """
            if self._in_context and value_or_callback is None:
                context = Scheduling.BuilderContext()
                context._parent_builder = self
                context._field_name = "scheduling"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(Scheduling.builder())
                if isinstance(output, Scheduling.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("scheduling", value)

    class BuilderContext(BuilderContextBase["RuntimeClass.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = RuntimeClass.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for RuntimeClass."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["RuntimeClass", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use RuntimeClass.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    api_version: Annotated[Optional[Literal["node.k8s.io/v1"]], Field(alias="apiVersion")] = (
        "node.k8s.io/v1"
    )
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    handler: str
    """
    handler specifies the underlying runtime and configuration that the CRI implementation will use to handle pods of this class. The possible values are specific to the node & CRI configuration.  It is assumed that all handlers are available on every node, and handlers of the same name are equivalent on every node. For example, a handler called "runc" might specify that the runc OCI runtime (using native Linux containers) will be used to run the containers in a pod. The Handler must be lowercase, conform to the DNS Label (RFC 1123) requirements, and is immutable.
    """
    kind: Optional[Literal["RuntimeClass"]] = "RuntimeClass"
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: Optional[apimachinery.ObjectMeta] = None
    """
    More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    overhead: Optional[Overhead] = None
    """
    overhead represents the resource overhead associated with running a pod for a given RuntimeClass. For more details, see
     https://kubernetes.io/docs/concepts/scheduling-eviction/pod-overhead/
    """
    scheduling: Optional[Scheduling] = None
    """
    scheduling holds the scheduling constraints to ensure that pods running with this RuntimeClass are scheduled to nodes that support it. If scheduling is nil, this RuntimeClass is assumed to be supported by all nodes.
    """


RuntimeClassList = ResourceList["RuntimeClass"]
