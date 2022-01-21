from collections.abc import Mapping

from bot.base import ConnectableObject

from bpyutils.util.imports import import_or_raise

class Camera(ConnectableObject):
    """
    High-Level Camera Object.
    """
    def __init__(self, module = None):
        if module:
            package = module
            name    = package

            if isinstance(module, Mapping):
                package = module["package"]
                name    = module.get("name", package)
                
            self._module = import_or_raise(package, name = name)

        self._capture = None

    @property
    def module(self):
        return getattr(self, "_module", None)

    # TODO: Check Error
    # @property.setter
    # def module(self, value):
    #     self._module = import_or_raise(value)

    @property
    def connected(self):
        attr = getattr(self, "_capture", None)

        if attr:
            return True
        
        return False

    def snap(self):
        raise NotImplementedError