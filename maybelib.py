import svgwrite, webbrowser, math, os
from sympy import Matrix

def get_rotate_matrix(angle):
    return Matrix(
        [
            [math.cos(angle), -math.sin(angle)],
            [math.sin(angle), math.cos(angle)],
        ]
    )

points = [(0, 0), (50, 0), (50, 50), (0, 50)]

num_frames = 90
total_angle = math.pi / 4
angle_delta = num_frames / num_frames
delta_rotate_matrix = get_rotate_matrix(angle_delta)

# frame = svgwrite.Drawing("foo.svg", profile="tiny")
# frame.add(frame.polygon(points, fill="blue"))
# frame.save()

def new_points(r):
    for point in points:
        x, y = r * Matrix(point)
        yield int(x), int(y)

r = get_rotate_matrix(math.pi / 4)

frame = svgwrite.Drawing("foo.svg", profile="tiny")
frame.add(frame.polygon(new_points(r), fill="blue"))
frame.save()

if __name__ == "__main__":
    pass
