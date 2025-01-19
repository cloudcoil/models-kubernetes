# Generated by cloudcoil-model-codegen v0.0.31
# DO NOT EDIT

from __future__ import annotations

from typing import Annotated, List, Literal, Optional

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


class HPAScalingPolicy(BaseModel):
    period_seconds: Annotated[
        int,
        Field(
            alias="periodSeconds",
            description="periodSeconds specifies the window of time for which the policy should hold true. PeriodSeconds must be greater than zero and less than or equal to 1800 (30 min).",
        ),
    ]
    type: Annotated[str, Field(description="type is used to specify the scaling policy.")]
    value: Annotated[
        int,
        Field(
            description="value contains the amount of change which is permitted by the policy. It must be greater than zero"
        ),
    ]


class HPAScalingRules(BaseModel):
    policies: Annotated[
        Optional[List[HPAScalingPolicy]],
        Field(
            description="policies is a list of potential scaling polices which can be used during scaling. At least one policy must be specified, otherwise the HPAScalingRules will be discarded as invalid"
        ),
    ] = None
    select_policy: Annotated[
        Optional[str],
        Field(
            alias="selectPolicy",
            description="selectPolicy is used to specify which policy should be used. If not set, the default value Max is used.",
        ),
    ] = None
    stabilization_window_seconds: Annotated[
        Optional[int],
        Field(
            alias="stabilizationWindowSeconds",
            description="stabilizationWindowSeconds is the number of seconds for which past recommendations should be considered while scaling up or scaling down. StabilizationWindowSeconds must be greater than or equal to zero and less than or equal to 3600 (one hour). If not set, use the default values: - For scale up: 0 (i.e. no stabilization is done). - For scale down: 300 (i.e. the stabilization window is 300 seconds long).",
        ),
    ] = None


class HorizontalPodAutoscalerBehavior(BaseModel):
    scale_down: Annotated[
        Optional[HPAScalingRules],
        Field(
            alias="scaleDown",
            description="scaleDown is scaling policy for scaling Down. If not set, the default value is to allow to scale down to minReplicas pods, with a 300 second stabilization window (i.e., the highest recommendation for the last 300sec is used).",
        ),
    ] = None
    scale_up: Annotated[
        Optional[HPAScalingRules],
        Field(
            alias="scaleUp",
            description="scaleUp is scaling policy for scaling Up. If not set, the default value is the higher of:\n  * increase no more than 4 pods per 60 seconds\n  * double the number of pods per 60 seconds\nNo stabilization is used.",
        ),
    ] = None


class HorizontalPodAutoscalerCondition(BaseModel):
    last_transition_time: Annotated[
        Optional[apimachinery.Time],
        Field(
            alias="lastTransitionTime",
            description="lastTransitionTime is the last time the condition transitioned from one status to another",
        ),
    ] = None
    message: Annotated[
        Optional[str],
        Field(
            description="message is a human-readable explanation containing details about the transition"
        ),
    ] = None
    reason: Annotated[
        Optional[str],
        Field(description="reason is the reason for the condition's last transition."),
    ] = None
    status: Annotated[
        str,
        Field(description="status is the status of the condition (True, False, Unknown)"),
    ]
    type: Annotated[str, Field(description="type describes the current condition")]


class MetricTarget(BaseModel):
    average_utilization: Annotated[
        Optional[int],
        Field(
            alias="averageUtilization",
            description="averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type",
        ),
    ] = None
    average_value: Annotated[
        Optional[apimachinery.Quantity],
        Field(
            alias="averageValue",
            description="averageValue is the target value of the average of the metric across all relevant pods (as a quantity)",
        ),
    ] = None
    type: Annotated[
        str,
        Field(
            description="type represents whether the metric type is Utilization, Value, or AverageValue"
        ),
    ]
    value: Annotated[
        Optional[apimachinery.Quantity],
        Field(description="value is the target value of the metric (as a quantity)."),
    ] = None


class MetricValueStatus(BaseModel):
    average_utilization: Annotated[
        Optional[int],
        Field(
            alias="averageUtilization",
            description="currentAverageUtilization is the current value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.",
        ),
    ] = None
    average_value: Annotated[
        Optional[apimachinery.Quantity],
        Field(
            alias="averageValue",
            description="averageValue is the current value of the average of the metric across all relevant pods (as a quantity)",
        ),
    ] = None
    value: Annotated[
        Optional[apimachinery.Quantity],
        Field(description="value is the current value of the metric (as a quantity)."),
    ] = None


