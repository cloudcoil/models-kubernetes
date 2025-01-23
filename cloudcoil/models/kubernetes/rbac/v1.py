# Generated by cloudcoil-model-codegen v0.1.1
# DO NOT EDIT

from __future__ import annotations

from typing import Annotated, Callable, List, Literal, Optional, Type, Union

from pydantic import Field

from cloudcoil import apimachinery
from cloudcoil.pydantic import BaseBuilder, BaseModel, ListBuilder, Self
from cloudcoil.resources import Resource, ResourceList


class PolicyRule(BaseModel):
    class Builder(BaseBuilder):
        def build(self) -> "PolicyRule":
            return PolicyRule(**self._attrs)

        def api_groups(self, value: Optional[List[str]]) -> Self:
            return self._set("api_groups", value)

        def non_resource_ur_ls(self, value: Optional[List[str]]) -> Self:
            return self._set("non_resource_ur_ls", value)

        def resource_names(self, value: Optional[List[str]]) -> Self:
            return self._set("resource_names", value)

        def resources(self, value: Optional[List[str]]) -> Self:
            return self._set("resources", value)

        def verbs(self, value: List[str]) -> Self:
            return self._set("verbs", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def list_builder(cls) -> ListBuilder[Self]:
        return ListBuilder[cls]()  # type: ignore[valid-type]

    api_groups: Annotated[
        Optional[List[str]],
        Field(
            alias="apiGroups",
            description='APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed. "" represents the core API group and "*" represents all API groups.',
        ),
    ] = None
    non_resource_ur_ls: Annotated[
        Optional[List[str]],
        Field(
            alias="nonResourceURLs",
            description='NonResourceURLs is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path Since non-resource URLs are not namespaced, this field is only applicable for ClusterRoles referenced from a ClusterRoleBinding. Rules can either apply to API resources (such as "pods" or "secrets") or non-resource URL paths (such as "/api"),  but not both.',
        ),
    ] = None
    resource_names: Annotated[
        Optional[List[str]],
        Field(
            alias="resourceNames",
            description="ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed.",
        ),
    ] = None
    resources: Annotated[
        Optional[List[str]],
        Field(
            description="Resources is a list of resources this rule applies to. '*' represents all resources."
        ),
    ] = None
    verbs: Annotated[
        List[str],
        Field(
            description="Verbs is a list of Verbs that apply to ALL the ResourceKinds contained in this rule. '*' represents all verbs."
        ),
    ]


class RoleRef(BaseModel):
    class Builder(BaseBuilder):
        def build(self) -> "RoleRef":
            return RoleRef(**self._attrs)

        def api_group(self, value: str) -> Self:
            return self._set("api_group", value)

        def kind(self, value: str) -> Self:
            return self._set("kind", value)

        def name(self, value: str) -> Self:
            return self._set("name", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def list_builder(cls) -> ListBuilder[Self]:
        return ListBuilder[cls]()  # type: ignore[valid-type]

    api_group: Annotated[
        str,
        Field(
            alias="apiGroup",
            description="APIGroup is the group for the resource being referenced",
        ),
    ]
    kind: Annotated[str, Field(description="Kind is the type of resource being referenced")]
    name: Annotated[str, Field(description="Name is the name of resource being referenced")]


class Subject(BaseModel):
    class Builder(BaseBuilder):
        def build(self) -> "Subject":
            return Subject(**self._attrs)

        def api_group(self, value: Optional[str]) -> Self:
            return self._set("api_group", value)

        def kind(self, value: str) -> Self:
            return self._set("kind", value)

        def name(self, value: str) -> Self:
            return self._set("name", value)

        def namespace(self, value: Optional[str]) -> Self:
            return self._set("namespace", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def list_builder(cls) -> ListBuilder[Self]:
        return ListBuilder[cls]()  # type: ignore[valid-type]

    api_group: Annotated[
        Optional[str],
        Field(
            alias="apiGroup",
            description='APIGroup holds the API group of the referenced subject. Defaults to "" for ServiceAccount subjects. Defaults to "rbac.authorization.k8s.io" for User and Group subjects.',
        ),
    ] = None
    kind: Annotated[
        str,
        Field(
            description='Kind of object being referenced. Values defined by this API group are "User", "Group", and "ServiceAccount". If the Authorizer does not recognized the kind value, the Authorizer should report an error.'
        ),
    ]
    name: Annotated[str, Field(description="Name of the object being referenced.")]
    namespace: Annotated[
        Optional[str],
        Field(
            description='Namespace of the referenced object.  If the object kind is non-namespace, such as "User" or "Group", and this value is not empty the Authorizer should report an error.'
        ),
    ] = None


class AggregationRule(BaseModel):
    class Builder(BaseBuilder):
        def build(self) -> "AggregationRule":
            return AggregationRule(**self._attrs)

        def cluster_role_selectors(
            self,
            value_or_callback: Union[
                Optional[List[apimachinery.LabelSelector]],
                Callable[[Type[apimachinery.LabelSelector]], List[apimachinery.LabelSelector]],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(apimachinery.LabelSelector)
            return self._set("cluster_role_selectors", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def list_builder(cls) -> ListBuilder[Self]:
        return ListBuilder[cls]()  # type: ignore[valid-type]

    cluster_role_selectors: Annotated[
        Optional[List[apimachinery.LabelSelector]],
        Field(
            alias="clusterRoleSelectors",
            description="ClusterRoleSelectors holds a list of selectors which will be used to find ClusterRoles and create the rules. If any of the selectors match, then the ClusterRole's permissions will be added",
        ),
    ] = None


class ClusterRole(Resource):
    class Builder(BaseBuilder):
        def build(self) -> "ClusterRole":
            return ClusterRole(**self._attrs)

        def aggregation_rule(
            self,
            value_or_callback: Union[
                Optional[AggregationRule],
                Callable[[Type[AggregationRule]], AggregationRule],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(AggregationRule)
            return self._set("aggregation_rule", value)

        def api_version(self, value: Optional[Literal["rbac.authorization.k8s.io/v1"]]) -> Self:
            return self._set("api_version", value)

        def kind(self, value: Optional[Literal["ClusterRole"]]) -> Self:
            return self._set("kind", value)

        def metadata(
            self,
            value_or_callback: Union[
                Optional[apimachinery.ObjectMeta],
                Callable[[Type[apimachinery.ObjectMeta]], apimachinery.ObjectMeta],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(apimachinery.ObjectMeta)
            return self._set("metadata", value)

        def rules(
            self,
            value_or_callback: Union[
                Optional[List[PolicyRule]],
                Callable[[Type[PolicyRule]], List[PolicyRule]],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(PolicyRule)
            return self._set("rules", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def list_builder(cls) -> ListBuilder[Self]:
        return ListBuilder[cls]()  # type: ignore[valid-type]

    aggregation_rule: Annotated[
        Optional[AggregationRule],
        Field(
            alias="aggregationRule",
            description="AggregationRule is an optional field that describes how to build the Rules for this ClusterRole. If AggregationRule is set, then the Rules are controller managed and direct changes to Rules will be stomped by the controller.",
        ),
    ] = None
    api_version: Annotated[
        Optional[Literal["rbac.authorization.k8s.io/v1"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "rbac.authorization.k8s.io/v1"
    kind: Annotated[
        Optional[Literal["ClusterRole"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "ClusterRole"
    metadata: Annotated[
        Optional[apimachinery.ObjectMeta],
        Field(description="Standard object's metadata."),
    ] = None
    rules: Annotated[
        Optional[List[PolicyRule]],
        Field(description="Rules holds all the PolicyRules for this ClusterRole"),
    ] = None


class ClusterRoleBinding(Resource):
    class Builder(BaseBuilder):
        def build(self) -> "ClusterRoleBinding":
            return ClusterRoleBinding(**self._attrs)

        def api_version(self, value: Optional[Literal["rbac.authorization.k8s.io/v1"]]) -> Self:
            return self._set("api_version", value)

        def kind(self, value: Optional[Literal["ClusterRoleBinding"]]) -> Self:
            return self._set("kind", value)

        def metadata(
            self,
            value_or_callback: Union[
                Optional[apimachinery.ObjectMeta],
                Callable[[Type[apimachinery.ObjectMeta]], apimachinery.ObjectMeta],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(apimachinery.ObjectMeta)
            return self._set("metadata", value)

        def role_ref(
            self, value_or_callback: Union[RoleRef, Callable[[Type[RoleRef]], RoleRef]]
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(RoleRef)
            return self._set("role_ref", value)

        def subjects(
            self,
            value_or_callback: Union[
                Optional[List[Subject]], Callable[[Type[Subject]], List[Subject]]
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(Subject)
            return self._set("subjects", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def list_builder(cls) -> ListBuilder[Self]:
        return ListBuilder[cls]()  # type: ignore[valid-type]

    api_version: Annotated[
        Optional[Literal["rbac.authorization.k8s.io/v1"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "rbac.authorization.k8s.io/v1"
    kind: Annotated[
        Optional[Literal["ClusterRoleBinding"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "ClusterRoleBinding"
    metadata: Annotated[
        Optional[apimachinery.ObjectMeta],
        Field(description="Standard object's metadata."),
    ] = None
    role_ref: Annotated[
        RoleRef,
        Field(
            alias="roleRef",
            description="RoleRef can only reference a ClusterRole in the global namespace. If the RoleRef cannot be resolved, the Authorizer must return an error. This field is immutable.",
        ),
    ]
    subjects: Annotated[
        Optional[List[Subject]],
        Field(description="Subjects holds references to the objects the role applies to."),
    ] = None


ClusterRoleBindingList = ResourceList["ClusterRoleBinding"]


ClusterRoleList = ResourceList["ClusterRole"]


class Role(Resource):
    class Builder(BaseBuilder):
        def build(self) -> "Role":
            return Role(**self._attrs)

        def api_version(self, value: Optional[Literal["rbac.authorization.k8s.io/v1"]]) -> Self:
            return self._set("api_version", value)

        def kind(self, value: Optional[Literal["Role"]]) -> Self:
            return self._set("kind", value)

        def metadata(
            self,
            value_or_callback: Union[
                Optional[apimachinery.ObjectMeta],
                Callable[[Type[apimachinery.ObjectMeta]], apimachinery.ObjectMeta],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(apimachinery.ObjectMeta)
            return self._set("metadata", value)

        def rules(
            self,
            value_or_callback: Union[
                Optional[List[PolicyRule]],
                Callable[[Type[PolicyRule]], List[PolicyRule]],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(PolicyRule)
            return self._set("rules", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def list_builder(cls) -> ListBuilder[Self]:
        return ListBuilder[cls]()  # type: ignore[valid-type]

    api_version: Annotated[
        Optional[Literal["rbac.authorization.k8s.io/v1"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "rbac.authorization.k8s.io/v1"
    kind: Annotated[
        Optional[Literal["Role"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "Role"
    metadata: Annotated[
        Optional[apimachinery.ObjectMeta],
        Field(description="Standard object's metadata."),
    ] = None
    rules: Annotated[
        Optional[List[PolicyRule]],
        Field(description="Rules holds all the PolicyRules for this Role"),
    ] = None


class RoleBinding(Resource):
    class Builder(BaseBuilder):
        def build(self) -> "RoleBinding":
            return RoleBinding(**self._attrs)

        def api_version(self, value: Optional[Literal["rbac.authorization.k8s.io/v1"]]) -> Self:
            return self._set("api_version", value)

        def kind(self, value: Optional[Literal["RoleBinding"]]) -> Self:
            return self._set("kind", value)

        def metadata(
            self,
            value_or_callback: Union[
                Optional[apimachinery.ObjectMeta],
                Callable[[Type[apimachinery.ObjectMeta]], apimachinery.ObjectMeta],
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(apimachinery.ObjectMeta)
            return self._set("metadata", value)

        def role_ref(
            self, value_or_callback: Union[RoleRef, Callable[[Type[RoleRef]], RoleRef]]
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(RoleRef)
            return self._set("role_ref", value)

        def subjects(
            self,
            value_or_callback: Union[
                Optional[List[Subject]], Callable[[Type[Subject]], List[Subject]]
            ],
        ) -> Self:
            value = value_or_callback
            if callable(value_or_callback):
                value = value_or_callback(Subject)
            return self._set("subjects", value)

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def list_builder(cls) -> ListBuilder[Self]:
        return ListBuilder[cls]()  # type: ignore[valid-type]

    api_version: Annotated[
        Optional[Literal["rbac.authorization.k8s.io/v1"]],
        Field(
            alias="apiVersion",
            description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources",
        ),
    ] = "rbac.authorization.k8s.io/v1"
    kind: Annotated[
        Optional[Literal["RoleBinding"]],
        Field(
            description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"
        ),
    ] = "RoleBinding"
    metadata: Annotated[
        Optional[apimachinery.ObjectMeta],
        Field(description="Standard object's metadata."),
    ] = None
    role_ref: Annotated[
        RoleRef,
        Field(
            alias="roleRef",
            description="RoleRef can reference a Role in the current namespace or a ClusterRole in the global namespace. If the RoleRef cannot be resolved, the Authorizer must return an error. This field is immutable.",
        ),
    ]
    subjects: Annotated[
        Optional[List[Subject]],
        Field(description="Subjects holds references to the objects the role applies to."),
    ] = None


RoleBindingList = ResourceList["RoleBinding"]


RoleList = ResourceList["Role"]
