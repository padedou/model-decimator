import bpy

# Clear the default scene

bpy.data.objects['Camera'].select = True
bpy.data.objects['Cube'].select = True
bpy.data.objects['Lamp'].select = True


bpy.ops.object.delete()