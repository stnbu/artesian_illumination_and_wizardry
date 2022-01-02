"""
For your help!

Cartesian   Screen
---------   ----------
(0, 0)      (500, 500)
(1, 0)      (550, 500)
(1, 1)      (550, 450)
(0, 1)      (500, 450)
"""


import math, os, svgwrite

scale = 500
NEW_ORIGIN = scale, scale

def C(x, y):
    dx, dy = NEW_ORIGIN
    return dx + x, dy - y

frame = svgwrite.Drawing("foo2.svg")

frame.defs.add(frame.style('* {font-size: 9px;}'))

lines = 20
step = lines / 2

for i in range(0, lines):
    t = scale - ((scale/step) * i)
    if t == 0:
        continue

    text_x, text_y = C(3, -11)
    frame.add(frame.line(start=C(-scale, t), end=C(scale, t), stroke='lightgrey', stroke_width=1))
    frame.add(frame.circle(C(t, 0), 1, fill='black', stroke='black'))
    frame.add(frame.text("%d" % (t//(scale/step)), x=[text_x + t], y=[text_y], fill='black'))

    frame.add(frame.line(start=C(t, scale), end=C(t, -scale), stroke='lightgrey', stroke_width=1))
    frame.add(frame.circle(C(0, t), 1, fill='black', stroke='black'))
    frame.add(frame.text("%d" % (t//(scale/step)), x=[text_x], y=[text_y + t], fill='black'))

frame.add(frame.line(start=C(-scale, 0), end=C(scale, 0), stroke='red', stroke_width=1))
frame.add(frame.line(start=C(0, scale), end=C(0, -scale), stroke='red', stroke_width=1))
frame.add(frame.circle(C(0, 0), 1, fill='black', stroke='black'))

def RC(x, y):
    return C(x * 50, y * 50)


def graph(f):
    points = []
    granularity = 1
    step = scale * granularity
    for x in range(-step, step):
        rx = x / 50 / granularity
        points.append(RC(rx, f(rx)))

    frame.add(frame.polyline(points, stroke="green", stroke_width=1))

def f(x):
    return x**2

graph(f)

frame.save()

# for x, y in [(0, 0), (1, 0), (1, 1), (0, 1)]:
#     screen_x, screen_y = RC(x, y)
#     print("(%d, %d) --> (%d, %d)" % (x, y, screen_x, screen_y))
