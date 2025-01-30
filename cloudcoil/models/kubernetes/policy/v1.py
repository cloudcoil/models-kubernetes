# Generated by cloudcoil-model-codegen v0.4.4
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


class Eviction(Resource):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["Eviction"]:
            return Eviction

        def build(self) -> "Eviction":
            return Eviction(**self._attrs)

        def api_version(self, value: Optional[Literal["policy/v1"]], /) -> Self:
            """
            APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
            """
            return self._set("api_version", value)

        @overload
        def delete_options(
            self, value_or_callback: Optional[apimachinery.DeleteOptions], /
        ) -> "Eviction.Builder": ...

        @overload
        def delete_options(
            self,
            value_or_callback: Callable[
                [apimachinery.DeleteOptions.Builder],
                apimachinery.DeleteOptions.Builder | apimachinery.DeleteOptions,
            ],
            /,
        ) -> "Eviction.Builder": ...

        @overload
        def delete_options(
            self, value_or_callback: Never = ...
        ) -> "apimachinery.DeleteOptions.BuilderContext": ...

        def delete_options(self, value_or_callback=None, /):
            """
            DeleteOptions may be provided
            """
            if self._in_context and value_or_callback is None:
                context = apimachinery.DeleteOptions.BuilderContext()
                context._parent_builder = self
                context._field_name = "delete_options"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(apimachinery.DeleteOptions.builder())
                if isinstance(output, apimachinery.DeleteOptions.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("delete_options", value)

        def kind(self, value: Optional[Literal["Eviction"]], /) -> Self:
            """
            Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
            """
            return self._set("kind", value)

        @overload
        def metadata(
            self, value_or_callback: Optional[apimachinery.ObjectMeta], /
        ) -> "Eviction.Builder": ...

        @overload
        def metadata(
            self,
            value_or_callback: Callable[
                [apimachinery.ObjectMeta.Builder],
                apimachinery.ObjectMeta.Builder | apimachinery.ObjectMeta,
            ],
            /,
        ) -> "Eviction.Builder": ...

        @overload
        def metadata(
            self, value_or_callback: Never = ...
        ) -> "apimachinery.ObjectMeta.BuilderContext": ...

        def metadata(self, value_or_callback=None, /):
            """
            ObjectMeta describes the pod that is being evicted.
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

    class BuilderContext(BuilderContextBase["Eviction.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = Eviction.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for Eviction."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["Eviction", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use Eviction.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    api_version: Annotated[Optional[Literal["policy/v1"]], Field(alias="apiVersion")] = "policy/v1"
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    delete_options: Annotated[
        Optional[apimachinery.DeleteOptions], Field(alias="deleteOptions")
    ] = None
    """
    DeleteOptions may be provided
    """
    kind: Optional[Literal["Eviction"]] = "Eviction"
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: Optional[apimachinery.ObjectMeta] = None
    """
    ObjectMeta describes the pod that is being evicted.
    """


class PodDisruptionBudgetSpec(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["PodDisruptionBudgetSpec"]:
            return PodDisruptionBudgetSpec

        def build(self) -> "PodDisruptionBudgetSpec":
            return PodDisruptionBudgetSpec(**self._attrs)

        @overload
        def max_unavailable(
            self, value_or_callback: Optional[apimachinery.IntOrString], /
        ) -> "PodDisruptionBudgetSpec.Builder": ...

        @overload
        def max_unavailable(
            self,
            value_or_callback: Callable[
                [apimachinery.IntOrString.Builder],
                apimachinery.IntOrString.Builder | apimachinery.IntOrString,
            ],
            /,
        ) -> "PodDisruptionBudgetSpec.Builder": ...

        @overload
        def max_unavailable(
            self, value_or_callback: Never = ...
        ) -> "apimachinery.IntOrString.BuilderContext": ...

        def max_unavailable(self, value_or_callback=None, /):
            """
            An eviction is allowed if at most "maxUnavailable" pods selected by "selector" are unavailable after the eviction, i.e. even in absence of the evicted pod. For example, one can prevent all voluntary evictions by specifying 0. This is a mutually exclusive setting with "minAvailable".
            """
            if self._in_context and value_or_callback is None:
                context = apimachinery.IntOrString.BuilderContext()
                context._parent_builder = self
                context._field_name = "max_unavailable"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(apimachinery.IntOrString.builder())
                if isinstance(output, apimachinery.IntOrString.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("max_unavailable", value)

        @overload
        def min_available(
            self, value_or_callback: Optional[apimachinery.IntOrString], /
        ) -> "PodDisruptionBudgetSpec.Builder": ...

        @overload
        def min_available(
            self,
            value_or_callback: Callable[
                [apimachinery.IntOrString.Builder],
                apimachinery.IntOrString.Builder | apimachinery.IntOrString,
            ],
            /,
        ) -> "PodDisruptionBudgetSpec.Builder": ...

        @overload
        def min_available(
            self, value_or_callback: Never = ...
        ) -> "apimachinery.IntOrString.BuilderContext": ...

        def min_available(self, value_or_callback=None, /):
            """
            An eviction is allowed if at least "minAvailable" pods selected by "selector" will still be available after the eviction, i.e. even in the absence of the evicted pod.  So for example you can prevent all voluntary evictions by specifying "100%".
            """
            if self._in_context and value_or_callback is None:
                context = apimachinery.IntOrString.BuilderContext()
                context._parent_builder = self
                context._field_name = "min_available"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(apimachinery.IntOrString.builder())
                if isinstance(output, apimachinery.IntOrString.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("min_available", value)

        @overload
        def selector(
            self, value_or_callback: Optional[apimachinery.LabelSelector], /
        ) -> "PodDisruptionBudgetSpec.Builder": ...

        @overload
        def selector(
            self,
            value_or_callback: Callable[
                [apimachinery.LabelSelector.Builder],
                apimachinery.LabelSelector.Builder | apimachinery.LabelSelector,
            ],
            /,
        ) -> "PodDisruptionBudgetSpec.Builder": ...

        @overload
        def selector(
            self, value_or_callback: Never = ...
        ) -> "apimachinery.LabelSelector.BuilderContext": ...

        def selector(self, value_or_callback=None, /):
            """
            Label query over pods whose evictions are managed by the disruption budget. A null selector will match no pods, while an empty ({}) selector will select all pods within the namespace.
            """
            if self._in_context and value_or_callback is None:
                context = apimachinery.LabelSelector.BuilderContext()
                context._parent_builder = self
                context._field_name = "selector"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(apimachinery.LabelSelector.builder())
                if isinstance(output, apimachinery.LabelSelector.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("selector", value)

        def unhealthy_pod_eviction_policy(self, value: Optional[str], /) -> Self:
            """
            UnhealthyPodEvictionPolicy defines the criteria for when unhealthy pods should be considered for eviction. Current implementation considers healthy pods, as pods that have status.conditions item with type="Ready",status="True".

            Valid policies are IfHealthyBudget and AlwaysAllow. If no policy is specified, the default behavior will be used, which corresponds to the IfHealthyBudget policy.

            IfHealthyBudget policy means that running pods (status.phase="Running"), but not yet healthy can be evicted only if the guarded application is not disrupted (status.currentHealthy is at least equal to status.desiredHealthy). Healthy pods will be subject to the PDB for eviction.

            AlwaysAllow policy means that all running pods (status.phase="Running"), but not yet healthy are considered disrupted and can be evicted regardless of whether the criteria in a PDB is met. This means perspective running pods of a disrupted application might not get a chance to become healthy. Healthy pods will be subject to the PDB for eviction.

            Additional policies may be added in the future. Clients making eviction decisions should disallow eviction of unhealthy pods if they encounter an unrecognized policy in this field.

            This field is beta-level. The eviction API uses this field when the feature gate PDBUnhealthyPodEvictionPolicy is enabled (enabled by default).
            """
            return self._set("unhealthy_pod_eviction_policy", value)

    class BuilderContext(BuilderContextBase["PodDisruptionBudgetSpec.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = PodDisruptionBudgetSpec.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for PodDisruptionBudgetSpec."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["PodDisruptionBudgetSpec", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use PodDisruptionBudgetSpec.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    max_unavailable: Annotated[
        Optional[apimachinery.IntOrString], Field(alias="maxUnavailable")
    ] = None
    """
    An eviction is allowed if at most "maxUnavailable" pods selected by "selector" are unavailable after the eviction, i.e. even in absence of the evicted pod. For example, one can prevent all voluntary evictions by specifying 0. This is a mutually exclusive setting with "minAvailable".
    """
    min_available: Annotated[Optional[apimachinery.IntOrString], Field(alias="minAvailable")] = None
    """
    An eviction is allowed if at least "minAvailable" pods selected by "selector" will still be available after the eviction, i.e. even in the absence of the evicted pod.  So for example you can prevent all voluntary evictions by specifying "100%".
    """
    selector: Optional[apimachinery.LabelSelector] = None
    """
    Label query over pods whose evictions are managed by the disruption budget. A null selector will match no pods, while an empty ({}) selector will select all pods within the namespace.
    """
    unhealthy_pod_eviction_policy: Annotated[
        Optional[str], Field(alias="unhealthyPodEvictionPolicy")
    ] = None
    """
    UnhealthyPodEvictionPolicy defines the criteria for when unhealthy pods should be considered for eviction. Current implementation considers healthy pods, as pods that have status.conditions item with type="Ready",status="True".

    Valid policies are IfHealthyBudget and AlwaysAllow. If no policy is specified, the default behavior will be used, which corresponds to the IfHealthyBudget policy.

    IfHealthyBudget policy means that running pods (status.phase="Running"), but not yet healthy can be evicted only if the guarded application is not disrupted (status.currentHealthy is at least equal to status.desiredHealthy). Healthy pods will be subject to the PDB for eviction.

    AlwaysAllow policy means that all running pods (status.phase="Running"), but not yet healthy are considered disrupted and can be evicted regardless of whether the criteria in a PDB is met. This means perspective running pods of a disrupted application might not get a chance to become healthy. Healthy pods will be subject to the PDB for eviction.

    Additional policies may be added in the future. Clients making eviction decisions should disallow eviction of unhealthy pods if they encounter an unrecognized policy in this field.

    This field is beta-level. The eviction API uses this field when the feature gate PDBUnhealthyPodEvictionPolicy is enabled (enabled by default).
    """


class PodDisruptionBudgetStatus(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["PodDisruptionBudgetStatus"]:
            return PodDisruptionBudgetStatus

        def build(self) -> "PodDisruptionBudgetStatus":
            return PodDisruptionBudgetStatus(**self._attrs)

        @overload
        def conditions(
            self, value_or_callback: List[apimachinery.Condition], /
        ) -> "PodDisruptionBudgetStatus.Builder": ...

        @overload
        def conditions(
            self,
            value_or_callback: Callable[
                [GenericListBuilder[apimachinery.Condition, apimachinery.Condition.Builder]],
                GenericListBuilder[apimachinery.Condition, apimachinery.Condition.Builder]
                | List[apimachinery.Condition],
            ],
            /,
        ) -> "PodDisruptionBudgetStatus.Builder": ...

        @overload
        def conditions(
            self, value_or_callback: Never = ...
        ) -> ListBuilderContext[apimachinery.Condition.Builder]: ...

        def conditions(self, value_or_callback=None, /):
            """
            Conditions contain conditions for PDB. The disruption controller sets the DisruptionAllowed condition. The following are known values for the reason field (additional reasons could be added in the future): - SyncFailed: The controller encountered an error and wasn't able to compute
                          the number of allowed disruptions. Therefore no disruptions are
                          allowed and the status of the condition will be False.
            - InsufficientPods: The number of pods are either at or below the number
                                required by the PodDisruptionBudget. No disruptions are
                                allowed and the status of the condition will be False.
            - SufficientPods: There are more pods than required by the PodDisruptionBudget.
                              The condition will be True, and the number of allowed
                              disruptions are provided by the disruptionsAllowed property.
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

        def current_healthy(self, value: int, /) -> Self:
            """
            current number of healthy pods
            """
            return self._set("current_healthy", value)

        def desired_healthy(self, value: int, /) -> Self:
            """
            minimum desired number of healthy pods
            """
            return self._set("desired_healthy", value)

        def disrupted_pods(self, value: Optional[Dict[str, apimachinery.Time]], /) -> Self:
            """
            DisruptedPods contains information about pods whose eviction was processed by the API server eviction subresource handler but has not yet been observed by the PodDisruptionBudget controller. A pod will be in this map from the time when the API server processed the eviction request to the time when the pod is seen by PDB controller as having been marked for deletion (or after a timeout). The key in the map is the name of the pod and the value is the time when the API server processed the eviction request. If the deletion didn't occur and a pod is still there it will be removed from the list automatically by PodDisruptionBudget controller after some time. If everything goes smooth this map should be empty for the most of the time. Large number of entries in the map may indicate problems with pod deletions.
            """
            return self._set("disrupted_pods", value)

        def disruptions_allowed(self, value: int, /) -> Self:
            """
            Number of pod disruptions that are currently allowed.
            """
            return self._set("disruptions_allowed", value)

        def expected_pods(self, value: int, /) -> Self:
            """
            total number of pods counted by this disruption budget
            """
            return self._set("expected_pods", value)

        def observed_generation(self, value: Optional[int], /) -> Self:
            """
            Most recent generation observed when updating this PDB status. DisruptionsAllowed and other status information is valid only if observedGeneration equals to PDB's object generation.
            """
            return self._set("observed_generation", value)

    class BuilderContext(BuilderContextBase["PodDisruptionBudgetStatus.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = PodDisruptionBudgetStatus.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for PodDisruptionBudgetStatus."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["PodDisruptionBudgetStatus", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use PodDisruptionBudgetStatus.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    conditions: Optional[List[apimachinery.Condition]] = None
    """
    Conditions contain conditions for PDB. The disruption controller sets the DisruptionAllowed condition. The following are known values for the reason field (additional reasons could be added in the future): - SyncFailed: The controller encountered an error and wasn't able to compute
                  the number of allowed disruptions. Therefore no disruptions are
                  allowed and the status of the condition will be False.
    - InsufficientPods: The number of pods are either at or below the number
                        required by the PodDisruptionBudget. No disruptions are
                        allowed and the status of the condition will be False.
    - SufficientPods: There are more pods than required by the PodDisruptionBudget.
                      The condition will be True, and the number of allowed
                      disruptions are provided by the disruptionsAllowed property.
    """
    current_healthy: Annotated[int, Field(alias="currentHealthy")]
    """
    current number of healthy pods
    """
    desired_healthy: Annotated[int, Field(alias="desiredHealthy")]
    """
    minimum desired number of healthy pods
    """
    disrupted_pods: Annotated[
        Optional[Dict[str, apimachinery.Time]], Field(alias="disruptedPods")
    ] = None
    """
    DisruptedPods contains information about pods whose eviction was processed by the API server eviction subresource handler but has not yet been observed by the PodDisruptionBudget controller. A pod will be in this map from the time when the API server processed the eviction request to the time when the pod is seen by PDB controller as having been marked for deletion (or after a timeout). The key in the map is the name of the pod and the value is the time when the API server processed the eviction request. If the deletion didn't occur and a pod is still there it will be removed from the list automatically by PodDisruptionBudget controller after some time. If everything goes smooth this map should be empty for the most of the time. Large number of entries in the map may indicate problems with pod deletions.
    """
    disruptions_allowed: Annotated[int, Field(alias="disruptionsAllowed")]
    """
    Number of pod disruptions that are currently allowed.
    """
    expected_pods: Annotated[int, Field(alias="expectedPods")]
    """
    total number of pods counted by this disruption budget
    """
    observed_generation: Annotated[Optional[int], Field(alias="observedGeneration")] = None
    """
    Most recent generation observed when updating this PDB status. DisruptionsAllowed and other status information is valid only if observedGeneration equals to PDB's object generation.
    """


class PodDisruptionBudget(Resource):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["PodDisruptionBudget"]:
            return PodDisruptionBudget

        def build(self) -> "PodDisruptionBudget":
            return PodDisruptionBudget(**self._attrs)

        def api_version(self, value: Optional[Literal["policy/v1"]], /) -> Self:
            """
            APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
            """
            return self._set("api_version", value)

        def kind(self, value: Optional[Literal["PodDisruptionBudget"]], /) -> Self:
            """
            Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
            """
            return self._set("kind", value)

        @overload
        def metadata(
            self, value_or_callback: Optional[apimachinery.ObjectMeta], /
        ) -> "PodDisruptionBudget.Builder": ...

        @overload
        def metadata(
            self,
            value_or_callback: Callable[
                [apimachinery.ObjectMeta.Builder],
                apimachinery.ObjectMeta.Builder | apimachinery.ObjectMeta,
            ],
            /,
        ) -> "PodDisruptionBudget.Builder": ...

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
            self, value_or_callback: Optional[PodDisruptionBudgetSpec], /
        ) -> "PodDisruptionBudget.Builder": ...

        @overload
        def spec(
            self,
            value_or_callback: Callable[
                [PodDisruptionBudgetSpec.Builder],
                PodDisruptionBudgetSpec.Builder | PodDisruptionBudgetSpec,
            ],
            /,
        ) -> "PodDisruptionBudget.Builder": ...

        @overload
        def spec(
            self, value_or_callback: Never = ...
        ) -> "PodDisruptionBudgetSpec.BuilderContext": ...

        def spec(self, value_or_callback=None, /):
            """
            Specification of the desired behavior of the PodDisruptionBudget.
            """
            if self._in_context and value_or_callback is None:
                context = PodDisruptionBudgetSpec.BuilderContext()
                context._parent_builder = self
                context._field_name = "spec"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(PodDisruptionBudgetSpec.builder())
                if isinstance(output, PodDisruptionBudgetSpec.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("spec", value)

        @overload
        def status(
            self, value_or_callback: Optional[PodDisruptionBudgetStatus], /
        ) -> "PodDisruptionBudget.Builder": ...

        @overload
        def status(
            self,
            value_or_callback: Callable[
                [PodDisruptionBudgetStatus.Builder],
                PodDisruptionBudgetStatus.Builder | PodDisruptionBudgetStatus,
            ],
            /,
        ) -> "PodDisruptionBudget.Builder": ...

        @overload
        def status(
            self, value_or_callback: Never = ...
        ) -> "PodDisruptionBudgetStatus.BuilderContext": ...

        def status(self, value_or_callback=None, /):
            """
            Most recently observed status of the PodDisruptionBudget.
            """
            if self._in_context and value_or_callback is None:
                context = PodDisruptionBudgetStatus.BuilderContext()
                context._parent_builder = self
                context._field_name = "status"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(PodDisruptionBudgetStatus.builder())
                if isinstance(output, PodDisruptionBudgetStatus.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("status", value)

    class BuilderContext(BuilderContextBase["PodDisruptionBudget.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = PodDisruptionBudget.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for PodDisruptionBudget."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["PodDisruptionBudget", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use PodDisruptionBudget.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    api_version: Annotated[Optional[Literal["policy/v1"]], Field(alias="apiVersion")] = "policy/v1"
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: Optional[Literal["PodDisruptionBudget"]] = "PodDisruptionBudget"
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: Optional[apimachinery.ObjectMeta] = None
    """
    Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    spec: Optional[PodDisruptionBudgetSpec] = None
    """
    Specification of the desired behavior of the PodDisruptionBudget.
    """
    status: Optional[PodDisruptionBudgetStatus] = None
    """
    Most recently observed status of the PodDisruptionBudget.
    """


PodDisruptionBudgetList = ResourceList["PodDisruptionBudget"]
