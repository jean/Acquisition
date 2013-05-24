"""Provide base classes for acquiring objects
"""

from ExtensionClass import Base


Acquired = "<Special Object Used to Force Acquisition>"


class Acquirer(Base):
    """
    Base class for objects that implicitly acquire attributes from containers
    """

    def __of__(self, other):
        """return the object in a context"""


class ExplicitAcquirer(Base):
    """
    Base class for objects that explicitly acquire attributes from containers
    """

    def __of__(self, other):
        """"""


class _Wrapper(Base):

    def acquire(self, *args, **kw):
        """Get an attribute, acquiring it if necessary"""

    aq_acquire = acquire  # NOQA

    def aq_inContextOf(self, *args):
        """Test whether the object is currently in the context of the argument
        """

    def __getnewargs__(self):
        """Get arguments to be passed to __new__"""
        return tuple()

    def __getstate__(self, *args):
        """Wrappers are not picklable"""
        raise TypeError("Can't pickle objects in acquisition wrappers.")

    def __reduce__(self, *args):
        """Wrappers are not picklable"""
        raise TypeError("Can't pickle objects in acquisition wrappers.")

    def __reduce_ex__(self, *args):
        """Wrappers are not picklable"""
        raise TypeError("Can't pickle objects in acquisition wrappers.")


class ExplicitAcquisitionWrapper(_Wrapper):
    """Wrapper object for implicit acquisition"""

    def __init__(self, *args, **kwargs):
        pass


class ImplicitAcquisitionWrapper(_Wrapper):
    """Wrapper object for implicit acquisition"""

    def __init__(self, *args, **kwargs):
        pass


class Explicit(ExplicitAcquirer):
    pass


class Implicit(Acquirer):
    pass


def aq_acquire(ob, name, filter=None, extra=None, explicit=None):
    """Get an attribute, acquiring it if necessary"""


def aq_get(ob, name, default=None):
    """Get an attribute, acquiring it if necessary."""


def aq_base(ob):
    """Get the object unwrapped"""


def aq_parent(ob):
    """Get the parent of an object"""


def aq_self(ob):
    """Get the object with the outermost wrapper removed"""


def aq_inner(ob):
    """Get the object with all but the innermost wrapper removed"""


def aq_chain(ob, containment=None):
    """Get a list of objects in the acquisition environment"""


def aq_inContextOf(base, ob, inner=None):
    """Determine whether the object is in the acquisition context of base."""
