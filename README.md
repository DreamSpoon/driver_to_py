# Drivers to Py addon for Blender 2.8+

## Summary
Blender addon to convert Drivers to Python code.

## Usage
Buttons/options for using this addon are found in the 3D-View window, the Tools panel (to the right side of 3D-View window), Drv2Py tab.
Use the checkbox list of different places of driver data to filter out unwanted drivers, if needed.
Press the "Drivers to Py" button to make Python code, output to a Textblock in the Text-Editor, name starts with "driver_to.py"

### Code Output
Output code can be found in Blender's builtin Text Editor, the name starts with "driver_to.py".

Python code that is output can be run immediately, because current names of objects/materials/nodes/etc. are incorporated into the code.
In other words, *objects/materials/nodes/etc. must already exist for the output code to work*.
The output code quickly captures the current state of drivers in the current .blend file, which includes:
- driver type (e.g. scripted)
- 'use_self' flag
- expression strings
- variables
  - in the output code, other things in the .blend file are given with references starting with "bpy.data."

This code can, and should, be modifed as needed.
For example, "bpy.data." references are used in the output code, along with names of materials/objects/etc., to help identify connections between code and the material/objects/etc. available in the current .blend file.
These "bpy.data" references could/should be replaced with Python variables that reference objects/materials/etc. created in Python code.

## Sources of Driver Data
All known sources of Driver data have been included, but more research is needed.
Known sources of Driver data:
- any thing that has the 'animation_data' attribute, and the 'animation_data' attribute's value is not None
- things that have the 'animation_data' attribute are stored in the 'bpy.data' collections
  - some things in the bpy.data collections have a 'node_tree' attribute, and this 'node_tree' attribute can have the 'animation_data' attribute
  - e.g. Material type things in bpy.data.materials can have drivers (e.g. 'Use Nodes' can have drivers), and
    - ShaderNodeTree type things can have drivers (e.g. drivers attached to input values of Vector Math node)
- full list of known sources of driver data (x would be replaced with actual index number, e.g. 0 ):
  - bpy.data.armatures (Rigs, Bones)
  - bpy.data.cache_files
  - bpy.data.cameras
  - bpy.data.curves
  - bpy.data.grease_pencils
  - bpy.data.lattices
  - bpy.data.lights
  - bpy.data.lightprobes
  - bpy.data.linestyles
    - bpy.data.linestyles[x].node_tree (Linestyle Nodes)
  - bpy.data.masks
  - bpy.data.materials
    - bpy.data.materials[x].node_tree (Material Nodes)
  - bpy.data.node_groups (Geometry Nodes / custom Node Group)
  - bpy.data.shape_keys (Mesh Shapekeys)
  - bpy.data.meshes
  - bpy.data.metaballs
  - bpy.data.movieclips
  - bpy.data.objects
  - bpy.data.particles (Particle Settings)
  - bpy.data.scenes
    - bpy.data.scenes[x].node_tree (Compositor Nodes)
  - bpy.data.speakers (Audio Sources)
  - bpy.data.textures
    - bpy.data.textures[x].node_tree (Texture Nodes)
  - bpy.data.volumes
  - bpy.data.worlds (Environment)
    - bpy.data.worlds[x].node_tree (Environment Nodes)

## Also, see:
    Blender Driver
https://docs.blender.org/manual/en/latest/animation/drivers/introduction.html
    Blender Python Console
https://docs.blender.org/manual/en/latest/editors/python_console.html
