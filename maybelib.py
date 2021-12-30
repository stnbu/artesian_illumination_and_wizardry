import svgwrite, webbrowser, math, os
from sympy import Matrix

def transform(points, **transforms):
    rotate = transforms.pop('rotate')

    angle = rotate['angle']
    about_x, about_y = rotate['about']

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

if __name__ == "__main__":
    points = [(0, 0), (50, 0), (50, 50), (0, 50)]
    frame = svgwrite.Drawing("foo.svg", profile="tiny")
    p = transform(points,
                  rotate=dict(
                      angle=math.pi / 3,
                      about=[25, 25]
                  )
    )
    frame.add(frame.polygon(p, fill="blue"))
    frame.add(frame.circle(center=(25,25), r=1, fill="black"))
    frame.save()
