from os.path import join as _join
from os.path import dirname as _dirname

with open(_join(_dirname(__file__), 'VERSION')) as _f:
    __version__ = _f.read().strip()

from .server import model_server  # noqa: F401
from .client import BSONModel  # noqa: F401
from .client import BSONAttack  # noqa: F401