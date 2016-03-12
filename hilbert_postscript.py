import bpy
from mathutils import Vector

cube_add = bpy.ops.mesh.primitive_cube_add
resize = bpy.ops.transform.resize
stopien = 3
frame_size = 0.02

def abs(x):
    if x > 0:
        return x
    else:
        return -x

def line(position, dir):
    position += (dir/2)
    cube_add(location = (position.x, position.y, position.z))
    resize(value = (frame_size+abs(dir.x)/2, frame_size+abs(dir.y)/2, frame_size+abs(dir.z)/2))
    position += (dir/2)
    return position
    
def hilbert(position, dir, v1, v2, s):
    if s == 0:
        return position
    position = hilbert(position, v1, dir, v2, s-1)
    position = line(position, v1)
    position = hilbert(position, v2, dir, v1, s-1)
    position = line(position, v2)
    position = hilbert(position, v2, dir, v1, s-1)
    position = line(position, -v1)
    position = hilbert(position, dir, -v1, -v2, s-1)
    position = line(position, dir)
    position = hilbert(position, dir, -v1, -v2, s-1)
    position = line(position, v1)
    position = hilbert(position, -v2, -dir, v1, s-1)
    position = line(position, -v2) 
    position = hilbert(position, -v2, -dir, v1, s-1)
    position = line(position, -v1)
    position = hilbert(position, -v1, -dir, v2, s-1)
    print('\n')
    return position

resize(value = (0.1 , 0.1, 0.1))
hilbert(2^stopien - 1, Vector((0, 1, 0)), Vector((0, 0, 1)), Vector((1, 0, 0)), stopien)  
