import bpy
import socket
import json

# UDP socket to receive coordinates from hand_tracking.py
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 9999))
sock.setblocking(False)  # non-blocking receive

cube = bpy.data.objects.get("Cube")

def update_cube():
    try:
        data, addr = sock.recvfrom(1024)
        coords = json.loads(data)
        # Map to Blender space (scale as needed)
        cube.location.x = coords["x"] * 5
        cube.location.y = coords["y"] * 5
        cube.location.z = coords["z"] * 5
    except:
        pass
    return 0.01  # call again in 0.01 seconds

# Register Blender timer
bpy.app.timers.register(update_cube)
