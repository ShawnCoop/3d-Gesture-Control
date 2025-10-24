import bpy

# Make sure there's a cube in the scene
cube = bpy.data.objects.get("Cube")

if cube:
    # Move the cube on the X, Y, Z axes
    cube.location.x += 1.0
    cube.location.y += 0.5
    cube.location.z += 0.2

    # Rotate the cube (in radians)
    cube.rotation_euler.x += 0.2
    cube.rotation_euler.y += 0.5
    cube.rotation_euler.z += 1.0

    # Scale the cube
    cube.scale.x *= 1.2
    cube.scale.y *= 0.8
    cube.scale.z *= 1.5

    print("Cube updated successfully!")
else:
    print("Cube not found in scene.")
