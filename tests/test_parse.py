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


def test_interface_inheritance():
    metamodel = get_metamodel()
    path = os.path.join(get_root_path(), "tests", "examples",
                        "interface_inheritance.tl")
    metamodel.model_from_file(path)


def test_type_inheritance():
    metamodel = get_metamodel()
    path = os.path.join(get_root_path(), "tests", "examples",
                        "typedef_inheritance.tl")
    metamodel.model_from_file(path)


def test_typhoon_api():
    metamodel = get_metamodel()
    path = os.path.join(get_root_path(), "tests", "examples",
                        "typhoon_example.tl")

    metamodel.model_from_file(path)


def test_typhoon_hil_api():
    metamodel = get_metamodel()
    path = os.path.join(get_root_path(), "tests", "examples",
                        "typhoon_hil_api.tl")

    metamodel.model_from_file(path)


def test_fsa_example():
    metamodel = get_metamodel()
    path = os.path.join(get_root_path(), "tests", "examples",
                        "fsa_example.tl")

    metamodel.model_from_file(path)


def test_fsa_example2():
    metamodel = get_metamodel()
    path = os.path.join(get_root_path(), "tests", "examples",
                        "fsa_example2.tl")

    metamodel.model_from_file(path)
