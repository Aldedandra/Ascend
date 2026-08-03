"""Ascend curriculum content package.

This package keeps the public import contract stable:
    from app.content import ACHIEVEMENTS, MODULES
"""

from .achievements import ACHIEVEMENTS
from .modules import MODULES

__all__ = ["ACHIEVEMENTS", "MODULES"]
