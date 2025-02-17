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


class CrossVersionObjectReference(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["CrossVersionObjectReference"]:
            return CrossVersionObjectReference

        def build(self) -> "CrossVersionObjectReference":
            return CrossVersionObjectReference(**self._attrs)

        def api_version(self, value: Optional[str], /) -> Self:
            """
            apiVersion is the API version of the referent
            """
            return self._set("api_version", value)

        def kind(self, value: str, /) -> Self:
            """
            kind is the kind of the referent; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
            """
            return self._set("kind", value)

        def name(self, value: str, /) -> Self:
            """
            name is the name of the referent; More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
            """
            return self._set("name", value)

    class BuilderContext(BuilderContextBase["CrossVersionObjectReference.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = CrossVersionObjectReference.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for CrossVersionObjectReference."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["CrossVersionObjectReference", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use CrossVersionObjectReference.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    api_version: Annotated[Optional[str], Field(alias="apiVersion")] = None
    """
    apiVersion is the API version of the referent
    """
    kind: str
    """
    kind is the kind of the referent; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    name: str
    """
    name is the name of the referent; More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names
    """


class HorizontalPodAutoscalerSpec(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["HorizontalPodAutoscalerSpec"]:
            return HorizontalPodAutoscalerSpec

        def build(self) -> "HorizontalPodAutoscalerSpec":
            return HorizontalPodAutoscalerSpec(**self._attrs)

        def max_replicas(self, value: int, /) -> Self:
            """
            maxReplicas is the upper limit for the number of pods that can be set by the autoscaler; cannot be smaller than MinReplicas.
            """
            return self._set("max_replicas", value)

        def min_replicas(self, value: Optional[int], /) -> Self:
            """
            minReplicas is the lower limit for the number of replicas to which the autoscaler can scale down.  It defaults to 1 pod.  minReplicas is allowed to be 0 if the alpha feature gate HPAScaleToZero is enabled and at least one Object or External metric is configured.  Scaling is active as long as at least one metric value is available.
            """
            return self._set("min_replicas", value)

        @overload
        def scale_target_ref(
            self, value_or_callback: CrossVersionObjectReference, /
        ) -> "HorizontalPodAutoscalerSpec.Builder": ...

        @overload
        def scale_target_ref(
            self,
            value_or_callback: Callable[
                [CrossVersionObjectReference.Builder],
                CrossVersionObjectReference.Builder | CrossVersionObjectReference,
            ],
            /,
        ) -> "HorizontalPodAutoscalerSpec.Builder": ...

        @overload
        def scale_target_ref(
            self, value_or_callback: Never = ...
        ) -> "CrossVersionObjectReference.BuilderContext": ...

        def scale_target_ref(self, value_or_callback=None, /):
            """
            reference to scaled resource; horizontal pod autoscaler will learn the current resource consumption and will set the desired number of pods by using its Scale subresource.
            """
            if self._in_context and value_or_callback is None:
                context = CrossVersionObjectReference.BuilderContext()
                context._parent_builder = self
                context._field_name = "scale_target_ref"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(CrossVersionObjectReference.builder())
                if isinstance(output, CrossVersionObjectReference.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("scale_target_ref", value)

        def target_cpu_utilization_percentage(self, value: Optional[int], /) -> Self:
            """
            targetCPUUtilizationPercentage is the target average CPU utilization (represented as a percentage of requested CPU) over all the pods; if not specified the default autoscaling policy will be used.
            """
            return self._set("target_cpu_utilization_percentage", value)

    class BuilderContext(BuilderContextBase["HorizontalPodAutoscalerSpec.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = HorizontalPodAutoscalerSpec.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for HorizontalPodAutoscalerSpec."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["HorizontalPodAutoscalerSpec", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use HorizontalPodAutoscalerSpec.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    max_replicas: Annotated[int, Field(alias="maxReplicas")]
    """
    maxReplicas is the upper limit for the number of pods that can be set by the autoscaler; cannot be smaller than MinReplicas.
    """
    min_replicas: Annotated[Optional[int], Field(alias="minReplicas")] = None
    """
    minReplicas is the lower limit for the number of replicas to which the autoscaler can scale down.  It defaults to 1 pod.  minReplicas is allowed to be 0 if the alpha feature gate HPAScaleToZero is enabled and at least one Object or External metric is configured.  Scaling is active as long as at least one metric value is available.
    """
    scale_target_ref: Annotated[CrossVersionObjectReference, Field(alias="scaleTargetRef")]
    """
    reference to scaled resource; horizontal pod autoscaler will learn the current resource consumption and will set the desired number of pods by using its Scale subresource.
    """
    target_cpu_utilization_percentage: Annotated[
        Optional[int], Field(alias="targetCPUUtilizationPercentage")
    ] = None
    """
    targetCPUUtilizationPercentage is the target average CPU utilization (represented as a percentage of requested CPU) over all the pods; if not specified the default autoscaling policy will be used.
    """


class ScaleSpec(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["ScaleSpec"]:
            return ScaleSpec

        def build(self) -> "ScaleSpec":
            return ScaleSpec(**self._attrs)

        def replicas(self, value: Optional[int], /) -> Self:
            """
            replicas is the desired number of instances for the scaled object.
            """
            return self._set("replicas", value)

    class BuilderContext(BuilderContextBase["ScaleSpec.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = ScaleSpec.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for ScaleSpec."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["ScaleSpec", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use ScaleSpec.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    replicas: Optional[int] = None
    """
    replicas is the desired number of instances for the scaled object.
    """


class ScaleStatus(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["ScaleStatus"]:
            return ScaleStatus

        def build(self) -> "ScaleStatus":
            return ScaleStatus(**self._attrs)

        def replicas(self, value: int, /) -> Self:
            """
            replicas is the actual number of observed instances of the scaled object.
            """
            return self._set("replicas", value)

        def selector(self, value: Optional[str], /) -> Self:
            """
            selector is the label query over pods that should match the replicas count. This is same as the label selector but in the string format to avoid introspection by clients. The string will be in the same format as the query-param syntax. More info about label selectors: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
            """
            return self._set("selector", value)

    class BuilderContext(BuilderContextBase["ScaleStatus.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = ScaleStatus.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for ScaleStatus."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["ScaleStatus", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use ScaleStatus.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    replicas: int
    """
    replicas is the actual number of observed instances of the scaled object.
    """
    selector: Optional[str] = None
    """
    selector is the label query over pods that should match the replicas count. This is same as the label selector but in the string format to avoid introspection by clients. The string will be in the same format as the query-param syntax. More info about label selectors: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
    """


class HorizontalPodAutoscalerStatus(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["HorizontalPodAutoscalerStatus"]:
            return HorizontalPodAutoscalerStatus

        def build(self) -> "HorizontalPodAutoscalerStatus":
            return HorizontalPodAutoscalerStatus(**self._attrs)

        def current_cpu_utilization_percentage(self, value: Optional[int], /) -> Self:
            """
            currentCPUUtilizationPercentage is the current average CPU utilization over all pods, represented as a percentage of requested CPU, e.g. 70 means that an average pod is using now 70% of its requested CPU.
            """
            return self._set("current_cpu_utilization_percentage", value)

        def current_replicas(self, value: int, /) -> Self:
            """
            currentReplicas is the current number of replicas of pods managed by this autoscaler.
            """
            return self._set("current_replicas", value)

        def desired_replicas(self, value: int, /) -> Self:
            """
            desiredReplicas is the  desired number of replicas of pods managed by this autoscaler.
            """
            return self._set("desired_replicas", value)

        @overload
        def last_scale_time(
            self, value_or_callback: Optional[apimachinery.Time], /
        ) -> "HorizontalPodAutoscalerStatus.Builder": ...

        @overload
        def last_scale_time(
            self,
            value_or_callback: Callable[
                [apimachinery.Time.Builder],
                apimachinery.Time.Builder | apimachinery.Time,
            ],
            /,
        ) -> "HorizontalPodAutoscalerStatus.Builder": ...

        @overload
        def last_scale_time(
            self, value_or_callback: Never = ...
        ) -> "apimachinery.Time.BuilderContext": ...

        def last_scale_time(self, value_or_callback=None, /):
            """
            lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods; used by the autoscaler to control how often the number of pods is changed.
            """
            if self._in_context and value_or_callback is None:
                context = apimachinery.Time.BuilderContext()
                context._parent_builder = self
                context._field_name = "last_scale_time"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(apimachinery.Time.builder())
                if isinstance(output, apimachinery.Time.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("last_scale_time", value)

        def observed_generation(self, value: Optional[int], /) -> Self:
            """
            observedGeneration is the most recent generation observed by this autoscaler.
            """
            return self._set("observed_generation", value)

    class BuilderContext(BuilderContextBase["HorizontalPodAutoscalerStatus.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = HorizontalPodAutoscalerStatus.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for HorizontalPodAutoscalerStatus."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["HorizontalPodAutoscalerStatus", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use HorizontalPodAutoscalerStatus.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    current_cpu_utilization_percentage: Annotated[
        Optional[int], Field(alias="currentCPUUtilizationPercentage")
    ] = None
    """
    currentCPUUtilizationPercentage is the current average CPU utilization over all pods, represented as a percentage of requested CPU, e.g. 70 means that an average pod is using now 70% of its requested CPU.
    """
    current_replicas: Annotated[int, Field(alias="currentReplicas")]
    """
    currentReplicas is the current number of replicas of pods managed by this autoscaler.
    """
    desired_replicas: Annotated[int, Field(alias="desiredReplicas")]
    """
    desiredReplicas is the  desired number of replicas of pods managed by this autoscaler.
    """
    last_scale_time: Annotated[Optional[apimachinery.Time], Field(alias="lastScaleTime")] = None
    """
    lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods; used by the autoscaler to control how often the number of pods is changed.
    """
    observed_generation: Annotated[Optional[int], Field(alias="observedGeneration")] = None
    """
    observedGeneration is the most recent generation observed by this autoscaler.
    """


class HorizontalPodAutoscaler(Resource):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["HorizontalPodAutoscaler"]:
            return HorizontalPodAutoscaler

        def build(self) -> "HorizontalPodAutoscaler":
            return HorizontalPodAutoscaler(**self._attrs)

        def api_version(self, value: Optional[Literal["autoscaling/v1"]], /) -> Self:
            """
            APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
            """
            return self._set("api_version", value)

        def kind(self, value: Optional[Literal["HorizontalPodAutoscaler"]], /) -> Self:
            """
            Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
            """
            return self._set("kind", value)

        @overload
        def metadata(
            self, value_or_callback: Optional[apimachinery.ObjectMeta], /
        ) -> "HorizontalPodAutoscaler.Builder": ...

        @overload
        def metadata(
            self,
            value_or_callback: Callable[
                [apimachinery.ObjectMeta.Builder],
                apimachinery.ObjectMeta.Builder | apimachinery.ObjectMeta,
            ],
            /,
        ) -> "HorizontalPodAutoscaler.Builder": ...

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
            self, value_or_callback: Optional[HorizontalPodAutoscalerSpec], /
        ) -> "HorizontalPodAutoscaler.Builder": ...

        @overload
        def spec(
            self,
            value_or_callback: Callable[
                [HorizontalPodAutoscalerSpec.Builder],
                HorizontalPodAutoscalerSpec.Builder | HorizontalPodAutoscalerSpec,
            ],
            /,
        ) -> "HorizontalPodAutoscaler.Builder": ...

        @overload
        def spec(
            self, value_or_callback: Never = ...
        ) -> "HorizontalPodAutoscalerSpec.BuilderContext": ...

        def spec(self, value_or_callback=None, /):
            """
            spec defines the behaviour of autoscaler. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status.
            """
            if self._in_context and value_or_callback is None:
                context = HorizontalPodAutoscalerSpec.BuilderContext()
                context._parent_builder = self
                context._field_name = "spec"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(HorizontalPodAutoscalerSpec.builder())
                if isinstance(output, HorizontalPodAutoscalerSpec.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("spec", value)

        @overload
        def status(
            self, value_or_callback: Optional[HorizontalPodAutoscalerStatus], /
        ) -> "HorizontalPodAutoscaler.Builder": ...

        @overload
        def status(
            self,
            value_or_callback: Callable[
                [HorizontalPodAutoscalerStatus.Builder],
                HorizontalPodAutoscalerStatus.Builder | HorizontalPodAutoscalerStatus,
            ],
            /,
        ) -> "HorizontalPodAutoscaler.Builder": ...

        @overload
        def status(
            self, value_or_callback: Never = ...
        ) -> "HorizontalPodAutoscalerStatus.BuilderContext": ...

        def status(self, value_or_callback=None, /):
            """
            status is the current information about the autoscaler.
            """
            if self._in_context and value_or_callback is None:
                context = HorizontalPodAutoscalerStatus.BuilderContext()
                context._parent_builder = self
                context._field_name = "status"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(HorizontalPodAutoscalerStatus.builder())
                if isinstance(output, HorizontalPodAutoscalerStatus.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("status", value)

    class BuilderContext(BuilderContextBase["HorizontalPodAutoscaler.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = HorizontalPodAutoscaler.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for HorizontalPodAutoscaler."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["HorizontalPodAutoscaler", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use HorizontalPodAutoscaler.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    api_version: Annotated[Optional[Literal["autoscaling/v1"]], Field(alias="apiVersion")] = (
        "autoscaling/v1"
    )
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: Optional[Literal["HorizontalPodAutoscaler"]] = "HorizontalPodAutoscaler"
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: Optional[apimachinery.ObjectMeta] = None
    """
    Standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    spec: Optional[HorizontalPodAutoscalerSpec] = None
    """
    spec defines the behaviour of autoscaler. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status.
    """
    status: Optional[HorizontalPodAutoscalerStatus] = None
    """
    status is the current information about the autoscaler.
    """


HorizontalPodAutoscalerList = ResourceList["HorizontalPodAutoscaler"]


class Scale(Resource):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["Scale"]:
            return Scale

        def build(self) -> "Scale":
            return Scale(**self._attrs)

        def api_version(self, value: Optional[Literal["autoscaling/v1"]], /) -> Self:
            """
            APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
            """
            return self._set("api_version", value)

        def kind(self, value: Optional[Literal["Scale"]], /) -> Self:
            """
            Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
            """
            return self._set("kind", value)

        @overload
        def metadata(
            self, value_or_callback: Optional[apimachinery.ObjectMeta], /
        ) -> "Scale.Builder": ...

        @overload
        def metadata(
            self,
            value_or_callback: Callable[
                [apimachinery.ObjectMeta.Builder],
                apimachinery.ObjectMeta.Builder | apimachinery.ObjectMeta,
            ],
            /,
        ) -> "Scale.Builder": ...

        @overload
        def metadata(
            self, value_or_callback: Never = ...
        ) -> "apimachinery.ObjectMeta.BuilderContext": ...

        def metadata(self, value_or_callback=None, /):
            """
            Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata.
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
        def spec(self, value_or_callback: Optional[ScaleSpec], /) -> "Scale.Builder": ...

        @overload
        def spec(
            self,
            value_or_callback: Callable[[ScaleSpec.Builder], ScaleSpec.Builder | ScaleSpec],
            /,
        ) -> "Scale.Builder": ...

        @overload
        def spec(self, value_or_callback: Never = ...) -> "ScaleSpec.BuilderContext": ...

        def spec(self, value_or_callback=None, /):
            """
            spec defines the behavior of the scale. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status.
            """
            if self._in_context and value_or_callback is None:
                context = ScaleSpec.BuilderContext()
                context._parent_builder = self
                context._field_name = "spec"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(ScaleSpec.builder())
                if isinstance(output, ScaleSpec.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("spec", value)

        @overload
        def status(self, value_or_callback: Optional[ScaleStatus], /) -> "Scale.Builder": ...

        @overload
        def status(
            self,
            value_or_callback: Callable[[ScaleStatus.Builder], ScaleStatus.Builder | ScaleStatus],
            /,
        ) -> "Scale.Builder": ...

        @overload
        def status(self, value_or_callback: Never = ...) -> "ScaleStatus.BuilderContext": ...

        def status(self, value_or_callback=None, /):
            """
            status is the current status of the scale. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status. Read-only.
            """
            if self._in_context and value_or_callback is None:
                context = ScaleStatus.BuilderContext()
                context._parent_builder = self
                context._field_name = "status"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(ScaleStatus.builder())
                if isinstance(output, ScaleStatus.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("status", value)

    class BuilderContext(BuilderContextBase["Scale.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = Scale.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for Scale."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["Scale", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use Scale.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    api_version: Annotated[Optional[Literal["autoscaling/v1"]], Field(alias="apiVersion")] = (
        "autoscaling/v1"
    )
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: Optional[Literal["Scale"]] = "Scale"
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: Optional[apimachinery.ObjectMeta] = None
    """
    Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata.
    """
    spec: Optional[ScaleSpec] = None
    """
    spec defines the behavior of the scale. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status.
    """
    status: Optional[ScaleStatus] = None
    """
    status is the current status of the scale. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status. Read-only.
    """
