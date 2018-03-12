import os
from talkie.compiler import TalkieCompiler
from talkie.generator.platforms import PYTHON
from talkie.utils import get_root_path


def test_interface_inheritance():
    path = os.path.join(get_root_path(), "tests", "examples",
                        "interface_inheritance.tl")
    compiler = TalkieCompiler(PYTHON, path, None)
    compiler.compile()