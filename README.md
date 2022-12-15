# Drivers to Py addon for Blender 2.8+

## Summary
Blender addon to help convert Drivers in current Blend file to Python code, which can immeditaely be run to test output Python code.

## Sources of Driver Data
All known sources of Driver data have been included, although testing is necessary to confirm this.

Known sources of Driver data:
- any thing that has the 'animation_data' attribute, where the 'animation_data' attribute's value is not None
- things that have the 'animation_data' attribute are stored in the 'bpy.data' collections
  - e.g bpy.data.cameras collection stores Camera type things
  - some things in the bpy.data collections have a 'node_tree' attribute, and this 'node_tree' attribute can have the 'animation_data' attribute
  - e.g. Material type things in bpy.data.materials can have drivers (e.g. 'Use Nodes' can have drivers)
  - e.g. ShaderNodeTree type things can have drivers (e.g. drivers attached to input values of Vector Math node)
