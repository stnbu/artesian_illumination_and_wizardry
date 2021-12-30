import svgwrite, webbrowser, math, os
from sympy import Matrix

ROTATE = 0
SCALE = 1

def transform(points, transforms):
    for transform in transforms:
        if transform['type'] == ROTATE:
            angle = transform["angle"]
            about_x, about_y = transform["about"]
            r = Matrix(
                [
                    [math.cos(angle), -math.sin(angle)],
                    [math.sin(angle), math.cos(angle)],
                ]
            )
            rotated_about_x, rotated_about_y = r * Matrix([about_x, about_y])
            d_x, d_y = rotated_about_x - about_x, rotated_about_y - about_y
            for point in points:
                x, y = r * Matrix(point)
                yield int(x - d_x), int(y - d_y)
        elif transform['type'] == SCALE:
            raise NotImplementedError
        else:
            raise ValueError("Unknown transform type %s" % transform['type'])



if __name__ == "__main__":
    import time
    points = [(0, 0), (50, 0), (50, 50), (0, 50)]
    for i in range(0, 50):
        frame = svgwrite.Drawing("foo.svg", profile="tiny")
        p = transform(
            points,
            [
                dict(
                    type=ROTATE,
                    angle=(math.pi / 1000)*i*2,
                    about=[50, 50])
            ]
        )
        frame.add(frame.polygon(p, fill="blue"))
        frame.add(frame.circle(center=(25, 25), r=1, fill="black"))
        frame.save()
        time.sleep(0.2)
