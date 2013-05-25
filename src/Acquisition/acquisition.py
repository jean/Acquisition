"""Provide base classes for acquiring objects
"""

import sys

from ExtensionClass import Base

if sys.version_info >= (3, ):
    unicode = str

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

    def __init__(self, *args, **kwargs):
        if kwargs:
            raise TypeError("keyword arguments not allowed")
        if len(args) != 2:
            raise TypeError(
                "__init__() takes exactly 2 arguments (%s given)" % len(args))
        obj, container = args
        if self == obj:
            raise ValueError(
                "Cannot wrap acquisition wrapper in itself (Wrapper__init__)")
        Base.__setattr__(self, 'obj', obj)
        if container is not None:
            Base.__setattr__(self, 'container', container)

    def __setattr__(self, k, v):
        if k in ('aq_parent', '__parent__'):
            Base.__setattr__(self, 'container', v)
            return
        if self.obj:
            while v and _isWrapper(v):
                v = v.obj
            if v:
                Base.__setattr__(self.obj, k, v)
            else:
                Base.__delattr__(self.obj, k)
        else:
            raise AttributeError(
                "Attempt to set attribute on empty acquisition wrapper")

    def __repr__(self):
        r = getattr(self, '__repr__', None)
        if r is not None:
            return r()
        else:
            return repr(self.obj)

    def __str__(self):
        r = getattr(self, '__str__', None)
        if r is not None:
            return r()
        else:
            return str(self.obj)

    def __unicode__(self):
        r = getattr(self, '__unicode__', None)
        if r is not None:
            return r()
        else:
            return unicode(self.obj)

    def __call__(self, *args, **kw):
        return _CallMethodO(self, '__call__', *args, **kw)

    def __len__(self):
        r = getattr(self, '__len__', None)
        if r is None:
            return -1
        return r()

    def __hash__(self):
        return hash(self.obj)

    def __nonzero__(self, *args, **kw):
        raise NotImplementedError('TODO')

    __bool__ = __nonzero__

    def __cmp__(self, other):
        raise NotImplementedError('TODO')

    def __eq__(self, other):
        raise NotImplementedError('TODO')

    def __ne__(self, other):
        raise NotImplementedError('TODO')

    def __lt__(self, other):
        raise NotImplementedError('TODO')

    def __le__(self, other):
        raise NotImplementedError('TODO')

    def __gt__(self, other):
        raise NotImplementedError('TODO')

    def __ge__(self, other):
        raise NotImplementedError('TODO')

    def __add__(self, *args, **kw):
        return _CallMethodO(self, '__add__', *args, **kw)

    def __sub__(self, *args, **kw):
        return _CallMethodO(self, '__sub__', *args, **kw)

    def __mul__(self, *args, **kw):
        return _CallMethodO(self, '__mul__', *args, **kw)

    def __div__(self, *args, **kw):
        return _CallMethodO(self, '__div__', *args, **kw)

    def __mod__(self, *args, **kw):
        return _CallMethodO(self, '__mod__', *args, **kw)

    def __divmod__(self, *args, **kw):
        return _CallMethodO(self, '__divmod__', *args, **kw)

    def __pow__(self, *args, **kw):
        return _CallMethodO(self, '__pow__', *args, **kw)

    def __neg__(self, *args, **kw):
        return _CallMethodO(self, '__neg__', *args, **kw)

    def __pos__(self, *args, **kw):
        return _CallMethodO(self, '__pos__', *args, **kw)

    def __abs__(self, *args, **kw):
        return _CallMethodO(self, '__abs__', *args, **kw)

    def __invert__(self, *args, **kw):
        return _CallMethodO(self, '__invert__', *args, **kw)

    def __lshift__(self, *args, **kw):
        return _CallMethodO(self, '__lshift__', *args, **kw)

    def __rshift__(self, *args, **kw):
        return _CallMethodO(self, '__rshift__', *args, **kw)

    def __and__(self, *args, **kw):
        return _CallMethodO(self, '__and__', *args, **kw)

    def __or__(self, *args, **kw):
        return _CallMethodO(self, '__or__', *args, **kw)

    def __xor__(self, *args, **kw):
        return _CallMethodO(self, '__xor__', *args, **kw)

    def __coerce__(self, *args, **kw):
        raise NotImplementedError('TODO')

    def __int__(self, *args, **kw):
        return _CallMethodO(self, '__int__', *args, **kw)

    def __long__(self, *args, **kw):
        return _CallMethodO(self, '__long__', *args, **kw)

    def __float__(self, *args, **kw):
        return _CallMethodO(self, '__float__', *args, **kw)

    def __oct__(self, *args, **kw):
        return _CallMethodO(self, '__oct__', *args, **kw)

    def __hex__(self, *args, **kw):
        return _CallMethodO(self, '__hex__', *args, **kw)

    def __getitem__(self, *args, **kw):
        return _CallMethodO(self, '__getitem__', *args, **kw)

    def __setitem__(self, *args, **kw):
        return _CallMethodO(self, '__setitem__', *args, **kw)

    def __delitem__(self, *args, **kw):
        return _CallMethodO(self, '__delitem__', *args, **kw)

    def __getslice__(self, *args, **kw):
        return _CallMethodO(self, '__getslice__', *args, **kw)

    def __setslice__(self, *args, **kw):
        return _CallMethodO(self, '__setslice__', *args, **kw)

    def __delslice__(self, *args, **kw):
        return _CallMethodO(self, '__delslice__', *args, **kw)

    def __contains__(self, *args, **kw):
        return bool(_CallMethodO(self, '__contains__', *args, **kw))

    def __iter__(self):
        raise NotImplementedError('TODO')

    def acquire(self, *args, **kw):
        """Get an attribute, acquiring it if necessary"""
        raise NotImplementedError()

    aq_acquire = acquire  # NOQA

    def aq_inContextOf(self, *args):
        """Test whether the object is currently in the context of the argument
        """
        raise NotImplementedError()

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


def _CallMethodO(self, name, *args, **kw):
    if not args:
        return None
    r = getattr(self, name, None)
    if r is None:
        return None
    return r(*args, **kw)


def _isWrapper(ob):
    return isinstance(ob, _Wrapper)


class ExplicitAcquisitionWrapper(_Wrapper):
    """Wrapper object for implicit acquisition"""


class ImplicitAcquisitionWrapper(_Wrapper):
    """Wrapper object for implicit acquisition"""


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
