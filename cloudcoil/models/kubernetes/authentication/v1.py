# Generated by cloudcoil-model-codegen v0.2.0
# DO NOT EDIT

from __future__ import annotations

from typing import Annotated, Callable, Dict, List, Literal, Optional, Type, Union

from pydantic import Field

from cloudcoil import apimachinery
from cloudcoil.pydantic import BaseBuilder, BaseModel, GenericListBuilder, Self
from cloudcoil.resources import Resource


class BoundObjectReference(BaseModel):
    class Builder(BaseBuilder):
        @property
        def base_class(self) -> Type["BoundObjectReference"]:
            return BoundObjectReference

        def build(self) -> "BoundObjectReference":
            return BoundObjectReference(**self._attrs)

        def api_version(self, value: Optional[str]) -> Self:
            return self._set("api_version", value)

        def kind(self, value: Optional[str]) -> Self:
            return self._set("kind", value)

        def name(self, value: Optional[str]) -> Self:
            return self._set("name", value)

        def uid(self, value: Optional[str]) -> Self:
            return self._set("uid", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    class ListBuilder(GenericListBuilder["BoundObjectReference", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use BoundObjectReference.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

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
    class Builder(BaseBuilder):
        @property
        def base_class(self) -> Type["TokenRequestSpec"]:
            return TokenRequestSpec

        def build(self) -> "TokenRequestSpec":
            return TokenRequestSpec(**self._attrs)

        def audiences(self, value: List[str]) -> Self:
            return self._set("audiences", value)

        """  """

        def bound_object_ref(
            self,
            value_or_callback: Union[
                Optional[BoundObjectReference],
                Callable[[BoundObjectReference.Builder], BoundObjectReference.Builder],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(BoundObjectReference.builder()).build()
            return self._set("bound_object_ref", value)

        def expiration_seconds(self, value: Optional[int]) -> Self:
            return self._set("expiration_seconds", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    class ListBuilder(GenericListBuilder["TokenRequestSpec", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use TokenRequestSpec.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

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
    class Builder(BaseBuilder):
        @property
        def base_class(self) -> Type["TokenReviewSpec"]:
            return TokenReviewSpec

        def build(self) -> "TokenReviewSpec":
            return TokenReviewSpec(**self._attrs)

        def audiences(self, value: Optional[List[str]]) -> Self:
            return self._set("audiences", value)

        def token(self, value: Optional[str]) -> Self:
            return self._set("token", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    class ListBuilder(GenericListBuilder["TokenReviewSpec", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use TokenReviewSpec.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    audiences: Annotated[
        Optional[List[str]],
        Field(
            description="Audiences is a list of the identifiers that the resource server presented with the token identifies as. Audience-aware token authenticators will verify that the token was intended for at least one of the audiences in this list. If no audiences are provided, the audience will default to the audience of the Kubernetes apiserver."
        ),
    ] = None
    token: Annotated[Optional[str], Field(description="Token is the opaque bearer token.")] = None


class UserInfo(BaseModel):
    class Builder(BaseBuilder):
        @property
        def base_class(self) -> Type["UserInfo"]:
            return UserInfo

        def build(self) -> "UserInfo":
            return UserInfo(**self._attrs)

        def extra(self, value: Optional[Dict[str, List[str]]]) -> Self:
            return self._set("extra", value)

        def groups(self, value: Optional[List[str]]) -> Self:
            return self._set("groups", value)

        def uid(self, value: Optional[str]) -> Self:
            return self._set("uid", value)

        def username(self, value: Optional[str]) -> Self:
            return self._set("username", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    class ListBuilder(GenericListBuilder["UserInfo", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use UserInfo.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

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
    class Builder(BaseBuilder):
        @property
        def base_class(self) -> Type["SelfSubjectReviewStatus"]:
            return SelfSubjectReviewStatus

        def build(self) -> "SelfSubjectReviewStatus":
            return SelfSubjectReviewStatus(**self._attrs)

        """  """

        def user_info(
            self,
            value_or_callback: Union[
                Optional[UserInfo], Callable[[UserInfo.Builder], UserInfo.Builder]
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(UserInfo.builder()).build()
            return self._set("user_info", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    class ListBuilder(GenericListBuilder["SelfSubjectReviewStatus", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use SelfSubjectReviewStatus.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    user_info: Annotated[
        Optional[UserInfo],
        Field(
            alias="userInfo",
            description="User attributes of the user making this request.",
        ),
    ] = None


class TokenRequestStatus(BaseModel):
    class Builder(BaseBuilder):
        @property
        def base_class(self) -> Type["TokenRequestStatus"]:
            return TokenRequestStatus

        def build(self) -> "TokenRequestStatus":
            return TokenRequestStatus(**self._attrs)

        """  """

        def expiration_timestamp(
            self,
            value_or_callback: Union[
                apimachinery.Time,
                Callable[[apimachinery.Time.Builder], apimachinery.Time.Builder],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(apimachinery.Time.builder()).build()
            return self._set("expiration_timestamp", value)

        def token(self, value: str) -> Self:
            return self._set("token", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    class ListBuilder(GenericListBuilder["TokenRequestStatus", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use TokenRequestStatus.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    expiration_timestamp: Annotated[
        apimachinery.Time,
        Field(
            alias="expirationTimestamp",
            description="ExpirationTimestamp is the time of expiration of the returned token.",
        ),
    ]
    token: Annotated[str, Field(description="Token is the opaque bearer token.")]


class TokenReviewStatus(BaseModel):
    class Builder(BaseBuilder):
        @property
        def base_class(self) -> Type["TokenReviewStatus"]:
            return TokenReviewStatus

        def build(self) -> "TokenReviewStatus":
            return TokenReviewStatus(**self._attrs)

        def audiences(self, value: Optional[List[str]]) -> Self:
            return self._set("audiences", value)

        def authenticated(self, value: Optional[bool]) -> Self:
            return self._set("authenticated", value)

        def error(self, value: Optional[str]) -> Self:
            return self._set("error", value)

        """  """

        def user(
            self,
            value_or_callback: Union[
                Optional[UserInfo], Callable[[UserInfo.Builder], UserInfo.Builder]
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(UserInfo.builder()).build()
            return self._set("user", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    class ListBuilder(GenericListBuilder["TokenReviewStatus", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use TokenReviewStatus.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

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
    class Builder(BaseBuilder):
        @property
        def base_class(self) -> Type["SelfSubjectReview"]:
            return SelfSubjectReview

        def build(self) -> "SelfSubjectReview":
            return SelfSubjectReview(**self._attrs)

        def api_version(self, value: Optional[Literal["authentication.k8s.io/v1"]]) -> Self:
            return self._set("api_version", value)

        def kind(self, value: Optional[Literal["SelfSubjectReview"]]) -> Self:
            return self._set("kind", value)

        """  """

        def metadata(
            self,
            value_or_callback: Union[
                Optional[apimachinery.ObjectMeta],
                Callable[[apimachinery.ObjectMeta.Builder], apimachinery.ObjectMeta.Builder],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(apimachinery.ObjectMeta.builder()).build()
            return self._set("metadata", value)

        """  """

        def status(
            self,
            value_or_callback: Union[
                Optional[SelfSubjectReviewStatus],
                Callable[[SelfSubjectReviewStatus.Builder], SelfSubjectReviewStatus.Builder],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(SelfSubjectReviewStatus.builder()).build()
            return self._set("status", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    class ListBuilder(GenericListBuilder["SelfSubjectReview", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use SelfSubjectReview.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

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
    class Builder(BaseBuilder):
        @property
        def base_class(self) -> Type["TokenRequest"]:
            return TokenRequest

        def build(self) -> "TokenRequest":
            return TokenRequest(**self._attrs)

        def api_version(self, value: Optional[Literal["authentication.k8s.io/v1"]]) -> Self:
            return self._set("api_version", value)

        def kind(self, value: Optional[Literal["TokenRequest"]]) -> Self:
            return self._set("kind", value)

        """  """

        def metadata(
            self,
            value_or_callback: Union[
                Optional[apimachinery.ObjectMeta],
                Callable[[apimachinery.ObjectMeta.Builder], apimachinery.ObjectMeta.Builder],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(apimachinery.ObjectMeta.builder()).build()
            return self._set("metadata", value)

        """  """

        def spec(
            self,
            value_or_callback: Union[
                TokenRequestSpec,
                Callable[[TokenRequestSpec.Builder], TokenRequestSpec.Builder],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(TokenRequestSpec.builder()).build()
            return self._set("spec", value)

        """  """

        def status(
            self,
            value_or_callback: Union[
                Optional[TokenRequestStatus],
                Callable[[TokenRequestStatus.Builder], TokenRequestStatus.Builder],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(TokenRequestStatus.builder()).build()
            return self._set("status", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    class ListBuilder(GenericListBuilder["TokenRequest", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use TokenRequest.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

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
    class Builder(BaseBuilder):
        @property
        def base_class(self) -> Type["TokenReview"]:
            return TokenReview

        def build(self) -> "TokenReview":
            return TokenReview(**self._attrs)

        def api_version(self, value: Optional[Literal["authentication.k8s.io/v1"]]) -> Self:
            return self._set("api_version", value)

        def kind(self, value: Optional[Literal["TokenReview"]]) -> Self:
            return self._set("kind", value)

        """  """

        def metadata(
            self,
            value_or_callback: Union[
                Optional[apimachinery.ObjectMeta],
                Callable[[apimachinery.ObjectMeta.Builder], apimachinery.ObjectMeta.Builder],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(apimachinery.ObjectMeta.builder()).build()
            return self._set("metadata", value)

        """  """

        def spec(
            self,
            value_or_callback: Union[
                TokenReviewSpec,
                Callable[[TokenReviewSpec.Builder], TokenReviewSpec.Builder],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(TokenReviewSpec.builder()).build()
            return self._set("spec", value)

        """  """

        def status(
            self,
            value_or_callback: Union[
                Optional[TokenReviewStatus],
                Callable[[TokenReviewStatus.Builder], TokenReviewStatus.Builder],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(TokenReviewStatus.builder()).build()
            return self._set("status", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    class ListBuilder(GenericListBuilder["TokenReview", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use TokenReview.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

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
