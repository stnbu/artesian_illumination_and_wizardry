import svgwrite, webbrowser, math, os
from sympy import Matrix

ROTATE = 0
SCALE = 1
TRANSLATE = 2

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
            dx, dy = rotated_about_x - about_x, rotated_about_y - about_y
            for point in points:
                x, y = r * Matrix(point)
                yield int(x - dx), int(y - dy)
        elif transform['type'] == SCALE:
            factor = transform["factor"]
            about_x, about_y = transform["about"]
            s = Matrix(
                [
                    [factor, 0,      0],
                    [0,      factor, 0],
                    [0,      0,      1],
                ]
            )
            rotated_about_x, rotated_about_y, _ = s * Matrix([about_x, about_y, 1])
            dx, dy = rotated_about_x - about_x, rotated_about_y - about_y
            for point in points:
                x, y, _ = s * Matrix(list(point) + [1])
                yield int(x - dx), int(y - dy)
        elif transform['type'] == TRANSLATE:
            dx, dy = transform['delta']
            for x, y in points:
                yield int(x + dx), int(y + dy)
        else:
            raise ValueError("Unknown transform type %s" % transform['type'])



if __name__ == "__main__":

    import sys
    num_cases = 3
    selection = None

    def help():
        print("Choose a testcase in [0, %d]" % (num_cases - 1), file=sys.stderr)
        sys.exit(1)

    if len(sys.argv) > 1:
        try:
            selection = int(sys.argv[1])
        except:
            help()

    if selection == 0:
        points = [(0, 0), (10, 0), (10, 10), (0, 10)]
        frame = svgwrite.Drawing("foo.svg", profile="tiny")
        p = transform(
            points,
            [
                dict(
                    type=SCALE,
                    about=[5, 5],
                    factor=2,
                )
            ]
        )
        frame.add(frame.polygon(p, fill="blue"))
        frame.save()

    elif selection == 1:
        points = [(0, 0), (50, 0), (50, 50), (0, 50)]
        frame = svgwrite.Drawing("foo.svg", profile="tiny")
        p = transform(
            points,
            [
                dict(
                    type=ROTATE,
                    angle=math.pi / 4,
                    about=[50, 50])
            ]
        )
        frame.add(frame.polygon(p, fill="blue"))
        frame.save()
    elif selection == 2:
        points = [(0, 0), (10, 0), (10, 10), (0, 10)]
        frame = svgwrite.Drawing("foo.svg", profile="tiny")
        frame.add(frame.polygon(points, fill="green"))
        p = transform(
            points,
            [
                dict(
                    type=TRANSLATE, delta=[30, 30])
            ]
        )
        frame.add(frame.polygon(p, fill="blue"))
        frame.save()
    else:
        help()