class ResourceMetricSource(BaseModel):
    name: Annotated[str, Field(description="name is the name of the resource in question.")]
    target: Annotated[
        MetricTarget,
        Field(description="target specifies the target value for the given metric"),
    ]


class ResourceMetricStatus(BaseModel):
    current: Annotated[
        MetricValueStatus,
        Field(description="current contains the current value for the given metric"),
    ]
    name: Annotated[str, Field(description="name is the name of the resource in question.")]


class ContainerResourceMetricSource(BaseModel):
    container: Annotated[
        str,
        Field(
            description="container is the name of the container in the pods of the scaling target"
        ),
    ]
    name: Annotated[str, Field(description="name is the name of the resource in question.")]
    target: Annotated[
        MetricTarget,
        Field(description="target specifies the target value for the given metric"),
    ]


class ContainerResourceMetricStatus(BaseModel):
    container: Annotated[
        str,
        Field(
            description="container is the name of the container in the pods of the scaling target"
        ),
    ]
    current: Annotated[
        MetricValueStatus,
        Field(description="current contains the current value for the given metric"),
    ]
    name: Annotated[str, Field(description="name is the name of the resource in question.")]


class MetricIdentifier(BaseModel):
    name: Annotated[str, Field(description="name is the name of the given metric")]
    selector: Annotated[
        Optional[apimachinery.LabelSelector],
        Field(
            description="selector is the string-encoded form of a standard kubernetes label selector for the given metric When set, it is passed as an additional parameter to the metrics server for more specific metrics scoping. When unset, just the metricName will be used to gather metrics."
        ),
    ] = None


class ObjectMetricSource(BaseModel):
    described_object: Annotated[
        CrossVersionObjectReference,
        Field(
            alias="describedObject",
            description="describedObject specifies the descriptions of a object,such as kind,name apiVersion",
        ),
    ]
    metric: Annotated[
        MetricIdentifier,
        Field(description="metric identifies the target metric by name and selector"),
    ]
    target: Annotated[
        MetricTarget,
        Field(description="target specifies the target value for the given metric"),
    ]


class ObjectMetricStatus(BaseModel):
    current: Annotated[
        MetricValueStatus,
        Field(description="current contains the current value for the given metric"),
    ]
    described_object: Annotated[
        CrossVersionObjectReference,
        Field(
            alias="describedObject",
            description="DescribedObject specifies the descriptions of a object,such as kind,name apiVersion",
        ),
    ]
    metric: Annotated[
        MetricIdentifier,
        Field(description="metric identifies the target metric by name and selector"),
    ]


class PodsMetricSource(BaseModel):
    metric: Annotated[
        MetricIdentifier,
        Field(description="metric identifies the target metric by name and selector"),
    ]
    target: Annotated[
        MetricTarget,
        Field(description="target specifies the target value for the given metric"),
    ]


class PodsMetricStatus(BaseModel):
    current: Annotated[
        MetricValueStatus,
        Field(description="current contains the current value for the given metric"),
    ]
    metric: Annotated[
        MetricIdentifier,
        Field(description="metric identifies the target metric by name and selector"),
    ]


class ExternalMetricSource(BaseModel):
    metric: Annotated[
        MetricIdentifier,
        Field(description="metric identifies the target metric by name and selector"),
    ]
    target: Annotated[
        MetricTarget,
        Field(description="target specifies the target value for the given metric"),
    ]


class ExternalMetricStatus(BaseModel):
    current: Annotated[
        MetricValueStatus,
        Field(description="current contains the current value for the given metric"),
    ]
    metric: Annotated[
        MetricIdentifier,
        Field(description="metric identifies the target metric by name and selector"),
    ]


class MetricSpec(BaseModel):
    container_resource: Annotated[
        Optional[ContainerResourceMetricSource],
        Field(
            alias="containerResource",
            description='containerResource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing a single container in each pod of the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source. This is an alpha feature and can be enabled by the HPAContainerMetrics feature flag.',
        ),
    ] = None
    external: Annotated[
        Optional[ExternalMetricSource],
        Field(
            description="external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster)."
        ),
    ] = None
    object: Annotated[
        Optional[ObjectMetricSource],
        Field(
            description="object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object)."
        ),
    ] = None
    pods: Annotated[
        Optional[PodsMetricSource],
        Field(
            description="pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value."
        ),
    ] = None
    resource: Annotated[
        Optional[ResourceMetricSource],
        Field(
            description='resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source.'
        ),
    ] = None
    type: Annotated[
        str,
        Field(
            description='type is the type of metric source.  It should be one of "ContainerResource", "External", "Object", "Pods" or "Resource", each mapping to a matching field in the object. Note: "ContainerResource" type is available on when the feature-gate HPAContainerMetrics is enabled'
        ),
    ]


