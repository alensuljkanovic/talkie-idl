"""
Tests simple example.
"""
import os
from talkie.lang.meta import get_metamodel
from talkie.utils import get_root_path


def test_complex_types():
    metamodel = get_metamodel()
    path = os.path.join(get_root_path(), "tests", "examples",
                        "complex_types.tl")
    metamodel.model_from_file(path)


def test_typhoon_api():
    metamodel = get_metamodel()
    path = os.path.join(get_root_path(), "tests", "examples",
                        "typhoon_example.tl")

    metamodel.model_from_file(path)

