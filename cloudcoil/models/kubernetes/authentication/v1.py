# Generated by cloudcoil-model-codegen v0.0.17
# DO NOT EDIT

from __future__ import annotations

from typing import Annotated, Dict, List, Literal, Optional

from pydantic import Field

from cloudcoil import apimachinery
from cloudcoil._pydantic import BaseModel
from cloudcoil.resources import Resource


class BoundObjectReference(BaseModel):
    api_version: Annotated[
        Optional[str],
        Field(alias="apiVersion", description="API version of the referent."),
    ] = None
    kind: Annotated[
        Optional[str],
        Field(description="Kind of the referent. Valid kinds are 'Pod' and 'Secret'."),
    ] = None
    name: Annotated[Optional[str], Field(description="Name of the referent.")] = None
    uid: Annotated[Optional[str], Field(description="UID of the referent.")] = None


class TokenRequestSpec(BaseModel):
    audiences: Annotated[
        List[str],
        Field(
            description="Audiences are the intendend audiences of the token. A recipient of a token must identify themself with an identifier in the list of audiences of the token, and otherwise should reject the token. A token issued for multiple audiences may be used to authenticate against any of the audiences listed but implies a high degree of trust between the target audiences."
        ),
    ]
    bound_object_ref: Annotated[
        Optional[BoundObjectReference],
        Field(
            alias="boundObjectRef",
            description="BoundObjectRef is a reference to an object that the token will be bound to. The token will only be valid for as long as the bound object exists. NOTE: The API server's TokenReview endpoint will validate the BoundObjectRef, but other audiences may not. Keep ExpirationSeconds small if you want prompt revocation.",
        ),
    ] = None
    expiration_seconds: Annotated[
        Optional[int],
        Field(
            alias="expirationSeconds",
            description="ExpirationSeconds is the requested duration of validity of the request. The token issuer may return a token with a different validity duration so a client needs to check the 'expiration' field in a response.",
        ),
    ] = None


class TokenReviewSpec(BaseModel):
    audiences: Annotated[
        Optional[List[str]],
        Field(
            description="Audiences is a list of the identifiers that the resource server presented with the token identifies as. Audience-aware token authenticators will verify that the token was intended for at least one of the audiences in this list. If no audiences are provided, the audience will default to the audience of the Kubernetes apiserver."
        ),
    ] = None
    token: Annotated[Optional[str], Field(description="Token is the opaque bearer token.")] = None


class UserInfo(BaseModel):
    extra: Annotated[
        Optional[Dict[str, List[str]]],
        Field(description="Any additional information provided by the authenticator."),
    ] = None
    groups: Annotated[
        Optional[List[str]],
        Field(description="The names of groups this user is a part of."),
    ] = None
    uid: Annotated[
        Optional[str],
        Field(
            description="A unique value that identifies this user across time. If this user is deleted and another user by the same name is added, they will have different UIDs."
        ),
    ] = None
    username: Annotated[
        Optional[str],
        Field(description="The name that uniquely identifies this user among all active users."),
    ] = None


class SelfSubjectReviewStatus(BaseModel):
    user_info: Annotated[
        Optional[UserInfo],
        Field(
            alias="userInfo",
            description="User attributes of the user making this request.",
        ),
    ] = None


class TokenRequestStatus(BaseModel):
    expiration_timestamp: Annotated[
        apimachinery.Time,
        Field(
            alias="expirationTimestamp",
            description="ExpirationTimestamp is the time of expiration of the returned token.",
        ),
    ]
    token: Annotated[str, Field(description="Token is the opaque bearer token.")]


class TokenReviewStatus(BaseModel):
    audiences: Annotated[
        Optional[List[str]],
        Field(
            description='Audiences are audience identifiers chosen by the authenticator that are compatible with both the TokenReview and token. An identifier is any identifier in the intersection of the TokenReviewSpec audiences and the token\'s audiences. A client of the TokenReview API that sets the spec.audiences field should validate that a compatible audience identifier is returned in the status.audiences field to ensure that the TokenReview server is audience aware. If a TokenReview returns an empty status.audience field where status.authenticated is "true", the token is valid against the audience of the Kubernetes API server.'
        ),
    ] = None
    authenticated: Annotated[
        Optional[bool],
        Field(
            description="Authenticated indicates that the token was associated with a known user."
        ),
    ] = None
    error: Annotated[
        Optional[str],
        Field(description="Error indicates that the token couldn't be checked"),
    ] = None
    user: Annotated[
        Optional[UserInfo],
        Field(description="User is the UserInfo associated with the provided token."),
    ] = None


class SelfSubjectReview(Resource):
    api_version: Annotated[
        Optional[Literal["authentication.k8s.io/v1"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "authentication.k8s.io/v1"
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


class TokenRequest(Resource):
    api_version: Annotated[
        Optional[Literal["authentication.k8s.io/v1"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "authentication.k8s.io/v1"
    kind: Annotated[
        Optional[Literal["TokenRequest"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "TokenRequest"
    metadata: Annotated[
        Optional[apimachinery.ObjectMeta],
        Field(
            description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    ] = None
    spec: Annotated[
        TokenRequestSpec,
        Field(description="Spec holds information about the request being evaluated"),
    ]
    status: Annotated[
        Optional[TokenRequestStatus],
        Field(
            description="Status is filled in by the server and indicates whether the token can be authenticated."
        ),
    ] = None


class TokenReview(Resource):
    api_version: Annotated[
        Optional[Literal["authentication.k8s.io/v1"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "authentication.k8s.io/v1"
    kind: Annotated[
        Optional[Literal["TokenReview"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "TokenReview"
    metadata: Annotated[
        Optional[apimachinery.ObjectMeta],
        Field(
            description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"
        ),
    ] = None
    spec: Annotated[
        TokenReviewSpec,
        Field(description="Spec holds information about the request being evaluated"),
    ]
    status: Annotated[
        Optional[TokenReviewStatus],
        Field(
            description="Status is filled in by the server and indicates whether the request can be authenticated."
        ),
    ] = None
