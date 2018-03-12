"""
This module contains Talkie compiler implementation.
"""
from talkie.lang.meta import get_metamodel
from talkie.model import Interface


class TalkieCompiler(object):
    """Talkie compiler"""

    def __init__(self, target_platform, src_path, dest_path):

        self._target = target_platform
        self._src_path = src_path
        self._dest_path = dest_path
        self._package = get_metamodel().model_from_file(src_path)

        self._namespace = {}

    def _analyse_interface(self, interface):
        """Performs the analysis on the given Interface object."""
        print("Analysing interface: %s" % interface.name)

        pfuncs = [f for p in interface.inherits for f in p.functions]
        interface.functions.extend(pfuncs)

        for func in interface.functions:
            self._analyse_function(func)

    def _analyse_function(self, func):
        """Performs analysis on the given Function object."""
        print("\tAnalysing function: %s" % func.name)

        # TODO Calculate the return type (if needed)
        pass

    def compile(self):
        print("Compiling to %s... " % self._target)
        print("%s -> %s" % (self._src_path, self._dest_path))
        print("PACKAGE: %s" % self._package)

        interfaces = [i for i in self._package.items
                      if isinstance(i, Interface)]
        for interface in interfaces:
            self._analyse_interface(interface)