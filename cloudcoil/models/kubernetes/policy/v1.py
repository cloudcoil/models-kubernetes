# Generated by cloudcoil-model-codegen v0.0.14
# DO NOT EDIT

from __future__ import annotations

from typing import Annotated, Dict, List, Literal, Optional

from pydantic import Field

from cloudcoil import apimachinery
from cloudcoil._pydantic import BaseModel
from cloudcoil.resources import Resource, ResourceList


class Eviction(Resource):
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
