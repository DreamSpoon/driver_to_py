# test init

bl_info = {
    "name": "Driver to Python",
    "description": "Create text-block of Python code to re-create drivers of objects. Currently supports some " \
        "drivers, more support will be added when possible.",
    "author": "Dave",
    "version": (0, 0, 2),
    "blender": (2, 80, 0),
    "location": "3DView -> Tools -> Drv2Py",
    "category": "Drivers, Python",
    "wiki_url": "",
}

import bpy
from numpy import ones as np_ones
from bpy.props import (BoolProperty, BoolVectorProperty, IntProperty)
from bpy.types import Panel

from .drv_to import (get_animdata_bool_names, DRV2PY_DriversToPython, DRV2PY_SelectAllAnimdataSrc,
    DRV2PY_SelectNoneAnimdataSrc)

ANIMDATA_BOOL_NAMES = get_animdata_bool_names()

class DRV2PY_PT_CreatePyText(bpy.types.Panel):
    bl_label = "Drivers to Python"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Drv2Py"

    def draw(self, context):
        layout = self.layout
        scn = context.scene

        box = layout.box()
        box.label(text="Driver Data Source")
        box.operator("drv2py.drivers_to_python")
        box.prop(scn, "D2P_NumSpacePad")
        box.prop(scn, "D2P_MakeFunction")
        box.operator("drv2py.select_all_animdata_src")
        box.operator("drv2py.select_none_animdata_src")
        box = box.box()
        for i in range(len(ANIMDATA_BOOL_NAMES)):
            box.prop(scn, "D2P_AnimdataBoolVec", index=i, text=ANIMDATA_BOOL_NAMES[i])

classes = [
    DRV2PY_PT_CreatePyText,
    DRV2PY_DriversToPython,
    DRV2PY_SelectAllAnimdataSrc,
    DRV2PY_SelectNoneAnimdataSrc,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bts = bpy.types.Scene
    bts.D2P_NumSpacePad = IntProperty(name="Num Space Pad", description="Number of spaces to prepend to each " +
        "line of code output in text-block", default=4, min=0)
    bts.D2P_MakeFunction = BoolProperty(name="Make into Function", description="Add lines of Python code to " +
        "create runnable script (instead of just the bare essential code)", default=True)

    num_names = len(ANIMDATA_BOOL_NAMES)
    bts.D2P_AnimdataBoolVec = BoolVectorProperty(size=num_names, default=tuple(np_ones((num_names), dtype=int)))

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    bts = bpy.types.Scene
    del bts.D2P_AnimdataBoolVec
    del bts.D2P_MakeFunction
    del bts.D2P_NumSpacePad

if __name__ == "__main__":
    register()
