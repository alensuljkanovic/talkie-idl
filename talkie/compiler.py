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

        events = set()
        for func in interface.functions:
            self._analyse_function(func)
            events.update(self._get_fsa_events_from_function(func))
        print("Events: {}".format(events))

    def _get_fsa_events_from_function(self, func):
        """
        Returns the list of events for the FSA derived from the function name
        
        For each function name, following events are generated:
        1. <function_name> (same as function name)
        2. <function_name>_ok (used for cases where function call succeeded)
        3. <function_name>_failed (used for cases where function call failed)
        Args:
            func: 

        Returns:
            iterable
        """
        return {func.name, "%s_ok", "%s_failed"}

    def _analyse_function(self, func):
        """Performs analysis on the given Function object."""
        print("\tAnalysing function: %s" % func.name)

        # TODO Calculate the return type (if needed)
        pass

    def analyse_fsa(self, fsa):
        pass

    def compile(self):
        print("Compiling to %s... " % self._target)
        print("%s -> %s" % (self._src_path, self._dest_path))
        print("PACKAGE: %s" % self._package)

        interfaces = [i for i in self._package.items
                      if isinstance(i, Interface)]
        for interface in interfaces:
            self._analyse_interface(interface)
