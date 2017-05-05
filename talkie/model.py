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
    def __init__(self, name, parent=None, functions=None):
        """Initializes Interface object."""
        super(Interface, self).__init__(parent)
        self.name = name
        self.functions = functions if functions else []


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
    def __init__(self, parent, p_name, p_type, p_modifier, default=None):
        super(FunctionParameter, self).__init__(parent)
        self.p_name = p_name
        self.p_modifier = p_modifier
        self.p_type = p_type
        self.default = default