class MetricStatus(BaseModel):
    container_resource: Annotated[
        Optional[ContainerResourceMetricStatus],
        Field(
            alias="containerResource",
            description='container resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing a single container in each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source.',
        ),
    ] = None
    external: Annotated[
        Optional[ExternalMetricStatus],
        Field(
            description="external refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster)."
        ),
    ] = None
    object: Annotated[
        Optional[ObjectMetricStatus],
        Field(
            description="object refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object)."
        ),
    ] = None
    pods: Annotated[
        Optional[PodsMetricStatus],
        Field(
            description="pods refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second).  The values will be averaged together before being compared to the target value."
        ),
    ] = None
    resource: Annotated[
        Optional[ResourceMetricStatus],
        Field(
            description='resource refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the "pods" source.'
        ),
    ] = None
    type: Annotated[
        str,
        Field(
            description='type is the type of metric source.  It will be one of "ContainerResource", "External", "Object", "Pods" or "Resource", each corresponds to a matching field in the object. Note: "ContainerResource" type is available on when the feature-gate HPAContainerMetrics is enabled'
        ),
    ]


class HorizontalPodAutoscalerSpec(BaseModel):
    behavior: Annotated[
        Optional[HorizontalPodAutoscalerBehavior],
        Field(
            description="behavior configures the scaling behavior of the target in both Up and Down directions (scaleUp and scaleDown fields respectively). If not set, the default HPAScalingRules for scale up and scale down are used."
        ),
    ] = None
    max_replicas: Annotated[
        int,
        Field(
            alias="maxReplicas",
            description="maxReplicas is the upper limit for the number of replicas to which the autoscaler can scale up. It cannot be less that minReplicas.",
        ),
    ]
    metrics: Annotated[
        Optional[List[MetricSpec]],
        Field(
            description="metrics contains the specifications for which to use to calculate the desired replica count (the maximum replica count across all metrics will be used).  The desired replica count is calculated multiplying the ratio between the target value and the current value by the current number of pods.  Ergo, metrics used must decrease as the pod count is increased, and vice-versa.  See the individual metric source types for more information about how each type of metric must respond. If not set, the default metric will be set to 80% average CPU utilization."
        ),
    ] = None
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
            description="scaleTargetRef points to the target resource to scale, and is used to the pods for which metrics should be collected, as well as to actually change the replica count.",
        ),
    ]


class HorizontalPodAutoscalerStatus(BaseModel):
    conditions: Annotated[
        Optional[List[HorizontalPodAutoscalerCondition]],
        Field(
            description="conditions is the set of conditions required for this autoscaler to scale its target, and indicates whether or not those conditions are met."
        ),
    ] = None
    current_metrics: Annotated[
        Optional[List[MetricStatus]],
        Field(
            alias="currentMetrics",
            description="currentMetrics is the last read state of the metrics used by this autoscaler.",
        ),
    ] = None
    current_replicas: Annotated[
        Optional[int],
        Field(
            alias="currentReplicas",
            description="currentReplicas is current number of replicas of pods managed by this autoscaler, as last seen by the autoscaler.",
        ),
    ] = None
    desired_replicas: Annotated[
        int,
        Field(
            alias="desiredReplicas",
            description="desiredReplicas is the desired number of replicas of pods managed by this autoscaler, as last calculated by the autoscaler.",
        ),
    ]
    last_scale_time: Annotated[
        Optional[apimachinery.Time],
        Field(
            alias="lastScaleTime",
            description="lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods, used by the autoscaler to control how often the number of pods is changed.",
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
        Optional[Literal["autoscaling/v2"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "autoscaling/v2"
    kind: Annotated[
        Optional[Literal["HorizontalPodAutoscaler"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "HorizontalPodAutoscaler"
    metadata: Annotated[
        Optional[apimachinery.ObjectMeta],
        Field(
            description="metadata is the standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    ] = None
    spec: Annotated[
        Optional[HorizontalPodAutoscalerSpec],
        Field(
            description="spec is the specification for the behaviour of the autoscaler. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status."
        ),
    ] = None
    status: Annotated[
        Optional[HorizontalPodAutoscalerStatus],
        Field(description="status is the current information about the autoscaler."),
    ] = None


HorizontalPodAutoscalerList = ResourceList["HorizontalPodAutoscaler"]
