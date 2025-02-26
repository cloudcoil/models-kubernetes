# Generated by cloudcoil-model-codegen v0.5.6
# DO NOT EDIT

from __future__ import annotations

from typing import (
    Annotated,
    Callable,
    Dict,
    List,
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
    ListBuilderContext,
    Never,
    Self,
)
from cloudcoil.resources import Resource, ResourceList


class CertificateSigningRequestSpec(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["CertificateSigningRequestSpec"]:
            return CertificateSigningRequestSpec

        def build(self) -> "CertificateSigningRequestSpec":
            return CertificateSigningRequestSpec(**self._attrs)

        def expiration_seconds(self, value: Optional[int], /) -> Self:
            """
            expirationSeconds is the requested duration of validity of the issued certificate. The certificate signer may issue a certificate with a different validity duration so a client must check the delta between the notBefore and and notAfter fields in the issued certificate to determine the actual duration.

            The v1.22+ in-tree implementations of the well-known Kubernetes signers will honor this field as long as the requested duration is not greater than the maximum duration they will honor per the --cluster-signing-duration CLI flag to the Kubernetes controller manager.

            Certificate signers may not honor this field for various reasons:

              1. Old signer that is unaware of the field (such as the in-tree
                 implementations prior to v1.22)
              2. Signer whose configured maximum is shorter than the requested duration
              3. Signer whose configured minimum is longer than the requested duration

            The minimum valid value for expirationSeconds is 600, i.e. 10 minutes.
            """
            return self._set("expiration_seconds", value)

        def extra(self, value: Optional[Dict[str, List[str]]], /) -> Self:
            """
            extra contains extra attributes of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable.
            """
            return self._set("extra", value)

        def groups(self, value: Optional[List[str]], /) -> Self:
            """
            groups contains group membership of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable.
            """
            return self._set("groups", value)

        def request(self, value: str, /) -> Self:
            """
            request contains an x509 certificate signing request encoded in a "CERTIFICATE REQUEST" PEM block. When serialized as JSON or YAML, the data is additionally base64-encoded.
            """
            return self._set("request", value)

        def signer_name(self, value: str, /) -> Self:
            """
            signerName indicates the requested signer, and is a qualified name.

            List/watch requests for CertificateSigningRequests can filter on this field using a "spec.signerName=NAME" fieldSelector.

            Well-known Kubernetes signers are:
             1. "kubernetes.io/kube-apiserver-client": issues client certificates that can be used to authenticate to kube-apiserver.
              Requests for this signer are never auto-approved by kube-controller-manager, can be issued by the "csrsigning" controller in kube-controller-manager.
             2. "kubernetes.io/kube-apiserver-client-kubelet": issues client certificates that kubelets use to authenticate to kube-apiserver.
              Requests for this signer can be auto-approved by the "csrapproving" controller in kube-controller-manager, and can be issued by the "csrsigning" controller in kube-controller-manager.
             3. "kubernetes.io/kubelet-serving" issues serving certificates that kubelets use to serve TLS endpoints, which kube-apiserver can connect to securely.
              Requests for this signer are never auto-approved by kube-controller-manager, and can be issued by the "csrsigning" controller in kube-controller-manager.

            More details are available at https://k8s.io/docs/reference/access-authn-authz/certificate-signing-requests/#kubernetes-signers

            Custom signerNames can also be specified. The signer defines:
             1. Trust distribution: how trust (CA bundles) are distributed.
             2. Permitted subjects: and behavior when a disallowed subject is requested.
             3. Required, permitted, or forbidden x509 extensions in the request (including whether subjectAltNames are allowed, which types, restrictions on allowed values) and behavior when a disallowed extension is requested.
             4. Required, permitted, or forbidden key usages / extended key usages.
             5. Expiration/certificate lifetime: whether it is fixed by the signer, configurable by the admin.
             6. Whether or not requests for CA certificates are allowed.
            """
            return self._set("signer_name", value)

        def uid(self, value: Optional[str], /) -> Self:
            """
            uid contains the uid of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable.
            """
            return self._set("uid", value)

        def usages(self, value: Optional[List[str]], /) -> Self:
            """
            usages specifies a set of key usages requested in the issued certificate.

            Requests for TLS client certificates typically request: "digital signature", "key encipherment", "client auth".

            Requests for TLS serving certificates typically request: "key encipherment", "digital signature", "server auth".

            Valid values are:
             "signing", "digital signature", "content commitment",
             "key encipherment", "key agreement", "data encipherment",
             "cert sign", "crl sign", "encipher only", "decipher only", "any",
             "server auth", "client auth",
             "code signing", "email protection", "s/mime",
             "ipsec end system", "ipsec tunnel", "ipsec user",
             "timestamping", "ocsp signing", "microsoft sgc", "netscape sgc"
            """
            return self._set("usages", value)

        def username(self, value: Optional[str], /) -> Self:
            """
            username contains the name of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable.
            """
            return self._set("username", value)

    class BuilderContext(BuilderContextBase["CertificateSigningRequestSpec.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = CertificateSigningRequestSpec.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for CertificateSigningRequestSpec."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["CertificateSigningRequestSpec", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use CertificateSigningRequestSpec.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    expiration_seconds: Annotated[Optional[int], Field(alias="expirationSeconds")] = None
    """
    expirationSeconds is the requested duration of validity of the issued certificate. The certificate signer may issue a certificate with a different validity duration so a client must check the delta between the notBefore and and notAfter fields in the issued certificate to determine the actual duration.

    The v1.22+ in-tree implementations of the well-known Kubernetes signers will honor this field as long as the requested duration is not greater than the maximum duration they will honor per the --cluster-signing-duration CLI flag to the Kubernetes controller manager.

    Certificate signers may not honor this field for various reasons:

      1. Old signer that is unaware of the field (such as the in-tree
         implementations prior to v1.22)
      2. Signer whose configured maximum is shorter than the requested duration
      3. Signer whose configured minimum is longer than the requested duration

    The minimum valid value for expirationSeconds is 600, i.e. 10 minutes.
    """
    extra: Optional[Dict[str, List[str]]] = None
    """
    extra contains extra attributes of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable.
    """
    groups: Optional[List[str]] = None
    """
    groups contains group membership of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable.
    """
    request: str
    """
    request contains an x509 certificate signing request encoded in a "CERTIFICATE REQUEST" PEM block. When serialized as JSON or YAML, the data is additionally base64-encoded.
    """
    signer_name: Annotated[str, Field(alias="signerName")]
    """
    signerName indicates the requested signer, and is a qualified name.

    List/watch requests for CertificateSigningRequests can filter on this field using a "spec.signerName=NAME" fieldSelector.

    Well-known Kubernetes signers are:
     1. "kubernetes.io/kube-apiserver-client": issues client certificates that can be used to authenticate to kube-apiserver.
      Requests for this signer are never auto-approved by kube-controller-manager, can be issued by the "csrsigning" controller in kube-controller-manager.
     2. "kubernetes.io/kube-apiserver-client-kubelet": issues client certificates that kubelets use to authenticate to kube-apiserver.
      Requests for this signer can be auto-approved by the "csrapproving" controller in kube-controller-manager, and can be issued by the "csrsigning" controller in kube-controller-manager.
     3. "kubernetes.io/kubelet-serving" issues serving certificates that kubelets use to serve TLS endpoints, which kube-apiserver can connect to securely.
      Requests for this signer are never auto-approved by kube-controller-manager, and can be issued by the "csrsigning" controller in kube-controller-manager.

    More details are available at https://k8s.io/docs/reference/access-authn-authz/certificate-signing-requests/#kubernetes-signers

    Custom signerNames can also be specified. The signer defines:
     1. Trust distribution: how trust (CA bundles) are distributed.
     2. Permitted subjects: and behavior when a disallowed subject is requested.
     3. Required, permitted, or forbidden x509 extensions in the request (including whether subjectAltNames are allowed, which types, restrictions on allowed values) and behavior when a disallowed extension is requested.
     4. Required, permitted, or forbidden key usages / extended key usages.
     5. Expiration/certificate lifetime: whether it is fixed by the signer, configurable by the admin.
     6. Whether or not requests for CA certificates are allowed.
    """
    uid: Optional[str] = None
    """
    uid contains the uid of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable.
    """
    usages: Optional[List[str]] = None
    """
    usages specifies a set of key usages requested in the issued certificate.

    Requests for TLS client certificates typically request: "digital signature", "key encipherment", "client auth".

    Requests for TLS serving certificates typically request: "key encipherment", "digital signature", "server auth".

    Valid values are:
     "signing", "digital signature", "content commitment",
     "key encipherment", "key agreement", "data encipherment",
     "cert sign", "crl sign", "encipher only", "decipher only", "any",
     "server auth", "client auth",
     "code signing", "email protection", "s/mime",
     "ipsec end system", "ipsec tunnel", "ipsec user",
     "timestamping", "ocsp signing", "microsoft sgc", "netscape sgc"
    """
    username: Optional[str] = None
    """
    username contains the name of the user that created the CertificateSigningRequest. Populated by the API server on creation and immutable.
    """


class CertificateSigningRequestCondition(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["CertificateSigningRequestCondition"]:
            return CertificateSigningRequestCondition

        def build(self) -> "CertificateSigningRequestCondition":
            return CertificateSigningRequestCondition(**self._attrs)

        @overload
        def last_transition_time(
            self, value_or_callback: Optional[apimachinery.Time], /
        ) -> "CertificateSigningRequestCondition.Builder": ...

        @overload
        def last_transition_time(
            self,
            value_or_callback: Callable[
                [apimachinery.Time.Builder],
                apimachinery.Time.Builder | apimachinery.Time,
            ],
            /,
        ) -> "CertificateSigningRequestCondition.Builder": ...

        @overload
        def last_transition_time(
            self, value_or_callback: Never = ...
        ) -> "apimachinery.Time.BuilderContext": ...

        def last_transition_time(self, value_or_callback=None, /):
            """
            lastTransitionTime is the time the condition last transitioned from one status to another. If unset, when a new condition type is added or an existing condition's status is changed, the server defaults this to the current time.
            """
            if self._in_context and value_or_callback is None:
                context = apimachinery.Time.BuilderContext()
                context._parent_builder = self
                context._field_name = "last_transition_time"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(apimachinery.Time.builder())
                if isinstance(output, apimachinery.Time.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("last_transition_time", value)

        @overload
        def last_update_time(
            self, value_or_callback: Optional[apimachinery.Time], /
        ) -> "CertificateSigningRequestCondition.Builder": ...

        @overload
        def last_update_time(
            self,
            value_or_callback: Callable[
                [apimachinery.Time.Builder],
                apimachinery.Time.Builder | apimachinery.Time,
            ],
            /,
        ) -> "CertificateSigningRequestCondition.Builder": ...

        @overload
        def last_update_time(
            self, value_or_callback: Never = ...
        ) -> "apimachinery.Time.BuilderContext": ...

        def last_update_time(self, value_or_callback=None, /):
            """
            lastUpdateTime is the time of the last update to this condition
            """
            if self._in_context and value_or_callback is None:
                context = apimachinery.Time.BuilderContext()
                context._parent_builder = self
                context._field_name = "last_update_time"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(apimachinery.Time.builder())
                if isinstance(output, apimachinery.Time.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("last_update_time", value)

        def message(self, value: Optional[str], /) -> Self:
            """
            message contains a human readable message with details about the request state
            """
            return self._set("message", value)

        def reason(self, value: Optional[str], /) -> Self:
            """
            reason indicates a brief reason for the request state
            """
            return self._set("reason", value)

        def status(self, value: str, /) -> Self:
            """
            status of the condition, one of True, False, Unknown. Approved, Denied, and Failed conditions may not be "False" or "Unknown".
            """
            return self._set("status", value)

        def type(self, value: str, /) -> Self:
            """
            type of the condition. Known conditions are "Approved", "Denied", and "Failed".

            An "Approved" condition is added via the /approval subresource, indicating the request was approved and should be issued by the signer.

            A "Denied" condition is added via the /approval subresource, indicating the request was denied and should not be issued by the signer.

            A "Failed" condition is added via the /status subresource, indicating the signer failed to issue the certificate.

            Approved and Denied conditions are mutually exclusive. Approved, Denied, and Failed conditions cannot be removed once added.

            Only one condition of a given type is allowed.
            """
            return self._set("type", value)

    class BuilderContext(BuilderContextBase["CertificateSigningRequestCondition.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = CertificateSigningRequestCondition.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for CertificateSigningRequestCondition."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["CertificateSigningRequestCondition", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use CertificateSigningRequestCondition.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    last_transition_time: Annotated[
        Optional[apimachinery.Time], Field(alias="lastTransitionTime")
    ] = None
    """
    lastTransitionTime is the time the condition last transitioned from one status to another. If unset, when a new condition type is added or an existing condition's status is changed, the server defaults this to the current time.
    """
    last_update_time: Annotated[Optional[apimachinery.Time], Field(alias="lastUpdateTime")] = None
    """
    lastUpdateTime is the time of the last update to this condition
    """
    message: Optional[str] = None
    """
    message contains a human readable message with details about the request state
    """
    reason: Optional[str] = None
    """
    reason indicates a brief reason for the request state
    """
    status: str
    """
    status of the condition, one of True, False, Unknown. Approved, Denied, and Failed conditions may not be "False" or "Unknown".
    """
    type: str
    """
    type of the condition. Known conditions are "Approved", "Denied", and "Failed".

    An "Approved" condition is added via the /approval subresource, indicating the request was approved and should be issued by the signer.

    A "Denied" condition is added via the /approval subresource, indicating the request was denied and should not be issued by the signer.

    A "Failed" condition is added via the /status subresource, indicating the signer failed to issue the certificate.

    Approved and Denied conditions are mutually exclusive. Approved, Denied, and Failed conditions cannot be removed once added.

    Only one condition of a given type is allowed.
    """


class CertificateSigningRequestStatus(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["CertificateSigningRequestStatus"]:
            return CertificateSigningRequestStatus

        def build(self) -> "CertificateSigningRequestStatus":
            return CertificateSigningRequestStatus(**self._attrs)

        def certificate(self, value: Optional[str], /) -> Self:
            """
            certificate is populated with an issued certificate by the signer after an Approved condition is present. This field is set via the /status subresource. Once populated, this field is immutable.

            If the certificate signing request is denied, a condition of type "Denied" is added and this field remains empty. If the signer cannot issue the certificate, a condition of type "Failed" is added and this field remains empty.

            Validation requirements:
             1. certificate must contain one or more PEM blocks.
             2. All PEM blocks must have the "CERTIFICATE" label, contain no headers, and the encoded data
              must be a BER-encoded ASN.1 Certificate structure as described in section 4 of RFC5280.
             3. Non-PEM content may appear before or after the "CERTIFICATE" PEM blocks and is unvalidated,
              to allow for explanatory text as described in section 5.2 of RFC7468.

            If more than one PEM block is present, and the definition of the requested spec.signerName does not indicate otherwise, the first block is the issued certificate, and subsequent blocks should be treated as intermediate certificates and presented in TLS handshakes.

            The certificate is encoded in PEM format.

            When serialized as JSON or YAML, the data is additionally base64-encoded, so it consists of:

                base64(
                -----BEGIN CERTIFICATE-----
                ...
                -----END CERTIFICATE-----
                )
            """
            return self._set("certificate", value)

        @overload
        def conditions(
            self, value_or_callback: List[CertificateSigningRequestCondition], /
        ) -> "CertificateSigningRequestStatus.Builder": ...

        @overload
        def conditions(
            self,
            value_or_callback: Callable[
                [
                    GenericListBuilder[
                        CertificateSigningRequestCondition,
                        CertificateSigningRequestCondition.Builder,
                    ]
                ],
                GenericListBuilder[
                    CertificateSigningRequestCondition,
                    CertificateSigningRequestCondition.Builder,
                ]
                | List[CertificateSigningRequestCondition],
            ],
            /,
        ) -> "CertificateSigningRequestStatus.Builder": ...

        @overload
        def conditions(
            self, value_or_callback: Never = ...
        ) -> ListBuilderContext[CertificateSigningRequestCondition.Builder]: ...

        def conditions(self, value_or_callback=None, /):
            """
            conditions applied to the request. Known conditions are "Approved", "Denied", and "Failed".
            """
            if self._in_context and value_or_callback is None:
                context = ListBuilderContext[CertificateSigningRequestCondition.Builder]()
                context._parent_builder = self
                context._field_name = "conditions"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(CertificateSigningRequestCondition.list_builder())
                if isinstance(output, GenericListBuilder):
                    value = output.build()
                else:
                    value = output
            return self._set("conditions", value)

    class BuilderContext(BuilderContextBase["CertificateSigningRequestStatus.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = CertificateSigningRequestStatus.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for CertificateSigningRequestStatus."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["CertificateSigningRequestStatus", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use CertificateSigningRequestStatus.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    certificate: Optional[str] = None
    """
    certificate is populated with an issued certificate by the signer after an Approved condition is present. This field is set via the /status subresource. Once populated, this field is immutable.

    If the certificate signing request is denied, a condition of type "Denied" is added and this field remains empty. If the signer cannot issue the certificate, a condition of type "Failed" is added and this field remains empty.

    Validation requirements:
     1. certificate must contain one or more PEM blocks.
     2. All PEM blocks must have the "CERTIFICATE" label, contain no headers, and the encoded data
      must be a BER-encoded ASN.1 Certificate structure as described in section 4 of RFC5280.
     3. Non-PEM content may appear before or after the "CERTIFICATE" PEM blocks and is unvalidated,
      to allow for explanatory text as described in section 5.2 of RFC7468.

    If more than one PEM block is present, and the definition of the requested spec.signerName does not indicate otherwise, the first block is the issued certificate, and subsequent blocks should be treated as intermediate certificates and presented in TLS handshakes.

    The certificate is encoded in PEM format.

    When serialized as JSON or YAML, the data is additionally base64-encoded, so it consists of:

        base64(
        -----BEGIN CERTIFICATE-----
        ...
        -----END CERTIFICATE-----
        )
    """
    conditions: Optional[List[CertificateSigningRequestCondition]] = None
    """
    conditions applied to the request. Known conditions are "Approved", "Denied", and "Failed".
    """


class CertificateSigningRequest(Resource):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["CertificateSigningRequest"]:
            return CertificateSigningRequest

        def build(self) -> "CertificateSigningRequest":
            return CertificateSigningRequest(**self._attrs)

        def api_version(self, value: Optional[Literal["certificates.k8s.io/v1"]], /) -> Self:
            """
            APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
            """
            return self._set("api_version", value)

        def kind(self, value: Optional[Literal["CertificateSigningRequest"]], /) -> Self:
            """
            Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
            """
            return self._set("kind", value)

        @overload
        def metadata(
            self, value_or_callback: Optional[apimachinery.ObjectMeta], /
        ) -> "CertificateSigningRequest.Builder": ...

        @overload
        def metadata(
            self,
            value_or_callback: Callable[
                [apimachinery.ObjectMeta.Builder],
                apimachinery.ObjectMeta.Builder | apimachinery.ObjectMeta,
            ],
            /,
        ) -> "CertificateSigningRequest.Builder": ...

        @overload
        def metadata(
            self, value_or_callback: Never = ...
        ) -> "apimachinery.ObjectMeta.BuilderContext": ...

        def metadata(self, value_or_callback=None, /):
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
            self, value_or_callback: CertificateSigningRequestSpec, /
        ) -> "CertificateSigningRequest.Builder": ...

        @overload
        def spec(
            self,
            value_or_callback: Callable[
                [CertificateSigningRequestSpec.Builder],
                CertificateSigningRequestSpec.Builder | CertificateSigningRequestSpec,
            ],
            /,
        ) -> "CertificateSigningRequest.Builder": ...

        @overload
        def spec(
            self, value_or_callback: Never = ...
        ) -> "CertificateSigningRequestSpec.BuilderContext": ...

        def spec(self, value_or_callback=None, /):
            """
            spec contains the certificate request, and is immutable after creation. Only the request, signerName, expirationSeconds, and usages fields can be set on creation. Other fields are derived by Kubernetes and cannot be modified by users.
            """
            if self._in_context and value_or_callback is None:
                context = CertificateSigningRequestSpec.BuilderContext()
                context._parent_builder = self
                context._field_name = "spec"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(CertificateSigningRequestSpec.builder())
                if isinstance(output, CertificateSigningRequestSpec.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("spec", value)

        @overload
        def status(
            self, value_or_callback: Optional[CertificateSigningRequestStatus], /
        ) -> "CertificateSigningRequest.Builder": ...

        @overload
        def status(
            self,
            value_or_callback: Callable[
                [CertificateSigningRequestStatus.Builder],
                CertificateSigningRequestStatus.Builder | CertificateSigningRequestStatus,
            ],
            /,
        ) -> "CertificateSigningRequest.Builder": ...

        @overload
        def status(
            self, value_or_callback: Never = ...
        ) -> "CertificateSigningRequestStatus.BuilderContext": ...

        def status(self, value_or_callback=None, /):
            """
            status contains information about whether the request is approved or denied, and the certificate issued by the signer, or the failure condition indicating signer failure.
            """
            if self._in_context and value_or_callback is None:
                context = CertificateSigningRequestStatus.BuilderContext()
                context._parent_builder = self
                context._field_name = "status"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(CertificateSigningRequestStatus.builder())
                if isinstance(output, CertificateSigningRequestStatus.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("status", value)

    class BuilderContext(BuilderContextBase["CertificateSigningRequest.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = CertificateSigningRequest.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for CertificateSigningRequest."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["CertificateSigningRequest", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use CertificateSigningRequest.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    api_version: Annotated[
        Optional[Literal["certificates.k8s.io/v1"]], Field(alias="apiVersion")
    ] = "certificates.k8s.io/v1"
    """
    APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: Optional[Literal["CertificateSigningRequest"]] = "CertificateSigningRequest"
    """
    Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: Optional[apimachinery.ObjectMeta] = None
    spec: CertificateSigningRequestSpec
    """
    spec contains the certificate request, and is immutable after creation. Only the request, signerName, expirationSeconds, and usages fields can be set on creation. Other fields are derived by Kubernetes and cannot be modified by users.
    """
    status: Optional[CertificateSigningRequestStatus] = None
    """
    status contains information about whether the request is approved or denied, and the certificate issued by the signer, or the failure condition indicating signer failure.
    """


CertificateSigningRequestList = ResourceList["CertificateSigningRequest"]
