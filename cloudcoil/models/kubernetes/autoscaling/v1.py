# Generated by cloudcoil-model-codegen v0.0.31
# DO NOT EDIT

from __future__ import annotations

from typing import Annotated, Literal, Optional

from pydantic import Field

from cloudcoil import apimachinery
from cloudcoil.pydantic import BaseModel
from cloudcoil.resources import Resource, ResourceList


class CrossVersionObjectReference(BaseModel):
    api_version: Annotated[
        Optional[str],
        Field(
            alias="apiVersion",
            description="apiVersion is the API version of the referent",
        ),
    ] = None
    kind: Annotated[
        str,
        Field(
            description="kind is the kind of the referent; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ]
    name: Annotated[
        str,
        Field(
            description="name is the name of the referent; More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names"
        ),
    ]


class HorizontalPodAutoscalerSpec(BaseModel):
    max_replicas: Annotated[
        int,
        Field(
            alias="maxReplicas",
            description="maxReplicas is the upper limit for the number of pods that can be set by the autoscaler; cannot be smaller than MinReplicas.",
        ),
    ]
    min_replicas: Annotated[
        Optional[int],
        Field(
            alias="minReplicas",
            description="minReplicas is the lower limit for the number of replicas to which the autoscaler can scale down.  It defaults to 1 pod.  minReplicas is allowed to be 0 if the alpha feature gate HPAScaleToZero is enabled and at least one Object or External metric is configured.  Scaling is active as long as at least one metric value is available.",
        ),
    ] = None
    scale_target_ref: Annotated[
        CrossVersionObjectReference,
        Field(
            alias="scaleTargetRef",
            description="reference to scaled resource; horizontal pod autoscaler will learn the current resource consumption and will set the desired number of pods by using its Scale subresource.",
        ),
    ]
    target_cpu_utilization_percentage: Annotated[
        Optional[int],
        Field(
            alias="targetCPUUtilizationPercentage",
            description="targetCPUUtilizationPercentage is the target average CPU utilization (represented as a percentage of requested CPU) over all the pods; if not specified the default autoscaling policy will be used.",
        ),
    ] = None


class ScaleSpec(BaseModel):
    replicas: Annotated[
        Optional[int],
        Field(description="replicas is the desired number of instances for the scaled object."),
    ] = None


class ScaleStatus(BaseModel):
    replicas: Annotated[
        int,
        Field(
            description="replicas is the actual number of observed instances of the scaled object."
        ),
    ]
    selector: Annotated[
        Optional[str],
        Field(
            description="selector is the label query over pods that should match the replicas count. This is same as the label selector but in the string format to avoid introspection by clients. The string will be in the same format as the query-param syntax. More info about label selectors: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/"
        ),
    ] = None


class HorizontalPodAutoscalerStatus(BaseModel):
    current_cpu_utilization_percentage: Annotated[
        Optional[int],
        Field(
            alias="currentCPUUtilizationPercentage",
            description="currentCPUUtilizationPercentage is the current average CPU utilization over all pods, represented as a percentage of requested CPU, e.g. 70 means that an average pod is using now 70% of its requested CPU.",
        ),
    ] = None
    current_replicas: Annotated[
        int,
        Field(
            alias="currentReplicas",
            description="currentReplicas is the current number of replicas of pods managed by this autoscaler.",
        ),
    ]
    desired_replicas: Annotated[
        int,
        Field(
            alias="desiredReplicas",
            description="desiredReplicas is the  desired number of replicas of pods managed by this autoscaler.",
        ),
    ]
    last_scale_time: Annotated[
        Optional[apimachinery.Time],
        Field(
            alias="lastScaleTime",
            description="lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods; used by the autoscaler to control how often the number of pods is changed.",
        ),
    ] = None
    observed_generation: Annotated[
        Optional[int],
        Field(
            alias="observedGeneration",
            description="observedGeneration is the most recent generation observed by this autoscaler.",
        ),
    ] = None


class HorizontalPodAutoscaler(Resource):
    api_version: Annotated[
        Optional[Literal["autoscaling/v1"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "autoscaling/v1"
    kind: Annotated[
        Optional[Literal["HorizontalPodAutoscaler"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "HorizontalPodAutoscaler"
    metadata: Annotated[
        Optional[apimachinery.ObjectMeta],
        Field(
            description="Standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    ] = None
    spec: Annotated[
        Optional[HorizontalPodAutoscalerSpec],
        Field(
            description="spec defines the behaviour of autoscaler. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status."
        ),
    ] = None
    status: Annotated[
        Optional[HorizontalPodAutoscalerStatus],
        Field(description="status is the current information about the autoscaler."),
    ] = None


HorizontalPodAutoscalerList = ResourceList["HorizontalPodAutoscaler"]


class Scale(Resource):
    api_version: Annotated[
        Optional[Literal["autoscaling/v1"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "autoscaling/v1"
    kind: Annotated[
        Optional[Literal["Scale"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "Scale"
    metadata: Annotated[
        Optional[apimachinery.ObjectMeta],
        Field(
            description="Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata."
        ),
    ] = None
    spec: Annotated[
        Optional[ScaleSpec],
        Field(
            description="spec defines the behavior of the scale. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status."
        ),
    ] = None
    status: Annotated[
        Optional[ScaleStatus],
        Field(
            description="status is the current status of the scale. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status. Read-only."
        ),
    ] = None
