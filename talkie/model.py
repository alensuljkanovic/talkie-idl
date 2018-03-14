"""
This module contains the implementation of talkie IDL.
"""


class TalkieObject(object):
    """Base class for all classes used in the implementation of talkie IDL."""
    def __init__(self, parent):
        super(TalkieObject, self).__init__()
        self.parent = parent


class Package(TalkieObject):
    """Object representation of a package defined by talkie DSL."""
    def __init__(self, name, version, items=None):
        super(Package, self).__init__(None)
        self.name = name
        self.version = version
        self.items = items if items else []
        # self.typedefs = typedefs if typedefs else []
        # self.interfaces = interfaces if interfaces else []


class Interface(TalkieObject):
    """Object representation of an interface defined by talkie DSL."""
    def __init__(self, name, parent=None, inherits=None, functions=None,
                 fsa=None):
        """Initializes Interface object."""
        super(Interface, self).__init__(parent)
        self.name = name
        self.inherits = inherits if inherits else []
        self.functions = functions if functions else []

        self.fsa = fsa
        if fsa:
            self.fsa.events = self._get_events()

    def _get_events(self):
        events = set()
        for fn in self.functions:
            events.update(self._get_fsa_events_from_function(fn))
        return events

    def _get_fsa_events_from_function(self, func):
        """
        Returns the list of events for the FSA derived from the function name

        For each function name, following events are generated:
        1. <function_name>_called (used for a function call)
        2. <function_name>_ok (used for cases where function call succeeded)
        3. <function_name>_failed (used for cases where function call failed)
        Args:
            func: 

        Returns:
            iterable
        """
        return {
            "%s_called" % func.name,
            "%s_ok" % func.name,
            "%s_failed" % func.name
        }


class Function(TalkieObject):
    """Object representation of a function defined by talkie DSL."""
    def __init__(self, parent, name, params=None):
        """Initializes Interface object."""
        super(Function, self).__init__(parent)
        self.name = name
        self.params = params if params else []

    @property
    def parameters(self):
        params = ["%s %s" % (p.p_type, p.p_name) for p in self.params]
        return ", ".join(params)


class FunctionParameter(TalkieObject):
    """Object representation of a function param defined by talkie DSL."""
    def __init__(self, parent, name, type, modifier, default=None):
        super(FunctionParameter, self).__init__(parent)
        self.name = name
        self.modifier = modifier
        self.type = type
        self.default = default


class FiniteStateAutomata(TalkieObject):
    """Object representation of a Finite State Automata."""
    def __init__(self, parent, **kwargs):
        super(FiniteStateAutomata).__init__(parent)
        self.events = set()
