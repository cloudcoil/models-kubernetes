from types import ModuleType

import cloudcoil.models.kubernetes as kubernetes


def test_has_modules():
    modules = list(filter(lambda x: isinstance(x, ModuleType), kubernetes.__dict__.values()))
    assert modules, "No modules found in kubernetes"
