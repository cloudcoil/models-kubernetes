# Generated by cloudcoil-model-codegen v0.0.24
# DO NOT EDIT

from __future__ import annotations

from typing import Annotated, Literal, Optional

from pydantic import Field

from cloudcoil import apimachinery
from cloudcoil._pydantic import BaseModel
from cloudcoil.resources import Resource, ResourceList

from ..core import v1


class EventSeries(BaseModel):
    count: Annotated[
        int,
        Field(
            description="count is the number of occurrences in this series up to the last heartbeat time."
        ),
    ]
    last_observed_time: Annotated[
        apimachinery.MicroTime,
        Field(
            alias="lastObservedTime",
            description="lastObservedTime is the time when last Event from the series was seen before last heartbeat.",
        ),
    ]


class Event(Resource):
    action: Annotated[
        Optional[str],
        Field(
            description="action is what action was taken/failed regarding to the regarding object. It is machine-readable. This field cannot be empty for new Events and it can have at most 128 characters."
        ),
    ] = None
    api_version: Annotated[
        Optional[Literal["events.k8s.io/v1"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "events.k8s.io/v1"
    deprecated_count: Annotated[
        Optional[int],
        Field(
            alias="deprecatedCount",
            description="deprecatedCount is the deprecated field assuring backward compatibility with core.v1 Event type.",
        ),
    ] = None
    deprecated_first_timestamp: Annotated[
        Optional[apimachinery.Time],
        Field(
            alias="deprecatedFirstTimestamp",
            description="deprecatedFirstTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type.",
        ),
    ] = None
    deprecated_last_timestamp: Annotated[
        Optional[apimachinery.Time],
        Field(
            alias="deprecatedLastTimestamp",
            description="deprecatedLastTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type.",
        ),
    ] = None
    deprecated_source: Annotated[
        Optional[v1.EventSource],
        Field(
            alias="deprecatedSource",
            description="deprecatedSource is the deprecated field assuring backward compatibility with core.v1 Event type.",
        ),
    ] = None
    event_time: Annotated[
        apimachinery.MicroTime,
        Field(
            alias="eventTime",
            description="eventTime is the time when this Event was first observed. It is required.",
        ),
    ]
    kind: Annotated[
        Optional[Literal["Event"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "Event"
    metadata: Annotated[
        Optional[apimachinery.ObjectMeta],
        Field(
            description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    ] = None
    note: Annotated[
        Optional[str],
        Field(
            description="note is a human-readable description of the status of this operation. Maximal length of the note is 1kB, but libraries should be prepared to handle values up to 64kB."
        ),
    ] = None
    reason: Annotated[
        Optional[str],
        Field(
            description="reason is why the action was taken. It is human-readable. This field cannot be empty for new Events and it can have at most 128 characters."
        ),
    ] = None
    regarding: Annotated[
        Optional[v1.ObjectReference],
        Field(
            description="regarding contains the object this Event is about. In most cases it's an Object reporting controller implements, e.g. ReplicaSetController implements ReplicaSets and this event is emitted because it acts on some changes in a ReplicaSet object."
        ),
    ] = None
    related: Annotated[
        Optional[v1.ObjectReference],
        Field(
            description="related is the optional secondary object for more complex actions. E.g. when regarding object triggers a creation or deletion of related object."
        ),
    ] = None
    reporting_controller: Annotated[
        Optional[str],
        Field(
            alias="reportingController",
            description="reportingController is the name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`. This field cannot be empty for new Events.",
        ),
    ] = None
    reporting_instance: Annotated[
        Optional[str],
        Field(
            alias="reportingInstance",
            description="reportingInstance is the ID of the controller instance, e.g. `kubelet-xyzf`. This field cannot be empty for new Events and it can have at most 128 characters.",
        ),
    ] = None
    series: Annotated[
        Optional[EventSeries],
        Field(
            description="series is data about the Event series this event represents or nil if it's a singleton Event."
        ),
    ] = None
    type: Annotated[
        Optional[str],
        Field(
            description="type is the type of this event (Normal, Warning), new types could be added in the future. It is machine-readable. This field cannot be empty for new Events."
        ),
    ] = None


EventList = ResourceList["Event"]
