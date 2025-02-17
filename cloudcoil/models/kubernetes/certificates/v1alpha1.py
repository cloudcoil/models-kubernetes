# Generated by cloudcoil-model-codegen v0.5.5
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


class ClusterTrustBundleSpec(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["ClusterTrustBundleSpec"]:
            return ClusterTrustBundleSpec

        def build(self) -> "ClusterTrustBundleSpec":
            return ClusterTrustBundleSpec(**self._attrs)

        def signer_name(self, value: Optional[str], /) -> Self:
            """
            signerName indicates the associated signer, if any.

            In order to create or update a ClusterTrustBundle that sets signerName, you must have the following cluster-scoped permission: group=certificates.k8s.io resource=signers resourceName=<the signer name> verb=attest.

            If signerName is not empty, then the ClusterTrustBundle object must be named with the signer name as a prefix (translating slashes to colons). For example, for the signer name `example.com/foo`, valid ClusterTrustBundle object names include `example.com:foo:abc` and `example.com:foo:v1`.

            If signerName is empty, then the ClusterTrustBundle object's name must not have such a prefix.

            List/watch requests for ClusterTrustBundles can filter on this field using a `spec.signerName=NAME` field selector.
            """
            return self._set("signer_name", value)

        def trust_bundle(self, value: str, /) -> Self:
            """
            trustBundle contains the individual X.509 trust anchors for this bundle, as PEM bundle of PEM-wrapped, DER-formatted X.509 certificates.

            The data must consist only of PEM certificate blocks that parse as valid X.509 certificates.  Each certificate must include a basic constraints extension with the CA bit set.  The API server will reject objects that contain duplicate certificates, or that use PEM block headers.

            Users of ClusterTrustBundles, including Kubelet, are free to reorder and deduplicate certificate blocks in this file according to their own logic, as well as to drop PEM block headers and inter-block data.
            """
            return self._set("trust_bundle", value)

    class BuilderContext(BuilderContextBase["ClusterTrustBundleSpec.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = ClusterTrustBundleSpec.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for ClusterTrustBundleSpec."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["ClusterTrustBundleSpec", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use ClusterTrustBundleSpec.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    signer_name: Annotated[Optional[str], Field(alias="signerName")] = None
    """
    signerName indicates the associated signer, if any.

    In order to create or update a ClusterTrustBundle that sets signerName, you must have the following cluster-scoped permission: group=certificates.k8s.io resource=signers resourceName=<the signer name> verb=attest.

    If signerName is not empty, then the ClusterTrustBundle object must be named with the signer name as a prefix (translating slashes to colons). For example, for the signer name `example.com/foo`, valid ClusterTrustBundle object names include `example.com:foo:abc` and `example.com:foo:v1`.

    If signerName is empty, then the ClusterTrustBundle object's name must not have such a prefix.

    List/watch requests for ClusterTrustBundles can filter on this field using a `spec.signerName=NAME` field selector.
    """
    trust_bundle: Annotated[str, Field(alias="trustBundle")]
    """
    trustBundle contains the individual X.509 trust anchors for this bundle, as PEM bundle of PEM-wrapped, DER-formatted X.509 certificates.

    The data must consist only of PEM certificate blocks that parse as valid X.509 certificates.  Each certificate must include a basic constraints extension with the CA bit set.  The API server will reject objects that contain duplicate certificates, or that use PEM block headers.

    Users of ClusterTrustBundles, including Kubelet, are free to reorder and deduplicate certificate blocks in this file according to their own logic, as well as to drop PEM block headers and inter-block data.
    """


class ClusterTrustBundle(Resource):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["ClusterTrustBundle"]:
            return ClusterTrustBundle

        def build(self) -> "ClusterTrustBundle":
            return ClusterTrustBundle(**self._attrs)

        def api_version(self, value: Optional[Literal["certificates.k8s.io/v1alpha1"]], /) -> Self:
            """
            APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
            """
            return self._set("api_version", value)

        def kind(self, value: Optional[Literal["ClusterTrustBundle"]], /) -> Self:
            """
            Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
            """
            return self._set("kind", value)

        @overload
        def metadata(
            self, value_or_callback: Optional[apimachinery.ObjectMeta], /
        ) -> "ClusterTrustBundle.Builder": ...

        @overload
        def metadata(
            self,
            value_or_callback: Callable[
                [apimachinery.ObjectMeta.Builder],
                apimachinery.ObjectMeta.Builder | apimachinery.ObjectMeta,
            ],
            /,
        ) -> "ClusterTrustBundle.Builder": ...

        @overload
        def metadata(
            self, value_or_callback: Never = ...
        ) -> "apimachinery.ObjectMeta.BuilderContext": ...

        def metadata(self, value_or_callback=None, /):
            """
            metadata contains the object metadata.
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
        def spec(
            self, value_or_callback: ClusterTrustBundleSpec, /
        ) -> "ClusterTrustBundle.Builder": ...

        @overload
        def spec(
            self,
            value_or_callback: Callable[
                [ClusterTrustBundleSpec.Builder],
                ClusterTrustBundleSpec.Builder | ClusterTrustBundleSpec,
            ],
            /,
        ) -> "ClusterTrustBundle.Builder": ...

        @overload
        def spec(
            self, value_or_callback: Never = ...
        ) -> "ClusterTrustBundleSpec.BuilderContext": ...

        def spec(self, value_or_callback=None, /):
            """
            spec contains the signer (if any) and trust anchors.
            """
            if self._in_context and value_or_callback is None:
                context = ClusterTrustBundleSpec.BuilderContext()
                context._parent_builder = self
                context._field_name = "spec"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(ClusterTrustBundleSpec.builder())
                if isinstance(output, ClusterTrustBundleSpec.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("spec", value)

    class BuilderContext(BuilderContextBase["ClusterTrustBundle.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = ClusterTrustBundle.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for ClusterTrustBundle."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["ClusterTrustBundle", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use ClusterTrustBundle.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    api_version: Annotated[
        Optional[Literal["certificates.k8s.io/v1alpha1"]], Field(alias="apiVersion")
    ] = "certificates.k8s.io/v1alpha1"
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: Optional[Literal["ClusterTrustBundle"]] = "ClusterTrustBundle"
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: Optional[apimachinery.ObjectMeta] = None
    """
    metadata contains the object metadata.
    """
    spec: ClusterTrustBundleSpec
    """
    spec contains the signer (if any) and trust anchors.
    """


ClusterTrustBundleList = ResourceList["ClusterTrustBundle"]
