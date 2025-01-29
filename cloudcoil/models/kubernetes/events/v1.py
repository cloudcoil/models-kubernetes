# Generated by cloudcoil-model-codegen v0.4.2
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

from ..core import v1


class EventSeries(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["EventSeries"]:
            return EventSeries

        def build(self) -> "EventSeries":
            return EventSeries(**self._attrs)

        def count(self, value: int, /) -> Self:
            """
            count is the number of occurrences in this series up to the last heartbeat time.
            """
            return self._set("count", value)

        @overload
        def last_observed_time(
            self, value_or_callback: apimachinery.MicroTime, /
        ) -> "EventSeries.Builder": ...

        @overload
        def last_observed_time(
            self,
            value_or_callback: Callable[
                [apimachinery.MicroTime.Builder],
                apimachinery.MicroTime.Builder | apimachinery.MicroTime,
            ],
            /,
        ) -> "EventSeries.Builder": ...

        @overload
        def last_observed_time(
            self, value_or_callback: Never = ...
        ) -> "apimachinery.MicroTime.BuilderContext": ...

        def last_observed_time(self, value_or_callback=None, /):
            """
            lastObservedTime is the time when last Event from the series was seen before last heartbeat.
            """
            if self._in_context and value_or_callback is None:
                context = apimachinery.MicroTime.BuilderContext()
                context._parent_builder = self
                context._field_name = "last_observed_time"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(apimachinery.MicroTime.builder())
                if isinstance(output, apimachinery.MicroTime.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("last_observed_time", value)

    class BuilderContext(BuilderContextBase["EventSeries.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = EventSeries.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for EventSeries."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["EventSeries", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use EventSeries.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    count: int
    """
    count is the number of occurrences in this series up to the last heartbeat time.
    """
    last_observed_time: Annotated[apimachinery.MicroTime, Field(alias="lastObservedTime")]
    """
    lastObservedTime is the time when last Event from the series was seen before last heartbeat.
    """


class Event(Resource):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["Event"]:
            return Event

        def build(self) -> "Event":
            return Event(**self._attrs)

        def action(self, value: Optional[str], /) -> Self:
            """
            action is what action was taken/failed regarding to the regarding object. It is machine-readable. This field cannot be empty for new Events and it can have at most 128 characters.
            """
            return self._set("action", value)

        def api_version(self, value: Optional[Literal["events.k8s.io/v1"]], /) -> Self:
            """
            APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
            """
            return self._set("api_version", value)

        def deprecated_count(self, value: Optional[int], /) -> Self:
            """
            deprecatedCount is the deprecated field assuring backward compatibility with core.v1 Event type.
            """
            return self._set("deprecated_count", value)

        @overload
        def deprecated_first_timestamp(
            self, value_or_callback: Optional[apimachinery.Time], /
        ) -> "Event.Builder": ...

        @overload
        def deprecated_first_timestamp(
            self,
            value_or_callback: Callable[
                [apimachinery.Time.Builder],
                apimachinery.Time.Builder | apimachinery.Time,
            ],
            /,
        ) -> "Event.Builder": ...

        @overload
        def deprecated_first_timestamp(
            self, value_or_callback: Never = ...
        ) -> "apimachinery.Time.BuilderContext": ...

        def deprecated_first_timestamp(self, value_or_callback=None, /):
            """
            deprecatedFirstTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type.
            """
            if self._in_context and value_or_callback is None:
                context = apimachinery.Time.BuilderContext()
                context._parent_builder = self
                context._field_name = "deprecated_first_timestamp"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(apimachinery.Time.builder())
                if isinstance(output, apimachinery.Time.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("deprecated_first_timestamp", value)

        @overload
        def deprecated_last_timestamp(
            self, value_or_callback: Optional[apimachinery.Time], /
        ) -> "Event.Builder": ...

        @overload
        def deprecated_last_timestamp(
            self,
            value_or_callback: Callable[
                [apimachinery.Time.Builder],
                apimachinery.Time.Builder | apimachinery.Time,
            ],
            /,
        ) -> "Event.Builder": ...

        @overload
        def deprecated_last_timestamp(
            self, value_or_callback: Never = ...
        ) -> "apimachinery.Time.BuilderContext": ...

        def deprecated_last_timestamp(self, value_or_callback=None, /):
            """
            deprecatedLastTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type.
            """
            if self._in_context and value_or_callback is None:
                context = apimachinery.Time.BuilderContext()
                context._parent_builder = self
                context._field_name = "deprecated_last_timestamp"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(apimachinery.Time.builder())
                if isinstance(output, apimachinery.Time.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("deprecated_last_timestamp", value)

        @overload
        def deprecated_source(
            self, value_or_callback: Optional[v1.EventSource], /
        ) -> "Event.Builder": ...

        @overload
        def deprecated_source(
            self,
            value_or_callback: Callable[
                [v1.EventSource.Builder], v1.EventSource.Builder | v1.EventSource
            ],
            /,
        ) -> "Event.Builder": ...

        @overload
        def deprecated_source(
            self, value_or_callback: Never = ...
        ) -> "v1.EventSource.BuilderContext": ...

        def deprecated_source(self, value_or_callback=None, /):
            """
            deprecatedSource is the deprecated field assuring backward compatibility with core.v1 Event type.
            """
            if self._in_context and value_or_callback is None:
                context = v1.EventSource.BuilderContext()
                context._parent_builder = self
                context._field_name = "deprecated_source"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(v1.EventSource.builder())
                if isinstance(output, v1.EventSource.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("deprecated_source", value)

        @overload
        def event_time(self, value_or_callback: apimachinery.MicroTime, /) -> "Event.Builder": ...

        @overload
        def event_time(
            self,
            value_or_callback: Callable[
                [apimachinery.MicroTime.Builder],
                apimachinery.MicroTime.Builder | apimachinery.MicroTime,
            ],
            /,
        ) -> "Event.Builder": ...

        @overload
        def event_time(
            self, value_or_callback: Never = ...
        ) -> "apimachinery.MicroTime.BuilderContext": ...

        def event_time(self, value_or_callback=None, /):
            """
            eventTime is the time when this Event was first observed. It is required.
            """
            if self._in_context and value_or_callback is None:
                context = apimachinery.MicroTime.BuilderContext()
                context._parent_builder = self
                context._field_name = "event_time"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(apimachinery.MicroTime.builder())
                if isinstance(output, apimachinery.MicroTime.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("event_time", value)

        def kind(self, value: Optional[Literal["Event"]], /) -> Self:
            """
            Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
            """
            return self._set("kind", value)

        @overload
        def metadata(
            self, value_or_callback: Optional[apimachinery.ObjectMeta], /
        ) -> "Event.Builder": ...

        @overload
        def metadata(
            self,
            value_or_callback: Callable[
                [apimachinery.ObjectMeta.Builder],
                apimachinery.ObjectMeta.Builder | apimachinery.ObjectMeta,
            ],
            /,
        ) -> "Event.Builder": ...

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

        def note(self, value: Optional[str], /) -> Self:
            """
            note is a human-readable description of the status of this operation. Maximal length of the note is 1kB, but libraries should be prepared to handle values up to 64kB.
            """
            return self._set("note", value)

        def reason(self, value: Optional[str], /) -> Self:
            """
            reason is why the action was taken. It is human-readable. This field cannot be empty for new Events and it can have at most 128 characters.
            """
            return self._set("reason", value)

        @overload
        def regarding(
            self, value_or_callback: Optional[v1.ObjectReference], /
        ) -> "Event.Builder": ...

        @overload
        def regarding(
            self,
            value_or_callback: Callable[
                [v1.ObjectReference.Builder],
                v1.ObjectReference.Builder | v1.ObjectReference,
            ],
            /,
        ) -> "Event.Builder": ...

        @overload
        def regarding(
            self, value_or_callback: Never = ...
        ) -> "v1.ObjectReference.BuilderContext": ...

        def regarding(self, value_or_callback=None, /):
            """
            regarding contains the object this Event is about. In most cases it's an Object reporting controller implements, e.g. ReplicaSetController implements ReplicaSets and this event is emitted because it acts on some changes in a ReplicaSet object.
            """
            if self._in_context and value_or_callback is None:
                context = v1.ObjectReference.BuilderContext()
                context._parent_builder = self
                context._field_name = "regarding"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(v1.ObjectReference.builder())
                if isinstance(output, v1.ObjectReference.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("regarding", value)

        @overload
        def related(
            self, value_or_callback: Optional[v1.ObjectReference], /
        ) -> "Event.Builder": ...

        @overload
        def related(
            self,
            value_or_callback: Callable[
                [v1.ObjectReference.Builder],
                v1.ObjectReference.Builder | v1.ObjectReference,
            ],
            /,
        ) -> "Event.Builder": ...

        @overload
        def related(
            self, value_or_callback: Never = ...
        ) -> "v1.ObjectReference.BuilderContext": ...

        def related(self, value_or_callback=None, /):
            """
            related is the optional secondary object for more complex actions. E.g. when regarding object triggers a creation or deletion of related object.
            """
            if self._in_context and value_or_callback is None:
                context = v1.ObjectReference.BuilderContext()
                context._parent_builder = self
                context._field_name = "related"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(v1.ObjectReference.builder())
                if isinstance(output, v1.ObjectReference.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("related", value)

        def reporting_controller(self, value: Optional[str], /) -> Self:
            """
            reportingController is the name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`. This field cannot be empty for new Events.
            """
            return self._set("reporting_controller", value)

        def reporting_instance(self, value: Optional[str], /) -> Self:
            """
            reportingInstance is the ID of the controller instance, e.g. `kubelet-xyzf`. This field cannot be empty for new Events and it can have at most 128 characters.
            """
            return self._set("reporting_instance", value)

        @overload
        def series(self, value_or_callback: Optional[EventSeries], /) -> "Event.Builder": ...

        @overload
        def series(
            self,
            value_or_callback: Callable[[EventSeries.Builder], EventSeries.Builder | EventSeries],
            /,
        ) -> "Event.Builder": ...

        @overload
        def series(self, value_or_callback: Never = ...) -> "EventSeries.BuilderContext": ...

        def series(self, value_or_callback=None, /):
            """
            series is data about the Event series this event represents or nil if it's a singleton Event.
            """
            if self._in_context and value_or_callback is None:
                context = EventSeries.BuilderContext()
                context._parent_builder = self
                context._field_name = "series"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(EventSeries.builder())
                if isinstance(output, EventSeries.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("series", value)

        def type(self, value: Optional[str], /) -> Self:
            """
            type is the type of this event (Normal, Warning), new types could be added in the future. It is machine-readable. This field cannot be empty for new Events.
            """
            return self._set("type", value)

    class BuilderContext(BuilderContextBase["Event.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = Event.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for Event."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["Event", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use Event.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    action: Optional[str] = None
    """
    action is what action was taken/failed regarding to the regarding object. It is machine-readable. This field cannot be empty for new Events and it can have at most 128 characters.
    """
    api_version: Annotated[Optional[Literal["events.k8s.io/v1"]], Field(alias="apiVersion")] = (
        "events.k8s.io/v1"
    )
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    deprecated_count: Annotated[Optional[int], Field(alias="deprecatedCount")] = None
    """
    deprecatedCount is the deprecated field assuring backward compatibility with core.v1 Event type.
    """
    deprecated_first_timestamp: Annotated[
        Optional[apimachinery.Time], Field(alias="deprecatedFirstTimestamp")
    ] = None
    """
    deprecatedFirstTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type.
    """
    deprecated_last_timestamp: Annotated[
        Optional[apimachinery.Time], Field(alias="deprecatedLastTimestamp")
    ] = None
    """
    deprecatedLastTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type.
    """
    deprecated_source: Annotated[Optional[v1.EventSource], Field(alias="deprecatedSource")] = None
    """
    deprecatedSource is the deprecated field assuring backward compatibility with core.v1 Event type.
    """
    event_time: Annotated[apimachinery.MicroTime, Field(alias="eventTime")]
    """
    eventTime is the time when this Event was first observed. It is required.
    """
    kind: Optional[Literal["Event"]] = "Event"
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: Optional[apimachinery.ObjectMeta] = None
    """
    Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    note: Optional[str] = None
    """
    note is a human-readable description of the status of this operation. Maximal length of the note is 1kB, but libraries should be prepared to handle values up to 64kB.
    """
    reason: Optional[str] = None
    """
    reason is why the action was taken. It is human-readable. This field cannot be empty for new Events and it can have at most 128 characters.
    """
    regarding: Optional[v1.ObjectReference] = None
    """
    regarding contains the object this Event is about. In most cases it's an Object reporting controller implements, e.g. ReplicaSetController implements ReplicaSets and this event is emitted because it acts on some changes in a ReplicaSet object.
    """
    related: Optional[v1.ObjectReference] = None
    """
    related is the optional secondary object for more complex actions. E.g. when regarding object triggers a creation or deletion of related object.
    """
    reporting_controller: Annotated[Optional[str], Field(alias="reportingController")] = None
    """
    reportingController is the name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`. This field cannot be empty for new Events.
    """
    reporting_instance: Annotated[Optional[str], Field(alias="reportingInstance")] = None
    """
    reportingInstance is the ID of the controller instance, e.g. `kubelet-xyzf`. This field cannot be empty for new Events and it can have at most 128 characters.
    """
    series: Optional[EventSeries] = None
    """
    series is data about the Event series this event represents or nil if it's a singleton Event.
    """
    type: Optional[str] = None
    """
    type is the type of this event (Normal, Warning), new types could be added in the future. It is machine-readable. This field cannot be empty for new Events.
    """


EventList = ResourceList["Event"]
