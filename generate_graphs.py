import bpy
import json
import os
import random
from math import pi

with open('USE ABSOLUTE PATH') as f:
  data = json.load(f)

count = 0
for i in data:
    print(data[i])
    bpy.ops.mesh.primitive_cube_add(location=(count*4, 0 ,float(data[i])))  
    bpy.ops.transform.resize(value=(1, 1, float(data[i])))
    activeObject = bpy.context.active_object
    mat = bpy.data.materials.new(name="MaterialName")
    activeObject.data.materials.append(mat)
    bpy.context.object.active_material.diffuse_color = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1), 0) #change color
    count += 1

light_data = bpy.data.lights.new(name="my-light-data", type='SUN')
light_data.energy = 100
light_object = bpy.data.objects.new(name="my-light", object_data=light_data)
bpy.context.collection.objects.link(light_object)
light_object.location = (5, -10, 5)

camera_data = bpy.data.cameras.new(name='Camera')
camera_object = bpy.data.objects.new('Camera', camera_data)
bpy.context.scene.collection.objects.link(camera_object)
camera_object.location = (5, -35, 5)
camera_object.rotation_euler[0] = pi/2
