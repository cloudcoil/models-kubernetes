# Generated by cloudcoil-model-codegen v0.4.7
# DO NOT EDIT

from __future__ import annotations

from typing import Annotated, Callable, Literal, Optional, Type, overload

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
from cloudcoil.resources import Resource

from . import v1


class SelfSubjectReviewStatus(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["SelfSubjectReviewStatus"]:
            return SelfSubjectReviewStatus

        def build(self) -> "SelfSubjectReviewStatus":
            return SelfSubjectReviewStatus(**self._attrs)

        @overload
        def user_info(
            self, value_or_callback: Optional[v1.UserInfo], /
        ) -> "SelfSubjectReviewStatus.Builder": ...

        @overload
        def user_info(
            self,
            value_or_callback: Callable[[v1.UserInfo.Builder], v1.UserInfo.Builder | v1.UserInfo],
            /,
        ) -> "SelfSubjectReviewStatus.Builder": ...

        @overload
        def user_info(self, value_or_callback: Never = ...) -> "v1.UserInfo.BuilderContext": ...

        def user_info(self, value_or_callback=None, /):
            """
            User attributes of the user making this request.
            """
            if self._in_context and value_or_callback is None:
                context = v1.UserInfo.BuilderContext()
                context._parent_builder = self
                context._field_name = "user_info"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(v1.UserInfo.builder())
                if isinstance(output, v1.UserInfo.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("user_info", value)

    class BuilderContext(BuilderContextBase["SelfSubjectReviewStatus.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = SelfSubjectReviewStatus.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for SelfSubjectReviewStatus."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["SelfSubjectReviewStatus", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use SelfSubjectReviewStatus.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    user_info: Annotated[Optional[v1.UserInfo], Field(alias="userInfo")] = None
    """
    User attributes of the user making this request.
    """


class SelfSubjectReview(Resource):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["SelfSubjectReview"]:
            return SelfSubjectReview

        def build(self) -> "SelfSubjectReview":
            return SelfSubjectReview(**self._attrs)

        def api_version(
            self, value: Optional[Literal["authentication.k8s.io/v1alpha1"]], /
        ) -> Self:
            """
            APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
            """
            return self._set("api_version", value)

        def kind(self, value: Optional[Literal["SelfSubjectReview"]], /) -> Self:
            """
            Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
            """
            return self._set("kind", value)

        @overload
        def metadata(
            self, value_or_callback: Optional[apimachinery.ObjectMeta], /
        ) -> "SelfSubjectReview.Builder": ...

        @overload
        def metadata(
            self,
            value_or_callback: Callable[
                [apimachinery.ObjectMeta.Builder],
                apimachinery.ObjectMeta.Builder | apimachinery.ObjectMeta,
            ],
            /,
        ) -> "SelfSubjectReview.Builder": ...

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
        def status(
            self, value_or_callback: Optional[SelfSubjectReviewStatus], /
        ) -> "SelfSubjectReview.Builder": ...

        @overload
        def status(
            self,
            value_or_callback: Callable[
                [SelfSubjectReviewStatus.Builder],
                SelfSubjectReviewStatus.Builder | SelfSubjectReviewStatus,
            ],
            /,
        ) -> "SelfSubjectReview.Builder": ...

        @overload
        def status(
            self, value_or_callback: Never = ...
        ) -> "SelfSubjectReviewStatus.BuilderContext": ...

        def status(self, value_or_callback=None, /):
            """
            Status is filled in by the server with the user attributes.
            """
            if self._in_context and value_or_callback is None:
                context = SelfSubjectReviewStatus.BuilderContext()
                context._parent_builder = self
                context._field_name = "status"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(SelfSubjectReviewStatus.builder())
                if isinstance(output, SelfSubjectReviewStatus.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("status", value)

    class BuilderContext(BuilderContextBase["SelfSubjectReview.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = SelfSubjectReview.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for SelfSubjectReview."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["SelfSubjectReview", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use SelfSubjectReview.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    api_version: Annotated[
        Optional[Literal["authentication.k8s.io/v1alpha1"]], Field(alias="apiVersion")
    ] = "authentication.k8s.io/v1alpha1"
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: Optional[Literal["SelfSubjectReview"]] = "SelfSubjectReview"
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: Optional[apimachinery.ObjectMeta] = None
    """
    Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
    """
    status: Optional[SelfSubjectReviewStatus] = None
    """
    Status is filled in by the server with the user attributes.
    """
