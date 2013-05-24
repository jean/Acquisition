import os

from zope.interface import classImplements

from Acquisition.interfaces import IAcquirer
from Acquisition.interfaces import IAcquisitionWrapper


if not 'PURE_PYTHON' in os.environ:  # pragma no cover
    try:
        from Acquisition._Acquisition import *  # NOQA
    except ImportError:
        from Acquisition.acquisition import *  # NOQA


classImplements(Explicit, IAcquirer)
classImplements(ExplicitAcquisitionWrapper, IAcquisitionWrapper)
classImplements(Implicit, IAcquirer)
classImplements(ImplicitAcquisitionWrapper, IAcquisitionWrapper)
