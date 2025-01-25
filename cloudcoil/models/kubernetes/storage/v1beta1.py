# Generated by cloudcoil-model-codegen v0.3.0
# DO NOT EDIT

from __future__ import annotations

from typing import (
    Annotated,
    Callable,
    Dict,
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


class VolumeAttributesClass(Resource):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["VolumeAttributesClass"]:
            return VolumeAttributesClass

        def build(self) -> "VolumeAttributesClass":
            return VolumeAttributesClass(**self._attrs)

        def api_version(self, value: Optional[Literal["storage.k8s.io/v1beta1"]], /) -> Self:
            """
            APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
            """
            return self._set("api_version", value)

        def driver_name(self, value: str, /) -> Self:
            """
            Name of the CSI driver This field is immutable.
            """
            return self._set("driver_name", value)

        def kind(self, value: Optional[Literal["VolumeAttributesClass"]], /) -> Self:
            """
            Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
            """
            return self._set("kind", value)

        @overload
        def metadata(
            self, value_or_callback: Optional[apimachinery.ObjectMeta], /
        ) -> "VolumeAttributesClass.Builder": ...

        @overload
        def metadata(
            self,
            value_or_callback: Callable[
                [apimachinery.ObjectMeta.Builder],
                apimachinery.ObjectMeta.Builder | apimachinery.ObjectMeta,
            ],
            /,
        ) -> "VolumeAttributesClass.Builder": ...

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

        def parameters(self, value: Optional[Dict[str, str]], /) -> Self:
            """
            parameters hold volume attributes defined by the CSI driver. These values are opaque to the Kubernetes and are passed directly to the CSI driver. The underlying storage provider supports changing these attributes on an existing volume, however the parameters field itself is immutable. To invoke a volume update, a new VolumeAttributesClass should be created with new parameters, and the PersistentVolumeClaim should be updated to reference the new VolumeAttributesClass.

            This field is required and must contain at least one key/value pair. The keys cannot be empty, and the maximum number of parameters is 512, with a cumulative max size of 256K. If the CSI driver rejects invalid parameters, the target PersistentVolumeClaim will be set to an "Infeasible" state in the modifyVolumeStatus field.
            """
            return self._set("parameters", value)

    class BuilderContext(BuilderContextBase["VolumeAttributesClass.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = VolumeAttributesClass.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for VolumeAttributesClass."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["VolumeAttributesClass", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use VolumeAttributesClass.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    api_version: Annotated[
        Optional[Literal["storage.k8s.io/v1beta1"]], Field(alias="apiVersion")
    ] = "storage.k8s.io/v1beta1"
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    driver_name: Annotated[str, Field(alias="driverName")]
    """
    Name of the CSI driver This field is immutable.
    """
    kind: Optional[Literal["VolumeAttributesClass"]] = "VolumeAttributesClass"
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: Optional[apimachinery.ObjectMeta] = None
    """
    Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    parameters: Optional[Dict[str, str]] = None
    """
    parameters hold volume attributes defined by the CSI driver. These values are opaque to the Kubernetes and are passed directly to the CSI driver. The underlying storage provider supports changing these attributes on an existing volume, however the parameters field itself is immutable. To invoke a volume update, a new VolumeAttributesClass should be created with new parameters, and the PersistentVolumeClaim should be updated to reference the new VolumeAttributesClass.

    This field is required and must contain at least one key/value pair. The keys cannot be empty, and the maximum number of parameters is 512, with a cumulative max size of 256K. If the CSI driver rejects invalid parameters, the target PersistentVolumeClaim will be set to an "Infeasible" state in the modifyVolumeStatus field.
    """


VolumeAttributesClassList = ResourceList["VolumeAttributesClass"]
