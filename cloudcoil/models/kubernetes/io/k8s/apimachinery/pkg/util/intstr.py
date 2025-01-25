# Generated by cloudcoil-model-codegen v0.2.2
# DO NOT EDIT

from __future__ import annotations

from typing import Union, cast

from pydantic import RootModel

from cloudcoil.pydantic import (
    BaseBuilder,
    BuilderContextBase,
    Self,
)


class IntOrString(RootModel[Union[int, str]]):
    class Builder(BaseBuilder):
        _value: Union[int, str] | None = None

        def root(self, value: Union[int, str], /) -> Self:
            """
            IntOrString is a type that can hold an int32 or a string.  When used in JSON or YAML marshalling and unmarshalling, it produces or consumes the inner type.  This allows you to have, for example, a JSON field that can accept a name or number.
            """
            self._value = value
            return self

        def __call__(self, value: Union[int, str], /) -> Self:
            """
            IntOrString is a type that can hold an int32 or a string.  When used in JSON or YAML marshalling and unmarshalling, it produces or consumes the inner type.  This allows you to have, for example, a JSON field that can accept a name or number.
            """
            self._value = value
            return self

        def build(self) -> "IntOrString":
            value = cast(Union[int, str], self._value)
            return IntOrString(value)

    root: Union[int, str]
    """
    IntOrString is a type that can hold an int32 or a string.  When used in JSON or YAML marshalling and unmarshalling, it produces or consumes the inner type.  This allows you to have, for example, a JSON field that can accept a name or number.
    """

    class BuilderContext(BuilderContextBase["IntOrString.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = IntOrString.Builder()
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for IntOrString."""
        return cls.BuilderContext()
