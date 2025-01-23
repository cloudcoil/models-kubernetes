# Generated by cloudcoil-model-codegen v0.1.1
# DO NOT EDIT

from __future__ import annotations

from typing import Annotated, Callable, Dict, List, Literal, Optional, Type, Union

from pydantic import Field

from cloudcoil import apimachinery
from cloudcoil.pydantic import BaseBuilder, BaseModel, ListBuilder, Self
from cloudcoil.resources import Resource, ResourceList


class Eviction(Resource):
    class Builder(BaseBuilder):
        def build(self) -> "Eviction":
            return Eviction(**self._attrs)

        def api_version(self, value: Optional[Literal["policy/v1"]]) -> Self:
            return self._set("api_version", value)

        def delete_options(
            self,
            value_or_callback: Union[
                Optional[apimachinery.DeleteOptions],
                Callable[[Type[apimachinery.DeleteOptions]], apimachinery.DeleteOptions],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(apimachinery.DeleteOptions)
            return self._set("delete_options", value)

        def kind(self, value: Optional[Literal["Eviction"]]) -> Self:
            return self._set("kind", value)

        def metadata(
            self,
            value_or_callback: Union[
                Optional[apimachinery.ObjectMeta],
                Callable[[Type[apimachinery.ObjectMeta]], apimachinery.ObjectMeta],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(apimachinery.ObjectMeta)
            return self._set("metadata", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def list_builder(cls) -> ListBuilder[Self]:
        return ListBuilder[cls]()  # type: ignore[valid-type]

    api_version: Annotated[
        Optional[Literal["policy/v1"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "policy/v1"
    delete_options: Annotated[
        Optional[apimachinery.DeleteOptions],
        Field(alias="deleteOptions", description="DeleteOptions may be provided"),
    ] = None
    kind: Annotated[
        Optional[Literal["Eviction"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "Eviction"
    metadata: Annotated[
        Optional[apimachinery.ObjectMeta],
        Field(description="ObjectMeta describes the pod that is being evicted."),
    ] = None


class PodDisruptionBudgetSpec(BaseModel):
    class Builder(BaseBuilder):
        def build(self) -> "PodDisruptionBudgetSpec":
            return PodDisruptionBudgetSpec(**self._attrs)

        def max_unavailable(
            self,
            value_or_callback: Union[
                Optional[apimachinery.IntOrString],
                Callable[[Type[apimachinery.IntOrString]], apimachinery.IntOrString],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(apimachinery.IntOrString)
            return self._set("max_unavailable", value)

        def min_available(
            self,
            value_or_callback: Union[
                Optional[apimachinery.IntOrString],
                Callable[[Type[apimachinery.IntOrString]], apimachinery.IntOrString],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(apimachinery.IntOrString)
            return self._set("min_available", value)

        def selector(
            self,
            value_or_callback: Union[
                Optional[apimachinery.LabelSelector],
                Callable[[Type[apimachinery.LabelSelector]], apimachinery.LabelSelector],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(apimachinery.LabelSelector)
            return self._set("selector", value)

        def unhealthy_pod_eviction_policy(self, value: Optional[str]) -> Self:
            return self._set("unhealthy_pod_eviction_policy", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def list_builder(cls) -> ListBuilder[Self]:
        return ListBuilder[cls]()  # type: ignore[valid-type]

    max_unavailable: Annotated[
        Optional[apimachinery.IntOrString],
        Field(
            alias="maxUnavailable",
            description='An eviction is allowed if at most "maxUnavailable" pods selected by "selector" are unavailable after the eviction, i.e. even in absence of the evicted pod. For example, one can prevent all voluntary evictions by specifying 0. This is a mutually exclusive setting with "minAvailable".',
        ),
    ] = None
    min_available: Annotated[
        Optional[apimachinery.IntOrString],
        Field(
            alias="minAvailable",
            description='An eviction is allowed if at least "minAvailable" pods selected by "selector" will still be available after the eviction, i.e. even in the absence of the evicted pod.  So for example you can prevent all voluntary evictions by specifying "100%".',
        ),
    ] = None
    selector: Annotated[
        Optional[apimachinery.LabelSelector],
        Field(
            description="Label query over pods whose evictions are managed by the disruption budget. A null selector will match no pods, while an empty ({}) selector will select all pods within the namespace."
        ),
    ] = None
    unhealthy_pod_eviction_policy: Annotated[
        Optional[str],
        Field(
            alias="unhealthyPodEvictionPolicy",
            description='UnhealthyPodEvictionPolicy defines the criteria for when unhealthy pods should be considered for eviction. Current implementation considers healthy pods, as pods that have status.conditions item with type="Ready",status="True".\n\nValid policies are IfHealthyBudget and AlwaysAllow. If no policy is specified, the default behavior will be used, which corresponds to the IfHealthyBudget policy.\n\nIfHealthyBudget policy means that running pods (status.phase="Running"), but not yet healthy can be evicted only if the guarded application is not disrupted (status.currentHealthy is at least equal to status.desiredHealthy). Healthy pods will be subject to the PDB for eviction.\n\nAlwaysAllow policy means that all running pods (status.phase="Running"), but not yet healthy are considered disrupted and can be evicted regardless of whether the criteria in a PDB is met. This means perspective running pods of a disrupted application might not get a chance to become healthy. Healthy pods will be subject to the PDB for eviction.\n\nAdditional policies may be added in the future. Clients making eviction decisions should disallow eviction of unhealthy pods if they encounter an unrecognized policy in this field.\n\nThis field is beta-level. The eviction API uses this field when the feature gate PDBUnhealthyPodEvictionPolicy is enabled (enabled by default).',
        ),
    ] = None


class PodDisruptionBudgetStatus(BaseModel):
    class Builder(BaseBuilder):
        def build(self) -> "PodDisruptionBudgetStatus":
            return PodDisruptionBudgetStatus(**self._attrs)

        def conditions(
            self,
            value_or_callback: Union[
                Optional[List[apimachinery.Condition]],
                Callable[[Type[apimachinery.Condition]], List[apimachinery.Condition]],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(apimachinery.Condition)
            return self._set("conditions", value)

        def current_healthy(self, value: int) -> Self:
            return self._set("current_healthy", value)

        def desired_healthy(self, value: int) -> Self:
            return self._set("desired_healthy", value)

        def disrupted_pods(self, value: Optional[Dict[str, apimachinery.Time]]) -> Self:
            return self._set("disrupted_pods", value)

        def disruptions_allowed(self, value: int) -> Self:
            return self._set("disruptions_allowed", value)

        def expected_pods(self, value: int) -> Self:
            return self._set("expected_pods", value)

        def observed_generation(self, value: Optional[int]) -> Self:
            return self._set("observed_generation", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def list_builder(cls) -> ListBuilder[Self]:
        return ListBuilder[cls]()  # type: ignore[valid-type]

    conditions: Annotated[
        Optional[List[apimachinery.Condition]],
        Field(
            description="Conditions contain conditions for PDB. The disruption controller sets the DisruptionAllowed condition. The following are known values for the reason field (additional reasons could be added in the future): - SyncFailed: The controller encountered an error and wasn't able to compute\n              the number of allowed disruptions. Therefore no disruptions are\n              allowed and the status of the condition will be False.\n- InsufficientPods: The number of pods are either at or below the number\n                    required by the PodDisruptionBudget. No disruptions are\n                    allowed and the status of the condition will be False.\n- SufficientPods: There are more pods than required by the PodDisruptionBudget.\n                  The condition will be True, and the number of allowed\n                  disruptions are provided by the disruptionsAllowed property."
        ),
    ] = None
    current_healthy: Annotated[
        int, Field(alias="currentHealthy", description="current number of healthy pods")
    ]
    desired_healthy: Annotated[
        int,
        Field(alias="desiredHealthy", description="minimum desired number of healthy pods"),
    ]
    disrupted_pods: Annotated[
        Optional[Dict[str, apimachinery.Time]],
        Field(
            alias="disruptedPods",
            description="DisruptedPods contains information about pods whose eviction was processed by the API server eviction subresource handler but has not yet been observed by the PodDisruptionBudget controller. A pod will be in this map from the time when the API server processed the eviction request to the time when the pod is seen by PDB controller as having been marked for deletion (or after a timeout). The key in the map is the name of the pod and the value is the time when the API server processed the eviction request. If the deletion didn't occur and a pod is still there it will be removed from the list automatically by PodDisruptionBudget controller after some time. If everything goes smooth this map should be empty for the most of the time. Large number of entries in the map may indicate problems with pod deletions.",
        ),
    ] = None
    disruptions_allowed: Annotated[
        int,
        Field(
            alias="disruptionsAllowed",
            description="Number of pod disruptions that are currently allowed.",
        ),
    ]
    expected_pods: Annotated[
        int,
        Field(
            alias="expectedPods",
            description="total number of pods counted by this disruption budget",
        ),
    ]
    observed_generation: Annotated[
        Optional[int],
        Field(
            alias="observedGeneration",
            description="Most recent generation observed when updating this PDB status. DisruptionsAllowed and other status information is valid only if observedGeneration equals to PDB's object generation.",
        ),
    ] = None


class PodDisruptionBudget(Resource):
    class Builder(BaseBuilder):
        def build(self) -> "PodDisruptionBudget":
            return PodDisruptionBudget(**self._attrs)

        def api_version(self, value: Optional[Literal["policy/v1"]]) -> Self:
            return self._set("api_version", value)

        def kind(self, value: Optional[Literal["PodDisruptionBudget"]]) -> Self:
            return self._set("kind", value)

        def metadata(
            self,
            value_or_callback: Union[
                Optional[apimachinery.ObjectMeta],
                Callable[[Type[apimachinery.ObjectMeta]], apimachinery.ObjectMeta],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(apimachinery.ObjectMeta)
            return self._set("metadata", value)

        def spec(
            self,
            value_or_callback: Union[
                Optional[PodDisruptionBudgetSpec],
                Callable[[Type[PodDisruptionBudgetSpec]], PodDisruptionBudgetSpec],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(PodDisruptionBudgetSpec)
            return self._set("spec", value)

        def status(
            self,
            value_or_callback: Union[
                Optional[PodDisruptionBudgetStatus],
                Callable[[Type[PodDisruptionBudgetStatus]], PodDisruptionBudgetStatus],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(PodDisruptionBudgetStatus)
            return self._set("status", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def list_builder(cls) -> ListBuilder[Self]:
        return ListBuilder[cls]()  # type: ignore[valid-type]

    api_version: Annotated[
        Optional[Literal["policy/v1"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "policy/v1"
    kind: Annotated[
        Optional[Literal["PodDisruptionBudget"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "PodDisruptionBudget"
    metadata: Annotated[
        Optional[apimachinery.ObjectMeta],
        Field(
            description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    ] = None
    spec: Annotated[
        Optional[PodDisruptionBudgetSpec],
        Field(description="Specification of the desired behavior of the PodDisruptionBudget."),
    ] = None
    status: Annotated[
        Optional[PodDisruptionBudgetStatus],
        Field(description="Most recently observed status of the PodDisruptionBudget."),
    ] = None


PodDisruptionBudgetList = ResourceList["PodDisruptionBudget"]
