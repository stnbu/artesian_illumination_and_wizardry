import math, os, svgwrite

scale = 300
NEW_ORIGIN = scale, scale

def C(x, y):
    dx, dy = NEW_ORIGIN
    return dx + x, dy - y

frame = svgwrite.Drawing("foo2.svg", profile="tiny")

for i in range(0, 20):
    t = scale - ((scale/10) * i)
    frame.add(frame.line(start=C(-scale, t), end=C(scale, t), stroke='lightgrey', stroke_width=1))
    frame.add(frame.line(start=C(t, scale), end=C(t, -scale), stroke='lightgrey', stroke_width=1))

frame.add(frame.line(start=C(-scale, 0), end=C(scale, 0), stroke='red', stroke_width=1))
frame.add(frame.line(start=C(0, scale), end=C(0, -scale), stroke='red', stroke_width=1))

frame.save()
