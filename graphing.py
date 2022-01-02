import math, os, svgwrite

NEW_ORIGIN = 100, 100

def C(x, y):
    dx, dy = NEW_ORIGIN
    return dx + x, dy - y

frame = svgwrite.Drawing("foo2.svg", profile="tiny")

for i in range(0, 20):
    thing = 100 - (10 * i)
    frame.add(frame.line(start=C(-100, thing), end=C(100, thing), stroke='lightgrey', stroke_width=1))
    frame.add(frame.line(start=C(thing, 100), end=C(thing, -100), stroke='lightgrey', stroke_width=1))

frame.add(frame.line(start=C(-100, 0), end=C(100, 0), stroke='red', stroke_width=1))
frame.add(frame.line(start=C(0, 100), end=C(0, -100), stroke='red', stroke_width=1))

frame.save()
