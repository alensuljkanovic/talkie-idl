import os
from textx.metamodel import metamodel_from_file
from talkie.model import Package, Interface, Function, FunctionParameter
from talkie.utils import get_root_path

_classes = (Package, Interface, Function, FunctionParameter)
# _obj_processors = {"Interface": interface_processor}


def get_metamodel():
    """
    Returns metamodel of FreeMindMap.
    """
    global _metamodel

    path = os.path.join(get_root_path(), "talkie", "lang", "talkie.tx")
    _metamodel = metamodel_from_file(path)
    # _metamodel.register_obj_processors(_obj_processors)

    return _metamodel