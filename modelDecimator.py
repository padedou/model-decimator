import bpy

# Clear the default scene

bpy.data.objects['Camera'].select = True
bpy.data.objects['Cube'].select = True
bpy.data.objects['Lamp'].select = True

bpy.ops.object.delete()

# Add a testing model, store it in a variable and make it active

full_path_to_file = "C:\\Users\\Paschalis\\Development\\3dModels\\stanfordBunny\\mybunnyTri.obj"
bpy.ops.import_scene.obj(filepath=full_path_to_file)
inputModel = bpy.data.objects[0]
bpy.context.scene.objects.active = inputModel

# Apply the Decimate modifier until zero ratio

step = 0.1

bpy.ops.object.modifier_add(type='DECIMATE')
decRatio = inputModel.modifiers['Decimate'].ratio
inputModel.modifiers['Decimate'].ratio = decRatio - step
decRatio = decRatio - step
bpy.ops.object.modifier_apply(apply_as='DATA', modifier='Decimate')

while (decRatio - step > 0.0):
    bpy.ops.object.modifier_add(type='DECIMATE')
    #decRatio = inputModel.modifiers['Decimate'].ratio
    inputModel.modifiers['Decimate'].ratio = decRatio - step
    decRatio = decRatio - step
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier='Decimate')
    
'''
bpy.ops.object.modifier_add(type='DECIMATE')
inputModel.modifiers['Decimate'].ratio = 0.5


bpy.ops.object.modifier_apply(apply_as='DATA', modifier='Decimate')

bpy.ops.object.modifier_add(type='DECIMATE')
inputModel.modifiers['Decimate'].ratio = 0.1
bpy.ops.object.modifier_apply(apply_as='DATA', modifier='Decimate')
'''