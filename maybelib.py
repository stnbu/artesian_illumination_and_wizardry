import math, os, svgwrite
from sympy import Matrix

ROTATE = 0
SCALE = 1
TRANSLATE = 2

class tspec:

    def __init__(self, type_, **params):
        self.type = type_
        self.__dict__.update(params)

def get_transformer(transform):
    if transform.type == ROTATE:
        angle = transform.angle
        about_x, about_y = transform.about
        r = Matrix(
            [
                [math.cos(angle), -math.sin(angle)],
                [math.sin(angle),  math.cos(angle)],
            ]
        )
        rotated_about_x, rotated_about_y = r * Matrix([about_x, about_y])
        dx, dy = rotated_about_x - about_x, rotated_about_y - about_y
        def worker(points):
            for point in points:
                x, y = r * Matrix(point)
                yield int(x - dx), int(y - dy)
    elif transform.type == SCALE:
        sx, sy = transform.factor
        about_x, about_y = transform.about
        s = Matrix(
            [
                [sx,     0,      0],
                [0,      sy    , 0],
                [0,      0,      1],
            ]
        )
        rotated_about_x, rotated_about_y, _ = s * Matrix([about_x, about_y, 1])
        dx, dy = rotated_about_x - about_x, rotated_about_y - about_y
        def worker(points):
            for point in points:
                x, y, _ = s * Matrix(list(point) + [1])
                yield int(x - dx), int(y - dy)
    elif transform.type == TRANSLATE:
        dx, dy = transform.delta
        def worker(points):
            for x, y in points:
                yield int(x + dx), int(y + dy)
    else:
        raise ValueError("Unknown transform type %s" % transform.type)

    return worker


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
        transformer = get_transformer(
            tspec(
                SCALE,
                about=[5, 5],
                factor=[2, 4],
            )
        )
        frame.add(frame.polygon(transformer(points), fill="blue"))
        frame.save()
    elif selection == 1:
        points = [(0, 0), (50, 0), (50, 50), (0, 50)]
        frame = svgwrite.Drawing("foo.svg", profile="tiny")
        transformer = get_transformer(
                tspec(
                    ROTATE,
                    angle=math.pi / 4,
                    about=[50, 50])
        )
        frame.add(frame.polygon(transformer(points), fill="blue"))
        frame.save()
    elif selection == 2:
        points = [(0, 0), (10, 0), (10, 10), (0, 10)]
        frame = svgwrite.Drawing("foo.svg", profile="tiny")
        frame.add(frame.polygon(points, fill="green"))
        transformer = get_transformer(
                tspec(
                    TRANSLATE, delta=[30, 30])
        )
        frame.add(frame.polygon(transformer(points), fill="blue"))
        frame.save()
    else:
        help()
