import math

def point_circle_position(cx, cy, r, px, py):
    distance = math.sqrt((px - cx)*2 + (py - cy)*2)
    if distance < r:
        return "inside the circle"
    elif distance == r:
        return "on the circle"
    else:
        return "outside the circle"

cx, cy = map(float, input("Enter center of the circle (cx cy): ").split())
r = float(input("Enter radius of the circle: "))
px, py = map(float, input("Enter coordinates of the point (px py): ").split())

position = point_circle_position(cx, cy, r, px, py)
print(f"The point is {position}.")
