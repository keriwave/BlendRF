from enum import Enum

import bpy
from bpy.props import IntProperty, BoolProperty, FloatProperty, PointerProperty, StringProperty


try:
    from . import tensorfconnect
except ModuleNotFoundError:
    pass