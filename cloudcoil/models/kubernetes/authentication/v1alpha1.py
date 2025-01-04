# Generated by cloudcoil-model-codegen v0.0.14
# DO NOT EDIT

from __future__ import annotations

from typing import Annotated, Literal, Optional

from pydantic import Field

from cloudcoil import apimachinery
from cloudcoil._pydantic import BaseModel
from cloudcoil.resources import Resource

from . import v1


class SelfSubjectReviewStatus(BaseModel):
    user_info: Annotated[
        Optional[v1.UserInfo],
        Field(
            alias="userInfo",
            description="User attributes of the user making this request.",
        ),
    ] = None


class SelfSubjectReview(Resource):
    api_version: Annotated[
        Optional[Literal["authentication.k8s.io/v1alpha1"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "authentication.k8s.io/v1alpha1"
    kind: Annotated[
        Optional[Literal["SelfSubjectReview"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "SelfSubjectReview"
    metadata: Annotated[
        Optional[apimachinery.ObjectMeta],
        Field(
            description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    ] = None
    status: Annotated[
        Optional[SelfSubjectReviewStatus],
        Field(description="Status is filled in by the server with the user attributes."),
    ] = None
